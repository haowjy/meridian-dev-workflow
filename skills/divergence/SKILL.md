---
name: divergence
description: "Load when the design or plan may shift during multi-phase work: a logged shift lets reviewers tell planned change from drift."
model-invocable: true
metadata:
  type: reference
---

# Divergence Tracking

Maintain a `DIVERGENCE/` folder in the work directory. Add an entry when the
design or plan shifts — not every small implementation detail, but the
decisions that change what the work is building or how.

## What to capture

Each entry: what the plan said, what changed, why. One paragraph is enough.

## When to write

- A coder reports a conflict that changes the approach
- A redesign cycle settles on a different direction
- A constraint discovered during implementation narrows or widens scope
- A reviewer's frame-rot verdict triggers a rethink

## What not to write

Implementation-level choices that stay within the plan's intent (seam
selection, commit granularity, test tier). Those belong in commit messages
and coder reports, not the divergence log.
