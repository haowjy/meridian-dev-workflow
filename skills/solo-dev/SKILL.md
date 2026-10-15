---
name: solo-dev
type: reference
description: "Working discipline for a primary that implements and verifies the change itself in one session: spawn limits, checkpoint review, runtime verification, ship."
model-invocable: false
---

# Solo Dev

Fix local problems you touch; report larger unrelated ones.

## Spawns

Do the task yourself, without helpers, until you think it is done. Do not
split the work into parallel lanes; if it needs lanes, say it belongs to
`@tech-lead`.

When you think the task is done, commit, then spawn `@reviewer` and
`@prober` on that commit. Both read a frozen commit, so they can run
together while you prepare `/post-dev`. Fold in their findings. Re-review
only if a fix touched the path the review blocked on; re-probe only the
scenarios a fix touched.

## Verify

When you need to check something you implemented, or think you are done,
run the project's checks and load `/probe` to exercise the real system.
Checks catch breakage; passing unit tests never show the change works.

When a fix cycle isn't converging, or a second finding of the same failure
class hits the same code, stop patching and change the approach; that
usually means two places own one invariant. If the stall is that you don't
know what the user wanted, stop and say what's missing.

## Code Discipline

Don't add defensive checks, guard clauses, or try/catch unless you've hit
the failure or the logic can actually reach it. Speculative handling is
dead code. Don't re-wrap existing error handling.

## Ship

Source-code work runs in `$MERIDIAN_TASK_DIR` when set. Use `/dev-workflow`
for commit discipline and `/post-dev` for PR readiness.

Report: what changed, how you verified it, review findings if any, PR link.
