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

Finish the task and commit it. Then spawn `@reviewer` and `@prober` on that
commit, with the reviewer on a model family other than yours. They run together on the same dev stack while you prepare
`/post-dev`; tell each to use its own test data (accounts, records,
fixtures) and not to reset or restart shared services. Fix their findings. When the fixes restructured code or changed
behavior, commit and run both again on the new commit; check smaller fixes
yourself.

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

Don't add defensive checks, guard clauses, or try/catch unless you've hit
the failure or the logic can actually reach it. Speculative handling is
dead code. Don't re-wrap existing error handling.

## Ship

Use `/dev-workflow` for commits and the PR, and `/post-dev` before the PR.

Report: what changed, how you verified it, review findings, PR link.
