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

Finish the task and commit it. Before staffing a review, load
`/agent-staffing`, open its `resources/reviewers.md`, and staff the lanes
the change needs. Your own model counts among those that wrote the
change. Prepare `/post-dev` while the lanes run, then fix their findings. When the fixes restructured code or
changed behavior, commit and rerun the lanes whose verdicts the fixes could
change; check smaller fixes yourself.

## Verify

List the ways the change could fail and load `/probe` to exercise each on
the real system. As you go, run the existing tests that cover what you
changed. Keep no new test the user didn't ask for, and delete tests you wrote to
check your work. Run the full
suite once, before the review commit. Checks catch breakage; passing unit
tests never show the change works.

When a concern (the code behind one responsibility) would need a third
round of fixes or a second redesign, or a fourth review round, open
`/agent-staffing` `resources/reviewers.md` and follow its limits. Stuck on what the
user wanted? Stop and say what's missing.

## Code Discipline

Add defensive checks, guard clauses, or try/catch only for a failure you've
hit or the logic can reach; speculative handling is dead code. Let existing
error handling propagate unwrapped.

## Ship

Use `/dev-workflow` for commits and the PR, and `/post-dev` before the PR.

Report: what changed, how you verified it, review findings, PR link.
