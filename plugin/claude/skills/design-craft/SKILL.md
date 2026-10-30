---
name: design-craft
description: 'Load for any frontend work, HTML reports included: makes each visual and copy choice deliberate (colour, type, layout, motion, words on screen) and catches the AI-generated defaults that show up regardless of the brief.'
metadata:
  type: reference
---

# Design Craft

Follow the brief and the product's established system; what follows are
defaults, not bans. When a requested style would break accessibility, say so
and offer a compliant option rather than silently overriding either.

## Name the Surface

The defaults that make a result read as "AI made this" depend on the kind of
surface. Name it from what the person comes to do there, not from the
product, and open its resource:

- **Persuade** (a landing or marketing page that has to win attention):
  `resources/persuade.md`.
- **Operate** (an app screen, dashboard, tool, or settings page where people
  get work done): `resources/operate.md`.
- **Read** (an HTML report, doc, or article people read to understand and
  decide): `resources/read.md`.

A surface that mixes kinds, such as a dashboard with a written summary, takes
each resource for its part. On every surface, question these reflexes and
keep one only when the brand or the content calls for it: cream or beige
page backgrounds, side-stripe borders, gradient text, purple gradients, and
glassmorphism. Several together mean the design drifted from the brief.

## Visual Decisions

Open the resource for the decision in front of you:

- `resources/color.md`: contrast, neutrals, light or dark, colour strategy
  for a new identity.
- `resources/typography.md`: type scale, pairing, line length, wrapping.
- `resources/layout.md`: spacing, cards, z-index, dropdowns that escape
  clipping.
- `resources/motion.md`: easing, reduced motion, reveal transitions.

## Words on Screen

Ask of every hint, subtitle, and helper text what question it answers that
the control or heading doesn't, and delete it when the answer is none. Text
that explains how the screen works means the layout is wrong: name the
outcome on the control, rewrite the title, or fix the layout. A subtitle says
something about the data (the finding, the period, the scope), never about
the interface. Keep text the screen can't show: a required format, a
consequence, how to recover. Cut taglines and intros that repeat the title.

Use the audience's own words in labels, navigation, and empty states
("Waiting on the customer", "Due on the 28th"), not a template's nouns
("Items", "Records", "Status"). Buttons name their action ("Save changes",
not "OK"), and links make sense out of context ("View pricing", not "Click
here").

Where people read values, add a label last: let the value's format or
position say what it is ("$4,200", a date, an avatar), else fold the label
into the value ("12 left in stock", not "Stock: 12"), else add a quiet
label. Where people find things by their label (a settings page, a spec
table, a form), the label is what they scan for: keep it stable and visible.
Separate labels and metadata with spacing, not a decorative `•`.

Use standard controls and familiar icons for standard actions, and give
every icon-only button an accessible name and a tooltip. Few icons are
understood unlabelled in every context: add a visible label for primary
navigation, for actions costly to undo, and for icons specific to this
product. An icon alone suits a familiar action, settled by its context, on a
screen people use often.

Em dashes, aphoristic cadence, and marketing words ("streamline",
"empower", "seamless", "world-class") make copy read as generated; keep one
only when it says something precise.

## Check What Renders

Run the page checks in `resources/checks.md` on the rendered page before you
show it or ship it.
