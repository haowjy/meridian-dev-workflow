---
name: dev-principles
type: principle
description: "Load when implementing, reviewing, refactoring, or designing code: the engineering values every code decision is judged against."
model-invocable: true
---

# Dev Principles

Judge each code decision by what it does to the next change.

- **Simplicity of the system, not of the change.** The smaller diff today
  accretes parallel mechanisms, ghost states, and compatibility layers.
  Refactor and delete to reduce concepts, states, and moving parts, even
  when the diff is larger.
- **Consistency beats cleverness.** Read the surrounding code first and use
  the project's patterns; a new idiom must be worth what every later reader
  pays to learn it. A good dependency deletes more code than it adds.
- **Boundaries where things change independently.** Things that always
  change together are one thing; partitioning alone doesn't justify a
  split. Prefer deep modules: an exported function that wraps three lines
  belongs in its caller. When duplication crosses a boundary, suspect the
  boundary before extracting a helper. Keep files focused: an agent reads
  the whole file.

## Simplicity

Over-engineering is the default failure: moving parts that buy no real
independence. Before adding a branch, flag, or mode for a new case, look
for the model under which the case needs no special handling: a different
owner, state model, or shared path.

## Deletion

LLMs default to preserving code; fight that. Delete dead code, stale
imports, and orphaned files in the same change, and collapse obvious
duplication. When new code replaces old
behavior, delete the old path instead of keeping it as a fallback or
compatibility layer, unless the project's policy requires one. Fix the
structural problems you touch: circular dependencies, god modules, leaky
abstractions.

## Defensive Code

Validate at trust boundaries: user input, network, subprocess output, files
another process or an older build wrote. Inside a boundary, trust the types
and let errors propagate; a broad catch that falls back to a default turns a
bug into a wrong answer. Guard only against failures you've hit or the logic
can reach; any other guard is dead code. Re-checking data nothing has touched
since the last check catches nothing: verify a copy once, before deleting its
source.

## Efficiency by Construction

Large efficiency bugs are rarely slow lines. They are a cost paid on every
event, or one that grows with accumulated state. On a hot path (per chunk,
per turn, per poll, per invocation), keep each run's cost proportional to
the work in front of it: write only what changed, poll with a cheap check,
and load only what this run uses. Before you report or act on a performance
comparison, rule out errors, skipped work, and noise, per `/probe`'s
`resources/measurement.md`.

## Comments

Comment what the code can't show: a hidden constraint, a surprising
invariant, an external quirk, a race it avoids. Design rationale goes in
the directory's `.context/`; the story of a change goes in its commit
message.

## Testing

Verify by listing how the change could fail and checking each failure on
the running program, plus the existing tests that cover what you touched.
Keep no new test the user didn't ask for (`/testing`); propose one you
think would earn a permanent place to whoever you report to.
