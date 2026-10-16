---
name: solo-dev
type: reference
description: "Load when you implement and verify a change yourself in one session: when to spawn review and probe, how to verify, when to stop patching, how to ship."
model-invocable: false
---

# Solo Dev

Fix local problems you touch; report larger unrelated ones.

## Spawns

Do the task yourself. Run `/pre-dev` before your first source edit.

Finish the task and commit it. Then spawn these on that commit, each
reviewer on a model family other than every model that wrote the change
(yours and any worker's):

- `@reviewer` for correctness, regressions, and behavior.
- `@reviewer` with `/thermo-nuclear-review`, on structure alone. Code drifts
  from `/dev-principles` even when its writer loaded them; a reviewer with
  no other job catches what a general pass skims.
- One more `@reviewer` for each risk the change carries:
  `/test-architecture` for test changes, `/review-alignment` against a
  design or requirements, `/react-architecture` for React, the efficiency
  lane named in the brief for hot paths.
- `@prober` to exercise the real system.

Confirm the running stack was built from that commit. They run together on
it while you prepare `/post-dev`; tell each to use its own test data
(accounts, records, fixtures, browser session) and not to reset or restart
shared services. Run them one after the other when they would share state
you can't separate. Fix their findings. When the fixes restructured code or
changed behavior, commit and run them all again on the new commit; check
smaller fixes yourself.

## Verify

Check your work as you go with checks focused on what you changed, and
load `/probe` to exercise the real system. Run the full suite once, before
the review commit. Checks catch breakage; passing unit tests never
show the change works.

A second finding of the same failure class in the same code: stop patching
and find the shared cause. Two places owning one invariant is the usual
one; a wrong algorithm or a misread requirement are others. Stuck on
what the user wanted? Stop and say what's missing.

## Code Discipline

Add defensive checks, guard clauses, or try/catch only for a failure you've
hit or the logic can reach; speculative handling is dead code. Let existing
error handling propagate unwrapped.

## Ship

Use `/dev-workflow` for commits and the PR, and `/post-dev` before the PR.

Report: what changed, how you verified it, review findings, PR link.
