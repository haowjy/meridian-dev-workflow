---
name: dev-principles
type: principle
description: >
  Load when implementing, reviewing, refactoring, or designing. Core
  engineering values — simplicity, separation of concerns, structural
  judgment. The operating lens for all code decisions.
model-invocable: false
---

# Simplicity

The default failure mode is over-engineering, not under-engineering. Every
boundary, type, and layer is a cost.

Before adding structure, ask: is this actually a separate concern, or one
thing wearing two names? If these pieces always change together, they are
one thing. Partitioning does not make code simpler — independence does.

Justify the split, not the merge.

# Separation of Concerns

Group by concern. Draw boundaries where things actually change
independently.

When you see duplication across boundaries: are the boundaries wrong? Is
this really two modules, or one module that got split for the wrong reason?
Step back and rethink the structure — don't patch it with extraction.

# Make Changes Easy

Refactoring is disentangling. The question is: what would you need to
understand to make the next change here? Reduce that.

Refactor early while context is fresh. A refactor that grows the codebase
is suspect — are you disentangling, or adding ceremony?

# Abstraction Judgment

Before extracting: is this real shared behavior, or surface similarity?
Two cases look alike by coincidence. Three reveal the pattern.

When an abstraction grows flags and branches: did it capture the wrong
concept? Inline and re-form rather than patch.

# Deletion

Dead code is entanglement surface. LLMs default to preserving.

Before deleting: what constraint is this carrying? Before preserving: is
there actually a constraint, or just inertia?

# Consistency

Read surrounding code first. Does the project already solve this? Prefer
its patterns over introducing new ones. A good dependency deletes more code
than it adds.
