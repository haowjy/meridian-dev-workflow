# Agent Impact

Structural debt hurts agents differently than it hurts humans reading code
slowly and carefully.

## Why Structure Matters More With Agents

Agents work best when the next edit is narrow and the relevant concept is easy
to locate. Bad structure breaks that in a few recurring ways:

- **Wide edit surface.** One small change requires coordinated edits in many
  files, which raises the chance that the agent misses a site or updates them
  inconsistently.
- **Weak locality.** A concept's policy, data shape, and compatibility logic
  live in different places, so the agent has to reconstruct intent from many
  modules before touching anything.
- **Low greppability.** Dynamic indirection, vague names, and hidden branching
  make it hard to find the real implementation site.
- **Misleading abstraction.** The obvious place to edit is not the real place,
  because the current abstraction no longer matches the true variation.
- **Legacy sprawl.** Compatibility and deprecated paths are mixed into ordinary
  code, so the agent cannot tell what is normal behavior and what is temporary
  baggage.

## What Good Structure Buys

Good structure narrows the likely edit set and makes the right boundary obvious.
That improves:

- speed of orientation
- confidence that the agent found every impacted site
- odds that the change stays behavior-preserving
- ability to add tests at the correct seam
- future review quality, because the underlying concept is visible

When judging structural issues, ask how they affect agent discoverability,
change fan-out, and regression risk, not just whether a human might eventually
untangle them.
