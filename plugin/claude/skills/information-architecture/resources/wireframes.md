# Grey-Box Wireframes

The kit is a fixed set of CSS classes in `assets/wireframe.css`. A wireframe
page links that file and uses only its classes, so what's left to choose is
structure and words.

## Start a Page

Copy `assets/template.html` and `assets/wireframe.css` from this skill into
one folder. The template is the page with one empty screen: each screen is a
`<figure>`, a `<figcaption>` that names the screen and says what it decides
and what stays open, then the `.wf-screen` drawing. The page ends with the
open questions. `assets/example.html` shows the classes at work in one
filled screen; its layout is one product's, not a starting point.

## The Classes

| Part | Classes |
|---|---|
| Screen | `.wf-screen` (960×540; `.phone` makes it 390×780, and its `.wf-rail` the bottom tab bar) |
| Frame | `.wf-rail` with `.wf-rail-item`, `.wf-sidebar`, `.wf-main`, `.wf-topbar` |
| Layout | `.wf-hbox`, `.wf-vbox`, `.wf-grow`, `.wf-grid` (cards or tiles that wrap), `.wf-spacer`, `.wf-divider` |
| Panels | `.wf-panel` with `.wf-tabs`, `.wf-tab` and `.wf-body` |
| Wayfinding | `.wf-crumbs` and `.wf-steps`, each holding one `<span>` per crumb or step |
| Content | `.wf-title`, `.wf-label`, `.wf-muted`, `.wf-item` (with `.wf-end` for a note at its right; `data-depth="1"` to `"3"` indents it in a tree), `.wf-btn`, `.wf-chip`, `.wf-badge`, `.wf-avatar` (initials), `.wf-msg` (a chat message), `.wf-progress` holding one `<i>` with its `width`, `table.wf-table` |
| Form | `.wf-input`, `.wf-select`, `.wf-textarea`, `.wf-check`, `.wf-radio`, `.wf-switch`, `.wf-seg` (a segmented control holding `<span>`s); a field is a `.wf-vbox` with a `.wf-muted` label over its control |
| Placeholders | `.wf-img` (a crossed box: an image, a viewer, a chart), `.wf-empty` (a dashed area: an empty state, a drop zone), `.wf-lines` holding `<i></i>` bars for body text |
| Overlays | `.wf-pop` (a menu or dialog placed with `top`/`left`), `.wf-scrim` behind a dialog, `.wf-drawer` (from the right edge), `.wf-toast`, `.wf-zone` (a drop target placed with `top`/`left`/`width`/`height`) |
| Annotation | `.wf-note`, a remark on the drawing that isn't part of the product |
| States | `.on` (selected, current, checked) on `.wf-rail-item`, `.wf-tab`, `.wf-item`, `.wf-chip`, a `.wf-table` row, a form control, and a `.wf-seg` or `.wf-steps` span; `.done` on a `.wf-steps` span; `.caret` on a `.wf-item` that opens, with `.open` when it is; `.mine` on the person's own `.wf-msg`; `.focus` on `.wf-panel`; `.primary` on `.wf-btn`; `.flat` on `.wf-item`; `.phone` on `.wf-screen`; `.hot` (needs the person) and `.dashed` (proposed, or being dragged) on any bordered box. Elsewhere a state draws nothing. |

Only sizing and placement go inline: `width`, `height`, `min-`/`max-` sizes,
`flex`, `flex-basis`, `gap`, and `top`/`left`/`right`/`bottom` on an overlay.
Build a shape the kit lacks from panels, items and placeholders, and name it
in words.

Write the words the screen would show: the real names of things, real
labels, a few believable rows. A word stands in for an icon, and ↗ after
it marks a link that leaves the product. Use `.wf-lines` only for body text
nobody reads at this stage.

## Check

1. Run `python3 <skill dir>/scripts/validate.py page.html` and fix the
   page, not the check, until it passes.
2. Render the page and look at a screenshot of every screen
   (`/meridian-dev-workflow:agent-browser`): text that clips or wraps badly, a panel squeezed to
   nothing, a first view that isn't calm. Fix it and look again.

The folder opens from `file://` with no build step; share or serve it the
way the project shares HTML.
