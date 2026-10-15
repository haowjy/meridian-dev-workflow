---
name: solo-dev
type: reference
description: "Working discipline for a primary that implements and verifies the change itself in one session: spawn limits, checkpoint review, runtime verification, ship."
model-invocable: false
---

# Solo Dev

Fix local problems you touch; report larger unrelated ones.

## Spawns

Do the task yourself.

Finish the task and commit it. Then spawn `@reviewer` and `@prober` on that
commit; both read a frozen commit, so they run together while you prepare
`/post-dev`. Fix their findings. When the fixes restructured code or changed
behavior, commit and run both again on the new commit; check smaller fixes
yourself.

## Verify

Check your work as you go: run the project's checks and load `/probe` to
exercise the real system. Checks catch breakage; passing unit tests never
show the change works.

A second finding of the same failure class in the same code means two
places own one invariant: stop patching and change the approach. Stuck on
what the user wanted? Stop and say what's missing.

## Code Discipline

Don't add defensive checks, guard clauses, or try/catch unless you've hit
the failure or the logic can actually reach it. Speculative handling is
dead code. Don't re-wrap existing error handling.

## Ship

Use `/dev-workflow` for commit discipline and `/post-dev` for PR readiness.

Report: what changed, how you verified it, review findings, PR link.
