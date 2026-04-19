# Overview

This reference library distills refactoring guidance into three operational
questions:

1. What kind of structural problem is present?
2. Why does it make future changes slower or riskier?
3. What small behavior-preserving move should improve it?

The smell families are organized by review utility:

- `smells/bloaters.md` for oversized functions, classes, and responsibility
  mass
- `smells/change-preventers.md` for patterns that broaden the next change
- `smells/couplers.md` for bad locality, message passing, and intimacy between
  modules
- `smells/dispensables.md` for dead, obsolete, speculative, or low-value
  structure
- `smells/oo-abusers.md` for patterns where inheritance, conditionals, or
  generalization are being used in the wrong shape

The move families are organized by the kind of fix they usually imply:

- `moves/composing-methods.md` for splitting long routines into clearer steps
- `moves/moving-features.md` for relocating behavior to the concept it serves
- `moves/organizing-data.md` for replacing loose primitives and clumps with
  better data boundaries
- `moves/simplifying-conditionals.md` for untangling repeated or overloaded
  branching
- `moves/dealing-with-generalization.md` for inlining, splitting, or reshaping
  abstractions that froze the wrong axis of variation

Use `detection.md` to recognize smells from diffs and nearby context, and
`review-translation.md` to turn what you see into an actionable finding.
