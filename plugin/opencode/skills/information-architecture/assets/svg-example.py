"""Builds svg-example.html with svgkit: one product's screens, to show the primitives at work.
Its layout is that product's, not a starting point. Run: python3 svg-example.py"""
from svgkit import *

RW, SW = 48, 240
X0 = RW + SW
MW = W - X0


def frame(sidebar_body, lit="Projects"):
    return rail(["Projects", "Inbox", "Docs ↗"], lit, badges={"Inbox": 2}) + sidebar(RW, SW, "Garden plan", action="+") + sidebar_body(RW)


def notes_list(x):
    out = input_(x + 10, 36, SW - 20, "Search notes") + label(x + 12, 84, "Needs you")
    out += item(x + 10, 92, SW - 20, "Order seeds", "due today", hot=True) + label(x + 12, 140, "Notes")
    y = 148
    for s, d, on, c in [("Bed layout", 0, True, "open"), ("North bed", 1, False, None), ("South bed", 1, False, None), ("Watering", 0, False, "closed")]:
        out += item(x + 10, y, SW - 20, s, on=on, flat=True, depth=d, caret=c); y += 28
    return out


def note_body(x, y, w, h):
    out = text(x + 14, y + 26, "Bed layout", 14, 700) + chip(x + 14, y + 38, "Spring", on=True) + chip(x + 80, y + 38, "Summer")
    out += img(x + 14, y + 70, w - 28, 200, "Plan drawing") + lines(x + 14, y + 290, w - 60, 3)
    return out


def comments(x, y, w, h):
    m, mh = msg(x + 10, y + 12, w - 20, "Ana: should we move the beans to the south bed?")
    r, rh = msg(x + 10, y + 20 + mh, w - 20, "Yes, after the frost.", mine=True)
    return m + r + composer(x + 8, y + h - 42, w - 16, "Reply")


def s_note():
    return (frame(notes_list)
            + panel(X0 + 8, 8, MW - 290, H - 16, ["Bed layout", "Watering"], focus=True, body=note_body)
            + panel(W - 278, 8, 270, H - 16, ["Comments"], close=False, plus=False, body=comments))


def s_drag():
    out = frame(notes_list) + panel(X0 + 8, 8, MW - 16, H - 16, ["Bed layout", "Watering"], focus=True, body=note_body)
    out += zone(X0 + MW / 2, 44, MW / 2 - 16, H - 60, "Drop: new panel")
    return out + ghost(X0 + MW * .6, 140, "Watering") + arrow(X0 + 200, 22, X0 + MW * .6 - 6, 150, dash=True)


def s_phone():
    w, h = 390, 780
    out = rect(0, 0, w, 48, PAPER, r=0, stroke=LINE, sw=1) + text(14, 30, "Garden plan", 14, 700)
    out += item(12, 62, w - 24, "Order seeds", "due today", hot=True)
    y = 104
    for s in ["Bed layout", "Watering", "Seeds to buy"]:
        out += item(12, y, w - 24, s, "edited 2d"); y += 34
    out += rect(0, h - 60, w, 60, RAIL, r=0, stroke=LINE, sw=1)
    for i, s in enumerate(["Projects", "Inbox", "me"]):
        cx = w * (i + .5) / 3
        out += rect(cx - 12, h - 52, 24, 24, DARK if i == 0 else PAPER, r=6, stroke=INK if i == 0 else LINE) + text(cx, h - 16, s, 8.5, 700 if i == 0 else 400, "middle")
    return out + toast(w / 2, h - 110, "Note saved", "Undo")


page("svg-example.html", "Wireframes: Project notes",
     '<p>Structure only: no colour, type or visual choices. The things, how they nest and where each '
     'one opens are in <a href="information-architecture.md">the information architecture</a>.</p>',
     [("Screens", [
         ("note", "A project, one note open", "Decides: the sidebar lists the project's notes, and a note opens as a tab. Open: whether comments get their own panel.", s_note),
         ("drag", "Splitting: drag a tab to an edge", "Decides: dropping a tab on a panel's edge makes a new panel.", s_drag),
         ("phone", "Phone", "Decides: on a phone the notes list is the first view and the panels become one screen each.", s_phone, 390, 780),
     ])],
     ["Do comments get their own panel, or sit under the note? The panel keeps them beside the drawing; under the note frees the width. I'd pick the panel."])
