// Inventory the page's CSS and Web Animations: what animates, how long, on
// which curve, and the choices that usually need a reason.
// Run in the page: agent-browser eval --stdin < motion-audit.js
// Prints JSON. Every finding is a question for judgment, not a failure.
// Motion drawn by script each frame (requestAnimationFrame, canvas, WebGL)
// is invisible here; review it with motion-strip.sh.
(() => {
  const MAX = 25;
  const MAX_ELEMENTS = 5000;
  const LAYOUT = /^(width|height|top|left|right|bottom|margin|padding|inset|max-|min-|flex-basis|grid-template)/;
  const where = (el) => {
    const parts = [];
    for (let n = el; n && n.nodeType === 1 && parts.length < 4; n = n.parentElement) {
      let p = n.tagName.toLowerCase();
      if (n.id) { parts.unshift(`${p}#${n.id}`); break; }
      const cls = [...n.classList].slice(0, 2).join(".");
      if (cls) p += "." + cls;
      parts.unshift(p);
    }
    return parts.join(" > ");
  };
  const tally = (map, key) => map.set(key, (map.get(key) || 0) + 1);
  const top = (map) => [...map].sort((a, b) => b[1] - a[1]).slice(0, 12).map(([value, count]) => ({ value, count }));
  const ms = (s) => Math.round(parseFloat(s) * (s.trim().endsWith("ms") ? 1 : 1000));

  // Running and pending animations, including CSS animations and transitions.
  const running = [];
  const fromNothing = [];
  const layoutAnimated = [];
  let infinite = 0;
  for (const a of document.getAnimations()) {
    const effect = a.effect;
    const target = effect && effect.target;
    const timing = effect ? effect.getTiming() : {};
    const frames = effect && effect.getKeyframes ? effect.getKeyframes() : [];
    const props = [...new Set(frames.flatMap((f) => Object.keys(f).filter((k) => !["offset", "easing", "composite", "computedOffset"].includes(k))))];
    const row = {
      kind: a.constructor.name,
      name: a.animationName || a.transitionProperty || a.id || "",
      where: target ? where(target) : "",
      properties: props,
      duration_ms: typeof timing.duration === "number" ? Math.round(timing.duration) : timing.duration,
      delay_ms: Math.round(timing.delay || 0),
      easing: timing.easing,
      iterations: timing.iterations,
      state: a.playState,
    };
    running.push(row);
    if (timing.iterations === Infinity) infinite++;
    if (props.some((p) => LAYOUT.test(p.replace(/[A-Z]/g, (c) => "-" + c.toLowerCase())))) layoutAnimated.push(row);
    if (frames.some((f) => /scale\(\s*0\s*\)|scale3d\(\s*0\s*,|scale:\s*0(\s|$)/.test(`${f.transform || ""} scale:${f.scale ?? ""}`))) fromNothing.push(row);
  }

  // Declared transitions, which exist only while running, so read them from
  // computed style.
  const durations = new Map();
  const easings = new Map();
  const transitionAll = [];
  const layoutTransitions = [];
  const els = document.querySelectorAll("body *");
  for (let i = 0; i < els.length && i < MAX_ELEMENTS; i++) {
    const s = getComputedStyle(els[i]);
    const props = s.transitionProperty.split(",").map((p) => p.trim());
    const durs = s.transitionDuration.split(",").map(ms);
    if (!durs.some((d) => d > 0)) continue;
    const curves = s.transitionTimingFunction.split(/,(?![^(]*\))/).map((c) => c.trim());
    props.forEach((p, j) => {
      const d = durs[j % durs.length];
      if (!d) return;
      tally(durations, `${d}ms`);
      tally(easings, curves[j % curves.length]);
      const row = { where: where(els[i]), property: p, duration_ms: d, easing: curves[j % curves.length] };
      if (p === "all") transitionAll.push(row);
      else if (LAYOUT.test(p)) layoutTransitions.push(row);
    });
  }
  for (const a of running) {
    if (typeof a.duration_ms === "number" && a.duration_ms > 0) tally(durations, `${a.duration_ms}ms`);
    if (a.easing) tally(easings, a.easing);
  }

  // A reduced-motion rule in any readable stylesheet.
  let reducedMotionRules = 0;
  let unreadableSheets = 0;
  const scan = (rules) => {
    for (const r of rules) {
      if (r.media && /prefers-reduced-motion/.test(r.media.mediaText)) reducedMotionRules++;
      if (r.cssRules) scan(r.cssRules);
    }
  };
  for (const sheet of document.styleSheets) {
    try { scan(sheet.cssRules); } catch { unreadableSheets++; }
  }

  return {
    url: location.href,
    counts: {
      running: running.length,
      infinite_loops: infinite,
      transition_all: transitionAll.length,
      layout_properties: layoutAnimated.length + layoutTransitions.length,
      from_scale_zero: fromNothing.length,
      distinct_durations: durations.size,
      distinct_easings: easings.size,
      reduced_motion_rules: reducedMotionRules,
      unreadable_stylesheets: unreadableSheets,
    },
    durations: top(durations),
    easings: top(easings),
    running: running.slice(0, MAX),
    transition_all: transitionAll.slice(0, MAX),
    layout_properties: [...layoutAnimated, ...layoutTransitions].slice(0, MAX),
    from_scale_zero: fromNothing.slice(0, MAX),
  };
})();
