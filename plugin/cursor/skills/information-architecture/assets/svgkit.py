"""Grey-box SVG wireframe primitives.

Copy this file beside a build.py that does `from svgkit import *`, draws each screen as a
function returning SVG markup, and calls `page(...)`. Every primitive takes absolute
coordinates on a W x H screen and draws in the grey palette below; `page()` refuses any
other colour, an embedded image or a script. Labels are clipped with an ellipsis to the
box they sit in, so a long name can't overflow its row.
"""

import html
import re
from pathlib import Path

W, H = 960, 540  # a desktop screen; pass w=390, h=780 to screen() for a phone

INK, LINE, FILL, SOFT, DARK, MUTED, PAPER, RAIL, SIDE, VIEW = (
    "#2b2b2b", "#8c8c8c", "#f1f1f1", "#dcdcdc", "#bdbdbd", "#5c5c5c", "#ffffff", "#fafafa", "#fcfcfc", "#3a3a3a")
PALETTE = {INK, LINE, FILL, SOFT, DARK, MUTED, PAPER, RAIL, SIDE, VIEW, "#888888", "#eeeeee"}

e = html.escape


# ------------------------------------------------------------------ text
def tw(s, size=12, weight=400):
    """Estimated width of s in px."""
    return len(s) * size * (0.6 if weight >= 600 else 0.55)


def fit(s, size, width, weight=400):
    """s, cut with an ellipsis to fit width."""
    if width <= 0:
        return ""
    if tw(s, size, weight) <= width:
        return s
    n = max(0, int(width / (size * (0.6 if weight >= 600 else 0.55))) - 1)
    return s[:n].rstrip() + "…"


def text(x, y, s, size=12, weight=400, anchor="start", fill=INK, width=None, italic=False):
    """Text with its baseline at y. width clips it with an ellipsis."""
    if width is not None:
        s = fit(s, size, width, weight)
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{fill}"{st}>{e(s)}</text>')


def label(x, y, s):
    """A small uppercase group label: NEED YOU, STUDIES."""
    return text(x, y, s.upper(), 9, 700, fill=MUTED)


# ------------------------------------------------------------------ shapes
def rect(x, y, w, h, fill="none", r=4, stroke=LINE, sw=1.2, dash=False, opacity=None):
    d = ' stroke-dasharray="5 4"' if dash else ""
    o = f' fill-opacity="{opacity}"' if opacity is not None else ""
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}"{o}{s}{d}/>'


def line(x1, y1, x2, y2, stroke=LINE, sw=1, dash=False):
    d = ' stroke-dasharray="5 4"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def circle(cx, cy, r, fill="none", stroke=LINE, sw=1.2):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}"{s}/>'


def arrow(x1, y1, x2, y2, stroke=INK, sw=1.4, dash=False):
    """A line with a head at (x2, y2): a flow, a drag path, an annotation pointer."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p = [(x2 - 8 * math.cos(a - .45), y2 - 8 * math.sin(a - .45)), (x2 - 8 * math.cos(a + .45), y2 - 8 * math.sin(a + .45))]
    return line(x1, y1, x2, y2, stroke, sw, dash) + (
        f'<path d="M{p[0][0]:.1f},{p[0][1]:.1f} L{x2:.1f},{y2:.1f} L{p[1][0]:.1f},{p[1][1]:.1f}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>')


def bar(x, y, w, h=6, fill=SOFT):
    return rect(x, y, w, h, fill, r=h / 2, stroke=None)


def lines(x, y, w, n, gap=14):
    """n ragged grey bars: body text nobody reads at this stage."""
    rag = (1, .84, .93, .62, .88, .7)
    return "".join(bar(x, y + i * gap, w * rag[i % len(rag)]) for i in range(n))


# ------------------------------------------------------------------ controls
def btn(x, y, s, w=None, primary=False):
    """A pill button; returns markup. Its width is w or fits the label."""
    w = w or tw(s, 11, 600) + 22
    return (rect(x, y, w, 24, DARK if primary else PAPER, r=12, stroke=INK if primary else LINE, sw=1.4 if primary else 1.2)
            + text(x + w / 2, y + 16, s, 11, 700 if primary else 500, "middle", width=w - 12))


def btn_w(s):
    return tw(s, 11, 600) + 22


def input_(x, y, w, placeholder="", h=28):
    return rect(x, y, w, h, PAPER) + text(x + 9, y + h / 2 + 4, placeholder, 11, 400, fill=MUTED, width=w - 16)


def select(x, y, w, value):
    return input_(x, y, w, "") + text(x + 9, y + 18, value, 11, width=w - 30) + text(x + w - 10, y + 18, "▾", 10, fill=MUTED, anchor="end")


def check(x, y, s, on=False, kind="check"):
    """A checkbox, radio (kind="radio") or switch (kind="switch") with its label."""
    if kind == "switch":
        out = rect(x, y, 26, 15, DARK if on else PAPER, r=7.5, stroke=INK if on else LINE) + circle(x + (18 if on else 8), y + 7.5, 4, INK if on else LINE, None)
        return out + text(x + 32, y + 11.5, s, 11)
    r = 6.5 if kind == "radio" else 2
    out = rect(x, y + 1, 13, 13, PAPER, r=r, stroke=INK if on else LINE)
    if on:
        out += rect(x + 3, y + 4, 7, 7, INK, r=r / 2, stroke=None)
    return out + text(x + 19, y + 11.5, s, 11)


def chip(x, y, s, on=False):
    w = tw(s, 10.5) + 18
    return rect(x, y, w, 20, SOFT if on else PAPER, r=10, stroke=INK if on else LINE, sw=1) + text(x + w / 2, y + 14, s, 10.5, 600 if on else 400, "middle")


def badge(cx, cy, n):
    """A count on a dark dot, centred at (cx, cy)."""
    return circle(cx, cy, 7, INK, None) + text(cx, cy + 3.2, str(n), 8.5, 700, "middle", PAPER)


def avatar(cx, cy, initials, r=12):
    return circle(cx, cy, r, FILL) + text(cx, cy + 3, initials, 8.5, 700, "middle")


def progress(x, y, w, frac):
    return bar(x, y, w) + bar(x, y, w * frac, fill=INK)


# ------------------------------------------------------------------ rows and lists
def item(x, y, w, s, note="", on=False, hot=False, flat=False, depth=0, caret=None, h=26):
    """A list row. caret is "open", "closed" or None; depth indents it in a tree."""
    out = ""
    if not flat or on:
        out += rect(x, y, w, h, SOFT if on else PAPER, stroke=INK if (on or hot) else (LINE if not flat else None), sw=1.6 if hot else 1.2)
    tx = x + 9 + depth * 14
    if caret:
        out += text(tx, y + h / 2 + 4, "▾" if caret == "open" else "▸", 9, fill=MUTED)
        tx += 12
    nw = tw(note, 10.5) + 14 if note else 0
    out += text(tx, y + h / 2 + 4, s, 11.5, 700 if (on or hot) else 400, width=x + w - tx - nw - 6)
    if note:
        out += text(x + w - 9, y + h / 2 + 4, note, 10.5, fill=MUTED, anchor="end")
    return out


def table(x, y, w, headers, rows, widths=None, on=None, row_h=24):
    """headers and rows of strings; widths are column fractions; on is a selected row index."""
    widths = widths or [1 / len(headers)] * len(headers)
    out = line(x, y + row_h, x + w, y + row_h, INK, 1.2)
    cx = x
    for hd, f in zip(headers, widths):
        out += text(cx + 6, y + 16, hd, 10.5, 700, width=w * f - 10); cx += w * f
    yy = y + row_h
    for i, r in enumerate(rows):
        if i == on:
            out += rect(x, yy, w, row_h, SOFT, r=0, stroke=None)
        cx = x
        for c, f in zip(r, widths):
            out += text(cx + 6, yy + 16, c, 10.5, 600 if i == on else 400, width=w * f - 10); cx += w * f
        yy += row_h
        out += line(x, yy, x + w, yy, SOFT)
    return out


# ------------------------------------------------------------------ placeholders
def img(x, y, w, h, s="", dark=False):
    """A crossed box: an image, a chart, a map. dark=True draws an image viewer."""
    bg, fg = (VIEW, "#888888") if dark else (FILL, DARK)
    out = rect(x, y, w, h, bg, r=3, stroke=None if dark else LINE)
    out += line(x, y, x + w, y + h, fg) + line(x + w, y, x, y + h, fg)
    if s:
        out += text(x + w / 2, y + h / 2 + 4, s, 10.5, 600, "middle", "#eeeeee" if dark else MUTED)
    return out


def empty(x, y, w, h, s=""):
    """A dashed area: an empty state, a slot."""
    return rect(x, y, w, h, "none", r=5, dash=True) + (text(x + w / 2, y + h / 2 + 4, s, 11, fill=MUTED, anchor="middle", width=w - 16) if s else "")


# ------------------------------------------------------------------ frame
def rail(items, lit=None, x=0, y=0, h=H, w=48, bottom=("Settings", "me"), badges=None):
    """A vertical rail of labelled buttons; items at the top, bottom ones at the foot.
    lit names the current one; badges maps an item to a count."""
    badges = badges or {}
    out = rect(x, y, w, h, RAIL, r=0, stroke=LINE, sw=1)

    def one(name, yy):
        on = name == lit
        o = rect(x + 12, yy, 24, 24, DARK if on else PAPER, r=6, stroke=INK if on else LINE, sw=1.6 if on else 1.2)
        o += text(x + w / 2, yy + 36, name, 8.5, 700 if on else 400, "middle", INK if on else MUTED, width=w - 4)
        if name in badges:
            o += badge(x + 36, yy + 1, badges[name])
        return o
    for i, name in enumerate(items):
        out += one(name, y + 12 + i * 52)
    for i, name in enumerate(reversed(bottom)):
        out += one(name, y + h - 50 - i * 52)
    return out


def sidebar(x, w, title="", y=0, h=H, action=""):
    """The sidebar's ground and its title row."""
    out = rect(x, y, w, h, SIDE, r=0, stroke=LINE, sw=1)
    if title:
        out += text(x + 12, y + 24, title, 12.5, 700, width=w - 40)
    if action:
        out += text(x + w - 12, y + 24, action, 10.5, fill=MUTED, anchor="end")
    return out


def topbar(x, y, w, title="", right=(), h=40):
    """A top bar with a title and buttons at its right."""
    out = rect(x, y, w, h, PAPER, r=0, stroke=LINE, sw=1) + text(x + 12, y + h / 2 + 5, title, 13, 700)
    cx = x + w - 10
    for s in reversed(right):
        bw = btn_w(s); cx -= bw
        out += btn(cx, y + (h - 24) / 2, s); cx -= 6
    return out


TAB_H = 30


def tabbar(x, y, w, tabs, active=0, focus=True, close=True, plus=True):
    """A row of tabs. Returns markup; the active tab is outlined, ink when its panel has focus."""
    out = rect(x, y, w, TAB_H, RAIL, r=0, stroke=LINE, sw=1)
    cx = x + 4
    for i, s in enumerate(tabs):
        t = tw(s, 11, 700) + (34 if close else 20)
        if cx + t > x + w - 30:
            out += text(cx + 4, y + 20, f"+{len(tabs) - i}", 10.5, fill=MUTED); break
        if i == active:
            out += rect(cx, y + 3, t, TAB_H - 3, PAPER, r=3, stroke=INK if focus else LINE, sw=1.6 if focus else 1.1)
            out += text(cx + 10, y + 20, s, 11, 700)
            if close:
                out += text(cx + t - 10, y + 20, "×", 10, fill=MUTED, anchor="end")
        else:
            out += text(cx + 10, y + 20, s, 11, fill=MUTED)
        cx += t + 2
    if plus:
        out += text(cx + 8, y + 20, "+", 13, fill=MUTED)
    return out


def panel(x, y, w, h, tabs=(), active=0, focus=False, title="", body=None, **tabopts):
    """A bordered panel, with a tab row or a title. body(x, y, w, h) draws its content
    in the area under the header."""
    out = rect(x, y, w, h, PAPER, r=0 if tabs else 5, stroke=INK if focus else LINE, sw=1.8 if focus else 1.2)
    top = y
    if tabs:
        out += tabbar(x, y, w, tabs, active, focus, **tabopts); top += TAB_H
    elif title:
        out += text(x + 12, y + 22, title, 12.5, 700, width=w - 24); top += 32
    if body:
        out += body(x, top, w, y + h - top)
    return out


# ------------------------------------------------------------------ conversation
def msg(x, y, w, s, mine=False, size=10.5):
    """A chat message in a column x..x+w; mine sits right. Returns (markup, height)."""
    words, rows, cur = s.split(), [], ""
    maxw = w * .85 - 18
    for wd in words:
        t = (cur + " " + wd).strip()
        if tw(t, size) > maxw and cur:
            rows.append(cur); cur = wd
        else:
            cur = t
    rows.append(cur)
    bw = max(tw(r, size) for r in rows) + 18
    bh = len(rows) * (size + 4) + 12
    bx = x + w - bw if mine else x
    out = rect(bx, y, bw, bh, FILL if mine else PAPER, r=10, stroke=SOFT if mine else LINE, sw=1)
    for i, r in enumerate(rows):
        out += text(bx + 9, y + 6 + (i + 1) * (size + 4) - 3, r, size)
    return out, bh


def composer(x, y, w, s="Message…"):
    return rect(x, y, w, 32, PAPER, r=8, sw=1.4) + text(x + 10, y + 20, s, 10.5, fill=MUTED)


def card(x, y, w, s, action, h=56):
    """A card that asks the person to act: a question and its primary button."""
    return rect(x, y, w, h, PAPER, stroke=INK, sw=1.5) + text(x + 10, y + 18, s, 10.5, 600, width=w - 20) + btn(x + 10, y + 26, action, primary=True)


# ------------------------------------------------------------------ overlays
def pop(x, y, w, h):
    """The ground of a menu, popover or dialog; draw its content on top."""
    return rect(x, y, w, h, PAPER, r=6, stroke=INK, sw=1.5)


def scrim(w=W, h=H):
    return rect(0, 0, w, h, INK, r=0, stroke=None, opacity=.08)


def drawer(w=320, sw_=W, h=H):
    """A drawer's ground at the right edge; returns (markup, its x)."""
    return rect(sw_ - w, 0, w, h, PAPER, r=0, stroke=INK, sw=1.5), sw_ - w


def toast(cx, y, s, action=""):
    w = tw(s, 10.5, 600) + (btn_w(action) + 18 if action else 24)
    out = rect(cx - w / 2, y, w, 30, PAPER, r=6, stroke=INK, sw=1.5) + text(cx - w / 2 + 12, y + 19, s, 10.5, 600)
    if action:
        out += btn(cx + w / 2 - btn_w(action) - 4, y + 3, action)
    return out


def zone(x, y, w, h, s):
    """A drop target lit while something is dragged over it."""
    return rect(x, y, w, h, INK, r=5, stroke=INK, sw=1.6, dash=True, opacity=.08) + text(x + w / 2, y + h / 2 + 4, s, 11, 700, "middle")


def ghost(x, y, s, note="dragging"):
    """A tab or row being dragged, with a note beside it."""
    t = tw(s, 11, 700) + 22
    return rect(x, y, t, 26, PAPER, r=3, stroke=INK, sw=1.6, dash=True) + text(x + 11, y + 17, s, 11, 700) + text(x + t + 6, y + 30, note, 10, fill=MUTED, italic=True)


def note(x, y, s, w=None):
    """An annotation on the drawing that isn't part of the product."""
    w = w or tw(s, 10.5) + 14
    return rect(x, y, w, 22, PAPER, r=4, stroke=INK, sw=1, dash=True) + text(x + 7, y + 15, s, 10.5, fill=MUTED, italic=True, width=w - 12)


# ------------------------------------------------------------------ page
def screen(draw, title, w=W, h=H):
    """One screen: draw() returns its markup inside a w x h frame."""
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)} wireframe" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="system-ui, -apple-system, Segoe UI, sans-serif">'
            f'{rect(0, 0, w, h, PAPER, r=0, stroke=None)}{draw()}{rect(.75, .75, w - 1.5, h - 1.5, "none", r=6, stroke=INK, sw=1.5)}</svg>')


CSS = """*{box-sizing:border-box}
body{margin:0;background:#fff;color:#1f1f1f;font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1080px;margin:0 auto;padding:32px 24px 96px}
h1{font-size:28px;line-height:1.2;margin:0 0 8px}
h2{font-size:21px;margin:48px 0 12px;padding-top:16px;border-top:1.5px solid #2b2b2b}
p,li{max-width:76ch}
a{color:inherit;text-underline-offset:2px}
figure{margin:36px 0;min-width:0}
figure .wf{overflow-x:auto}
figure svg{display:block;width:100%;min-width:680px;height:auto}
figure.phone svg{width:390px;min-width:0}
figcaption{margin-bottom:10px;font-size:14px;line-height:1.45;max-width:76ch}
figcaption b{display:block;font-size:15px}"""


def page(path, title, intro="", sections=(), questions=()):
    """Write the page. intro is HTML. sections is a list of (heading, screens), each screen
    (id, title, caption, draw) or (id, title, caption, draw, w, h). questions are HTML strings."""
    body = f"<h1>{e(title)}</h1>{intro}"
    n = 0
    for heading, screens in sections:
        body += f"<h2>{e(heading)}</h2>"
        for s in screens:
            sid, st, cap, draw, *size = s
            w, h = size or (W, H)
            n += 1
            cls = ' class="phone"' if w < 600 else ""
            body += (f'<figure id="w-{sid}"{cls}><figcaption><b>{n}. {e(st)}</b>{e(cap)}</figcaption>'
                     f'<div class="wf">{screen(draw, st, w, h)}</div></figure>')
    if questions:
        body += '<h2 id="open">Open questions</h2><ol>' + "".join(f"<li>{q}</li>" for q in questions) + "</ol>"
    out = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
           f'content="width=device-width, initial-scale=1"><title>{e(title)}</title><style>{CSS}</style>'
           f'</head><body><main>{body}</main></body></html>')
    check_page(out)
    Path(path).write_text(out)
    print(f"{path}: {n} screen(s), {len(out) // 1024} KB")


def check_page(out):
    """Refuse colour outside the palette, embedded images and scripts."""
    svg = "".join(re.findall(r"<svg.*?</svg>", out, re.S))
    bad = sorted({c for c in re.findall(r"#[0-9a-fA-F]{3,6}\b", svg) if c.lower() not in PALETTE})
    problems = [f"colour {c} is outside the grey palette" for c in bad]
    for tag in ("<image", "<script", "<foreignObject", "url("):
        if tag in out:
            problems.append(f"{tag} is not part of the kit")
    if problems:
        raise SystemExit("svgkit: " + "; ".join(problems))
