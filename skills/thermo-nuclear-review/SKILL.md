---
name: thermo-nuclear-review
description: "Use for extremely strict maintainability review: find the code-judo move that makes a change or a design, and the system around it, dramatically simpler. Blocks structural regressions."
model-invocable: true
metadata:
  type: reference
---

# Thermo-Nuclear Review

Find the code-judo move: a restructuring that keeps behavior the same and
makes the code dramatically smaller and more direct. Cleaner lines are not
the goal. A review that only confirms the code works has failed this lane.

Hold the code to `/dev-principles`; this lane enforces them strictly.

## Scope: the System, Focused Where the Brief Points

Review the system as it stands, starting from the focus your brief names.
Read whole concerns: the modules in focus, their siblings, and the
paths that call into them. Start with giant files and the files that churn
most; churn concentrated in one place usually means a missing abstraction.

## Find the Shape

1. List the edge cases, special cases, modes, and flags the code handles.
2. Find the structure under which groups of them become one rule or disappear: a
   different ownership boundary, a state model, one write path, a shared
   base. Assume such a move usually exists and push for it.
3. Check the documented architecture (`AGENTS.md`, `.context/`) against the
   code. Where a claim such as "a new storage backend is one class plus
   registration" no longer holds, the gap is a finding.
4. Look across siblings for parallel copy-pasted structure (per-provider
   classes, per-store IO, per-command handlers) that one shared owner
   should hold.

Prefer deleting a layer, field, parameter, or branch over rearranging it. A
refactor that moves complexity without reducing the concepts a reader must
hold is not a fix.

## Reviewing a Design or Plan

Review it against the code it will land in. For each mechanism it adds (a
mode, a flag, a retry, a lock, a second writer of some state), ask first what
the system loses without it; an unneeded mechanism is the largest deletion
available. Then look for an enabling refactor in the existing code that
shrinks the design, and a structure that folds the design's special cases
into what the system already has. A new path beside one it should replace is
a finding. The file-size, dead-code, type-escape, and test-count blockers
wait for the code.

## Presumptive Blockers

Block unless the author justifies it:

- A simpler structure would delete a group of edge cases, and the change keeps
  them.
- The change pushes a file from under 1,000 lines to over.
- Ad-hoc conditionals, one-off flags, or nullable modes bolted into an
  existing flow, or feature checks scattered across shared code.
- Logic in the wrong layer, feature logic leaking into a shared path, or a
  bespoke helper where a canonical one exists.
- Dead code: a function, branch, flag, config key, or module that nothing
  reaches or whose result nothing uses, including what recent work left
  without a caller. Search for references to what it touched and removed.
- Shallow modules, wrappers, pass-through helpers, or generic "magic" that
  add indirection without clarity.
- Casts, `any`/`unknown`, needless optionality, or silent fallbacks hiding an
  unclear invariant.
- Related updates that can leave state half-applied.
- Test cases that multiply without covering new risk. Load
  `/test-architecture` when tests are in scope.

## Report

Lead with the shape: the simpler structure you propose, the edge cases it
deletes, and what survives unchanged. Then blockers, then lesser structural
findings. A few high-conviction findings beat a long list; skip renames and
cosmetics when the problem is structural.

End with a verdict on the structure, not the behavior: approve, or request
changes naming the simplification.
