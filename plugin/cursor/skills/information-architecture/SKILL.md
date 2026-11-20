---
name: information-architecture
description: 'Load before the first mockup of an unsettled product, area, or redesign, or when reviewing what opens upfront vs. behind a click: defines the domain things, nesting, and frame, then draws grey-box wireframes before styling.'
metadata:
  type: reference
alwaysApply: false
---

# Information Architecture

Settle how the product is organised before anything about how it looks. A
styled screen drawn while the structure is open fills the gaps with the
average app layout, and the human's reaction goes to colour and type instead
of the structure. A screen that is "too busy" one round and "too bare" the
next usually has a structure nobody decided.

## Work From the Things

1. **Name the things** people work with, in their own words (a study, a
   sample, a run), each with what it holds and what people do with it. Take
   them from the jobs people come to do, the product as it is, and the
   project's vocabulary. Cut a thing no job needs.
2. **Nest them.** For each thing, what owns it, what it holds, and what it
   only refers to. Draw this as a Mermaid graph, solid arrows for ownership
   and dotted for references. Navigation mostly follows ownership.
3. **Give each thing a place**: a screen, a tab, a panel, a row inside its
   owner, or a detail that opens in place. A thing that holds others and
   that people come back to gets a place of its own; one people only glance
   at lives inside its owner.
4. **Choose the frame**, the parts every screen shares (a rail, a sidebar, a
   top bar, a workspace), and the one question each part answers ("which
   study?", "what am I looking at?"). Cut a part whose question you can't
   state.
5. **Decide what each screen opens with.** The first view is calm: the thing
   the person came for and the next choice they make, and only that stands
   out. What people reach for only sometimes (history, evidence, a
   comparison they don't make every visit) opens on request, in place or as
   a tab, one step away. Nothing the person needs lives only in a tooltip.

Write the result in a markdown file beside the wireframe page, linked from
it: the things and what each holds, the graph, the frame, and each
choice with the reason the jobs give. Once the human accepts a structure, it
moves to where the project keeps its design decisions, with their answers
beside the choices they settle and what is still open.

## Draw Wireframes

Draw the screens as grey-box wireframes: layout and the words on screen,
with no colour, type or decoration to judge. Draw the screens that decide
something: the first view, the screen people spend most time in, each place
the frame changes, and the states that change the layout (empty, many items,
something that needs the person).

Each step up in fidelity costs more tokens to make and to change, and gives
more control over how the screen feels:

1. **Markdown with the Mermaid graph**: the things and how they nest, with
   no layout. Enough when the open question is what the things are.
2. **HTML grey-box wireframes**, the default (`resources/wireframes.md`):
   a fixed set of CSS classes, laid out by the browser and checked by a
   script. Cheap to write and to change, but spacing and density are the
   kit's.
3. **SVG grey-box wireframes** (`resources/svg-wireframes.md`): every box
   placed by hand, so spacing, density, overlap, a drag in progress or a
   canvas look exactly as drawn, and the human can judge how the screen
   feels. Several times the tokens, and each change moves coordinates.
4. **A styled HTML mockup with believable data** (`/meridian-dev-workflow:uxdev`): colour, type
   and real content. It starts from the structure the human accepted.

Draw at the lowest step that shows what the human has to decide, and move
up when they ask or when the question is one the lower step can't show.
The human reacts to the wireframes before anything is styled.
