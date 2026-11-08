# Motion

This file holds what applies to any animation. Two kinds of work need more,
each in its own file:

- `resources/motion/directing.md`: animation that tells a story over time, such as a scroll
  film, an animated explainer, or a scene where characters or objects act.
  Beats, staging, continuity, and reviewing motion as a sequence.
- `resources/motion/cinematic-scroll.md`: a page that plays like a film as the visitor
  scrolls. The techniques, and how to build them so every scroll path works.

## Should It Move

Name what an animation is for before you build it: feedback that the
interface heard the person, showing where something came from or went,
making a state change legible, bridging a change that would otherwise jump,
explaining how something works, or delight. Motion that serves none of these
is decoration. Cut it on anything people use often. Match the amount of
motion to how often people see it: an action people repeat many times a day
(a command palette, a keyboard shortcut, moving through a list) gets little
or none beyond what shows a state or a position change, while a first-run or
once-a-visit moment can carry the most. Sections that fade and rise into
view one after another as the page scrolls are the generated default; one
orchestrated moment, such as a single entrance or one scene, lands better
than motion scattered over every section.

## Timing and Easing

Things that enter or answer the person ease out: they start fast and land
softly. Things that leave ease in and run shorter than the entrance. Things
that move from one place to another on screen ease in and out. Linear suits
constant motion and values tied directly to scroll or drag. Ease-in on an
entrance delays the moment the person is watching.

Keep interface motion short: most UI animations land within about 300ms,
and a popover that waits is slower than one that doesn't move at all. Story
and marketing moments earn more length because they are seen once. Longer
travel takes a little longer, and heavy things move slower than light ones.

Give the product one motion language and reuse it: a main curve, three
durations (quick, standard, slow), one way things enter. Use the project's
existing motion tokens where they exist rather than a parallel set.

## Shape of a Move

A move that reads as physical has four parts: anticipation (a small
gathering or wind-up against the main direction), the action, the reaction
of what it touches (a shadow, a neighbour, the surface it lands on), and a
settle. Short UI moves keep only the action and the settle; longer and
expressive ones use all four. Nothing appears from nothing: start an
entrance from slightly smaller, offset, or transparent, not from `scale(0)`,
and grow popovers and menus from the control that opened them.

Use springs for motion the person can grab, throw, or interrupt, since a
spring carries velocity through the change. Use transitions rather than
keyframes for anything triggered twice in quick succession: a transition
retargets from where it is, a keyframe restarts from zero. Exit the way you
entered.

## Several Things at Once

Give each moving element a role before choosing any timing. The lead is the
one thing the person must notice: it moves first and furthest. Support
follows with smaller motion. Decoration fades in place or stays still.
Everything else, including a container whose content animates, stays still.
Two leads mean a hierarchy problem that motion can't fix.

Move things together by default. Sequence them only when the order means
something: reading order, cause and effect, one thing arriving before
another. Animate a container's entrance or stagger its children, never both.
Equal delays move like a metronome: vary the step by importance, and keep a
stagger on product UI short enough that nobody waits for it. Nothing
on screen waits for an animation to finish before it can be used.

## Rendering

Animate `transform` and `opacity` (and `clip-path` or `filter` sparingly),
not layout properties. Give reduced-motion users a crossfade or an instant
change, with the content and meaning intact.

A reveal animation enhances content that is already visible: hidden tabs and
headless renderers never fire the trigger, so content that starts hidden
stays hidden.
