---
name: thermo-nuclear-review
type: reference
description: "Use for extremely strict structural review: find the simpler shape of a change and the system around it, and block structural regressions."
model-invocable: true
---

# Thermo-Nuclear Review

Find the simpler shape, not cleaner lines. Behavior stays the same; the
structure should get dramatically smaller and more direct. A review that only
confirms the code works has failed this lane.

## Scope: the Change and the System It Lives In

Read whole cohesive seams, not only changed lines: the modules the change
touches, their siblings, and the paths that call into them. Start with giant
files and the files that churn most; churn concentrated in one place usually
means a missing abstraction.

## Find the Shape

1. List the edge cases, special cases, modes, and flags the code handles.
2. Find the model under which groups of them become one rule or disappear: a
   different ownership boundary, a state model, one write path, a shared
   base. Assume such a move usually exists and push for it.
3. Check the documented architecture (`AGENTS.md`, `.context/`) against the
   code. Where a claim such as "a new harness is one adapter plus
   registration" no longer holds, the gap is a finding.
4. Look across siblings for parallel copy-pasted structure (per-harness
   classes, per-store IO, per-command handlers) that one shared owner
   should hold.

Prefer deleting a layer, field, parameter, or branch over rearranging it. A
refactor that moves complexity without reducing the concepts a reader must
hold is not a fix.

## Presumptive Blockers

Block unless the author justifies it:

- A simpler model would delete a group of edge cases, and the change keeps
  them.
- The change pushes a file from under 1,000 lines to over.
- Ad-hoc conditionals, one-off flags, or nullable modes bolted into an
  existing flow, or feature checks scattered across shared code.
- Logic in the wrong layer, feature logic leaking into a shared path, or a
  bespoke helper where a canonical one exists.
- Wrappers, pass-through helpers, or generic "magic" that add indirection
  without clarity.
- Casts, `any`/`unknown`, needless optionality, or silent fallbacks hiding an
  unclear invariant.
- Related updates that can leave state half-applied.
- Test cases that multiply without covering new risk. Load
  `/test-architecture` when tests are in scope.

## Report

Lead with the shape: the simpler model you propose, the edge cases it
deletes, and what survives unchanged. Then blockers, then lesser structural
findings. A few high-conviction findings beat a long list; skip renames and
cosmetics when the problem is structural.

Be direct. When the change makes the codebase messier or misses a
dramatic simplification, say so plainly.

End with a verdict on the structure, not the behavior: approve, or request
changes naming the simplification.
