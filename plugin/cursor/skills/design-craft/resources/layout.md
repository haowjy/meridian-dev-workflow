# Layout

Vary spacing to group what belongs together and separate what doesn't; one
spacing value everywhere has no rhythm. Use a card when it makes content or
an interaction clearer, and nest cards only when the relationship needs it:
nesting adds depth without hierarchy.

Follow the project's z-index scale; where none exists, define one for the
layer you need instead of reaching for 999. Render dropdowns outside the
clipping container and its stacking context.

## What May Change Size

A screen's regions keep their size while the person works. When something
opens and the region beside it shrinks, then grows back on close, the person
has to find their place twice.

- **Opens over, never pushes.** A menu, a popover, a collapsible
  description, a notice or a row of details opens in a layer above what is
  there. A block that expands above a diagram or a table and squeezes it is
  the failure to look for.
- **Reserve the space or use none.** A row that sometimes appears (a
  breadcrumb, a status line, a toolbar for the current selection) keeps its
  height when empty, or sits over the content. Hover, focus and selection
  change colour and weight, not width or height.
- **Meant to resize.** A split the person drags, and a sidebar or panel they
  open, hide or resize, may change their neighbours: the person asked for
  it. Give each a visible control where they would look for it (a labelled
  or familiar icon button in the toolbar, an edge that shows it drags), and
  remember the choice.
- **Extra room goes to the content.** Don't add a column or a gutter to hold
  something occasional. If a thing must sit beside the content, it takes one
  of the regions meant to resize.
