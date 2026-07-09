---
name: divergence
type: reference
description: Track plan divergence during multi-phase work. Load when redesign or plan shifts are likely.
model-invocable: true
---

# Divergence Tracking

Maintain a `DIVERGENCE/` folder in the work directory. Add an entry when the
design or plan shifts — not every small implementation detail, but the
decisions that change what the work is building or how.

## What to capture

One file per entry, prefixed by date or phase so the folder reads
chronologically. Each entry: what the plan said, what changed, why. One
paragraph is enough.

## When to write

- A coder reports a conflict that changes the approach
- A redesign cycle settles on a different direction
- A constraint discovered during implementation narrows or widens scope
- A reviewer's frame-rot verdict triggers a rethink

## What not to write

Implementation-level choices that stay within the plan's intent (seam
selection, commit granularity, test tier). Those belong in commit messages
and coder reports, not the divergence log.

## Downstream

Reviewers check `DIVERGENCE/` for alignment between the plan and the code.
`@kb-lead` uses it as source material after the phase settles — the
divergences are often the most durable lessons.
