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

Finish the task and commit it. Then have the system reviewed and probed as
it stands, with the lanes the change needs, each briefed with what the
change touched and where to look. Put each reviewer on a model family other
than every model that wrote the change (yours and any worker's):

- `@reviewer` for correctness, regressions, and behavior, on every change.
- `@reviewer` with `/thermo-nuclear-review` when the change adds or
  restructures code. Code drifts from `/dev-principles` even when its
  writer loaded them; a reviewer focused there catches what a general pass
  skims.
- One more `@reviewer` for each risk the change carries:
  `/test-architecture` for test changes, `/review-alignment` against a
  design or requirements, `/react-architecture` for React, the efficiency
  lane named in the brief for hot paths.
- `@prober` when the change alters what the running system does.

Confirm the running stack was built from your latest commit. They run
together while you prepare `/post-dev`; tell each to use its own test data
(accounts, records, fixtures, browser session) and not to reset or restart
shared services. Run them one after the other when they would share state
you can't separate. Fix their findings. When the fixes restructured code or
changed behavior, commit and rerun the lanes whose verdicts the fixes could
change; check smaller fixes yourself.

## Verify

List the ways the change could fail and load `/probe` to exercise each on
the real system. As you go, run the existing tests that cover what you
changed. Keep no new test the user didn't ask for, and delete tests you wrote to
check your work. Run the full
suite once, before the review commit. Checks catch breakage; passing unit
tests never show the change works.

When the code behind one responsibility would need a third round of fixes,
however many files it spans and whatever the symptom, step back and find
the shared cause. Two places owning one invariant is the
usual one; a wrong algorithm or a misread requirement are others. Stuck on
what the user wanted? Stop and say what's missing.

## Code Discipline

Add defensive checks, guard clauses, or try/catch only for a failure you've
hit or the logic can reach; speculative handling is dead code. Let existing
error handling propagate unwrapped.

## Ship

Use `/dev-workflow` for commits and the PR, and `/post-dev` before the PR.

Report: what changed, how you verified it, review findings, PR link.
