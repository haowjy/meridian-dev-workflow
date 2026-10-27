# Detection

Use these signals to recognize structural problems from a diff plus nearby
context. A smell label is only useful if you can tie it to a concrete
maintenance cost.

## Diff-Level Signals

- One feature or bug fix touches many files for one concept.
- The same branch or special case is added in multiple places.
- A new parameter, flag, or mode is threaded through an existing abstraction.
- A supposedly generic helper gains caller-specific behavior.
- Compatibility logic is added to ordinary paths instead of an isolated
  boundary.
- A rename feels necessary but the codebase has no single name for the concept.

## Module-Level Signals

- Large functions where setup, policy, transformation, and IO are mixed.
- Large classes or modules that change for unrelated reasons.
- Methods that mostly read or manipulate another object's data.
- Callers traversing several layers of getters or helper wrappers.
- The same fields passed around together through several functions.
- Strange pass-through abstractions that add almost no value.

## Deletion and Legacy Signals

- Code appears unused, but nobody can say why it exists.
- Deprecated paths have no comment, exit condition, or replacement.
- Compatibility branches are everywhere instead of inside one boundary.
- Intentional duplication exists but the relationship is not marked.

## False Positives

Avoid over-reporting:

- Large modules are not automatically bad if the responsibilities are tightly
  cohesive.
- Duplication is not automatically bad if the cases are meaningfully different
  and keeping them separate improves clarity.
- A compatibility path is not automatically debt if it is already isolated,
  named, and has a clear removal condition.
- A small wrapper may be load-bearing if it enforces an important boundary such
  as tracing, authorization, retries, or protocol normalization.
