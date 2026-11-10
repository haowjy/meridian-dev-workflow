---
name: thermo-nuclear-review
description: "Use for extremely strict maintainability review: find the code-judo move that makes a change or a design, and the system around it, dramatically simpler. Blocks structural regressions."
model-invocable: true
metadata:
  type: reference
---

# Thermo-Nuclear Review

Find the code-judo move: a restructuring that keeps behavior the same and
makes the code dramatically smaller and more direct. Hold the code to
`/dev-principles`, strictly.

Review the system as it stands, starting from the focus your brief names:
the modules in focus, their siblings, and the paths that call into them; churn concentrated in one file usually means
a missing abstraction. List the special cases, modes and flags the code handles, then look for the
structure under which groups of them become one rule or disappear: a
different ownership boundary, a state model, one write path, one owner for
copy-pasted siblings. Assume such a move usually exists. Prefer deleting a
layer, field, parameter or branch over rearranging it; a refactor that moves
complexity without reducing what a reader must hold is not a fix. Where
`AGENTS.md` or `.context/` describes the architecture, check that the code
still matches; a claim that no longer holds is a finding.

For a design or plan, ask of each mechanism it adds (a mode, a flag, a
retry, a lock, a second writer) what the system loses without it: an
unneeded mechanism is the largest deletion available. Look for an enabling
refactor in the existing code that shrinks the design. A new path beside one it should replace is a finding. The blockers below
wait for the code.

## Blockers

Block unless the author justifies it:

- the change keeps a group of edge cases a simpler structure would delete;
- ad-hoc conditionals, one-off flags or nullable modes bolted into an
  existing flow;
- logic in the wrong layer, or a bespoke helper where a canonical one exists;
- dead code, including what the change left without a caller;
- casts, needless optionality or silent fallbacks hiding an unclear
  invariant;
- related updates that can leave state half-applied;
- test cases that multiply without covering new risk.

Load `/test-architecture` when tests are in scope.

## Report

Lead with the shape: the simpler structure, the edge cases it deletes, and
what survives unchanged. Then blockers, then lesser findings; a few
high-conviction findings beat a long list. End with a verdict on the
structure: approve, or request changes naming the simplification.
