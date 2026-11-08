#!/usr/bin/env bash
# Capture a scroll range of the page open in an agent-browser session as a
# frame strip (evenly spaced screenshots tiled in reading order) and,
# optionally, a video of a steady scroll through the same range and frame
# timings measured during three steady scrolls through it.
#
# Usage: motion-strip.sh --session NAME --from A --to B [--frames N]
#          [--settle MS] [--cols C] [--video SECONDS] [--perf SECONDS] OUT_DIR
# A and B are scroll positions in viewport heights (2.5 = 2.5 * innerHeight).
# Open the page and set the viewport in the session first.
set -euo pipefail

usage() { sed -n '2,10p' "$0" >&2; exit 2; }
session="" from="" to="" frames=12 settle=400 cols=4 video="" perf="" out=""
while [ $# -gt 0 ]; do
  case "$1" in
    --session|--from|--to|--frames|--settle|--cols|--video|--perf)
      [ $# -ge 2 ] || usage
      v="$2"; case "$1" in
        --session) session="$v" ;; --from) from="$v" ;; --to) to="$v" ;;
        --frames) frames="$v" ;; --settle) settle="$v" ;; --cols) cols="$v" ;;
        --video) video="$v" ;; --perf) perf="$v" ;;
      esac; shift 2 ;;
    -h|--help) sed -n '2,10p' "$0"; exit 0 ;;
    -*) echo "unknown option: $1" >&2; usage ;;
    *) [ -z "$out" ] || usage; out="$1"; shift ;;
  esac
done
[ -n "$session" ] && [ -n "$from" ] && [ -n "$to" ] && [ -n "$out" ] || usage
num='^[0-9]+([.][0-9]+)?$'
int='^[0-9]+$'
[[ $from =~ $num && $to =~ $num ]] || { echo "--from and --to take numbers of viewport heights" >&2; exit 2; }
[[ $frames =~ $int && $frames -ge 2 ]] || { echo "--frames takes a whole number, 2 or more" >&2; exit 2; }
[[ $cols =~ $int && $cols -ge 1 ]] || { echo "--cols takes a whole number, 1 or more" >&2; exit 2; }
[[ $settle =~ $int ]] || { echo "--settle takes milliseconds" >&2; exit 2; }
[ -z "$video" ] || [[ $video =~ $num ]] || { echo "--video takes seconds" >&2; exit 2; }
[ -z "$perf" ] || [[ $perf =~ $num ]] || { echo "--perf takes seconds" >&2; exit 2; }
command -v ffmpeg >/dev/null || { echo "ffmpeg is required for the strip" >&2; exit 1; }

ab() { agent-browser --session "$session" "$@"; }
mkdir -p "$out"
# The browser daemon resolves paths from its own directory, not ours.
out=$(cd "$out" && pwd)
rm -f "$out"/frame-*.png

# Scroll instantly whatever the page's scroll-behavior, then wait for
# scroll-driven films that ease toward the scroll target to settle.
for ((i = 0; i < frames; i++)); do
  pos=$(awk -v a="$from" -v b="$to" -v i="$i" -v n="$frames" 'BEGIN { printf "%.3f", a + (b - a) * i / (n - 1) }')
  got=$(ab eval "new Promise(r => { scrollTo({ top: innerHeight * $pos, behavior: 'instant' }); setTimeout(() => requestAnimationFrame(() => requestAnimationFrame(() => r((scrollY / innerHeight).toFixed(3)))), $settle) })" | tr -d '"')
  file=$(printf '%s/frame-%02d.png' "$out" "$((i + 1))")
  ab screenshot "$file" >/dev/null
  note=""
  awk -v a="$pos" -v b="$got" 'BEGIN { d = a - b; exit !(d > 0.01 || d < -0.01) }' && note="  (asked for $pos; the page stopped there)"
  echo "$(basename "$file")  ${got} vh${note}"
done

rows=$(( (frames + cols - 1) / cols ))
ffmpeg -v error -y -framerate 1 -i "$out/frame-%02d.png" \
  -vf "scale=480:-2,pad=iw+8:ih+8:4:4:color=gray,tile=${cols}x${rows}" \
  -frames:v 1 "$out/strip.png"
echo "strip: $out/strip.png (${cols} per row, left to right, top to bottom)"

if [ -n "$video" ]; then
  ab record start "$out/scroll.webm" >/dev/null
  trap 'ab record stop >/dev/null 2>&1 || true' EXIT
  ab eval "new Promise(r => { const a = innerHeight * $from, b = innerHeight * $to, T = $video * 1000, t0 = performance.now(); (function step() { const k = Math.min(1, (performance.now() - t0) / T); scrollTo({ top: a + (b - a) * k, behavior: 'instant' }); k < 1 ? requestAnimationFrame(step) : setTimeout(() => r(scrollY), 1000) })() })" >/dev/null
  trap - EXIT
  ab record stop >/dev/null
  echo "video: $out/scroll.webm (recording reloads the page, so state set before it is gone; judge order and continuity from the strip)"
fi

if [ -n "$perf" ]; then
  # Frame gaps from requestAnimationFrame and the browser's own long
  # animation frames (over 50ms), during a steady scroll. Headless Chrome on
  # this machine is not a phone: treat the numbers as relative, before and
  # after a change.
  echo "frame timing over ${perf}s, three runs:"
  for run in 1 2 3; do
    ab eval "new Promise(r => { scrollTo({ top: innerHeight * $from, behavior: 'instant' }); setTimeout(() => {
      const a = innerHeight * $from, b = innerHeight * $to, T = $perf * 1000, gaps = [], loaf = [];
      let po = null;
      try { po = new PerformanceObserver(l => loaf.push(...l.getEntries())); po.observe({ type: 'long-animation-frame' }); } catch {}
      let last = null; const t0 = performance.now();
      (function step(now) {
        if (last !== null) gaps.push(now - last); last = now;
        const k = Math.min(1, (performance.now() - t0) / T);
        scrollTo({ top: a + (b - a) * k, behavior: 'instant' });
        if (k < 1) return requestAnimationFrame(step);
        if (po) po.disconnect();
        const s = [...gaps].sort((x, y) => x - y), q = p => s[Math.min(s.length - 1, Math.floor(p * s.length))] || 0;
        const median = q(0.5);
        const scripts = {};
        for (const e of loaf) for (const sc of e.scripts || []) { const k = (sc.sourceURL || sc.invoker || '?').split('/').pop().slice(0, 60); scripts[k] = (scripts[k] || 0) + sc.duration; }
        const worst = Object.entries(scripts).sort((x, y) => y[1] - x[1]).slice(0, 3).map(([k, v]) => k + ' ' + Math.round(v) + 'ms').join(', ');
        r('frames ' + gaps.length + ', median ' + median.toFixed(1) + 'ms, p95 ' + q(0.95).toFixed(1) + 'ms, worst ' + (s[s.length - 1] || 0).toFixed(1) + 'ms, slow (>1.5x median) ' + gaps.filter(g => g > median * 1.5).length + ', long animation frames ' + loaf.length + (worst ? ' (scripts: ' + worst + ')' : ''));
      })(performance.now());
    }, $settle) })" | tr -d '"' | sed "s/^/  run $run: /"
  done
fi
