---
name: solo-dev
alwaysApply: false
metadata:
  type: reference
---

# Solo Dev

Fix local problems you touch; report larger unrelated ones.

## Spawns

Do the task yourself. Plan it, then run `/meridian-dev-workflow:pre-dev` before your first source edit.

Finish the task and commit it. Before staffing a review, load
`/meridian-dev-workflow:agent-staffing`, open its `resources/reviewers.md`, and staff the lanes
the change needs. Prepare `/meridian-dev-workflow:post-dev` while the lanes run, then fix their findings;
`reviewers.md` says which lanes rerun after a fix.

## Verify

Exercise each way the change could fail on the real system (`/meridian-dev-workflow:probe`).
Run the full suite once, before the review commit; passing unit tests
never show the change works.

When a concern (the code behind one responsibility) would need a third
round of fixes or a second redesign, or a fourth review round, open
`/meridian-dev-workflow:agent-staffing` `resources/reviewers.md` and follow its limits. Stuck on what the
user wanted? Stop and say what's missing.

## Ship

Use `/meridian-dev-workflow:dev-workflow` for commits and the PR, and `/meridian-dev-workflow:post-dev` before the PR.

Report: what changed, how you verified it, review findings, PR link.
