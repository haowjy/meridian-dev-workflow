# Designing a New Direction

A direction is a position on who the product serves and how it works for
them, made visible. A direction that could belong to any product has taken
no position: a stat-tile row, bordered cards, one blue accent. Work from the
people inward, and only then draw. First name what the brief changes
(structure, identity, or both) and what it keeps; keep those parts as they
are.

## Start From the Audience

Name who uses it, what they come to do, where (a lab bench, a dark reading
room, between meetings), how often, and which tools they already live in.
Derive density, pace, light or dark, and tone from those answers, and write
each derivation down: "they compare twenty scans at a glance, so rows stay
dense and numbers align." A choice with no derivation is a default; replace
it or make it on purpose.

## Inventory the Components They Need

Before drawing, list the jobs on each screen and the components those jobs
need. Every component traces to a job; cut the ones that trace to none, even
when similar products have them. Name the few components the user spends
most of their time in. They carry the direction, so design them hardest and
let the rest follow their language.

Make the mockup explain itself. Give it a notes layer the viewer can toggle
that says, for every control, label, and panel, which job it serves and what
it does. Writing these notes is the test: a control whose note you can't
write gets cut, and a job no control serves is a missing feature. Draw it,
or list it in the report as a proposed feature.

## Design How Components Work Together

Decide how selecting something in one component changes the others, what
stays put when the user moves between screens (state that is costly to
reload must persist), where panels open, dock, and collapse, and where focus
goes. Make the mockup clickable, and show the states that change the layout:
live, empty, many items, error.

## Give It an Identity

For a new or replacement identity, draw it from the audience and the
domain's own world, not from the product category. Borrow the domain's
qualities (the precision of an instrument, the calm of a reading room), not
its props: a working screen dressed as a fake terminal or lab label is a
costume. Settle type, colour, density, and one or two signature moves, apply
them in every component, and make each choice with `/design-craft`.
Directions offered side by side differ in position, not in palette.

Test for defaults: sketch the layout you would make for a different product
in the same category. For each choice the two share, name what in this
audience's jobs justifies it; keep the conventions that earn their place and
rethink the ones you can't explain.

## Trace Constraints to the Human

Build on what the human decided. When a rule reaches you through an agent's
summary or notes, follow it back to its source: honor it when the human or
an authoritative project document set it, and flag it when the trail ends in
an agent's own conclusion. Where the brief is thin, choose, and state what
you assumed.

## Look at What Renders

Render every screen the brief names at the real viewport, look at each
screenshot, and run `/design-craft`'s page checks on each screen before you
report. Walk the primary task in a browser once, clicking through the
cross-component changes and persistence you designed, and report which
interactions work and which are only drawn. Include a short style sheet
(type, colours, the core components) so the direction can be judged and
reused.
