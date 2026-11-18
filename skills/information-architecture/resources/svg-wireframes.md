# SVG Wireframes

The same grey-box wireframes, drawn as SVG by a short Python script. Every
box sits where you place it, and each screen scales to the page width.
Nothing lays text out for you, so a label can run into what you placed
beside it.

## Start a Page

Copy `assets/svgkit.py` from this skill beside a `build.py` of your own.
`assets/svg-example.py` is a build script for three screens of one product;
read it for how the pieces fit, not for its layout. A build script:

- does `from svgkit import *`;
- draws each screen as a function that returns SVG markup on a `W`×`H`
  (960×540) screen, or 390×780 for a phone;
- shares a function for anything every screen has (the frame, a list), so
  a structural change is one edit;
- ends with `page(path, title, intro, sections, questions)`, which writes
  the HTML page with each screen in a `<figure>` and its caption.

Run `python3 build.py` after every change and commit the script with the
page; the script is the source.

## The Primitives

`svgkit.py` documents each one; they are:

| Part | Functions |
|---|---|
| Frame | `rail`, `sidebar`, `topbar`, `panel` (a bordered box with `tabbar` or a title, and a `body(x, y, w, h)` that draws inside it) |
| Rows | `item` (a list or tree row: note, `on`, `hot`, `flat`, `depth`, `caret`), `table` |
| Controls | `btn`, `input_`, `select`, `check` (`kind="radio"` or `"switch"`), `chip`, `badge`, `avatar`, `progress` |
| Text | `text` (with `width` to clip), `label` (a group label), `lines` (unread body text), `fit`, `tw` (estimated width) |
| Placeholders | `img` (a crossed box; `dark=True` for an image viewer), `empty` (a dashed slot) |
| Conversation | `msg` (returns the markup and its height, so you stack messages), `composer`, `card` (a question with its button) |
| Overlays | `pop`, `scrim`, `drawer`, `toast`, `zone` (a lit drop target), `ghost` (what is being dragged) |
| Annotation | `note`, `arrow` |
| Shapes | `rect`, `line`, `circle`, `bar`, for what no primitive draws |

Draw with the palette constants (`INK`, `LINE`, `FILL`, `SOFT`, `DARK`,
`MUTED`, `PAPER`); `page()` refuses any other colour, an embedded image or
a script. Pass a `width` to any text that sits beside something else, so a
long name ends in an ellipsis instead of running under its neighbour; the
row and tab primitives do this already. The writing rules are the HTML
kit's (`resources/wireframes.md`): real names and labels, a word for an
icon, ↗ for a link that leaves the product.

## Check

Render the page and look at a screenshot of every screen (`/agent-browser`):
text that collides or clips, a box that pokes out of its panel, a first
view that isn't calm. Fix the script and look again.
