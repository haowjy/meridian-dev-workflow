# Ship

Opening the PR and cleaning up after the merge.

## Pushing and PRs

When a feature branch (never `main`) is complete, passes the full gate and
`/post-dev` is done, push it and open its PR, or mark it ready if it is a
draft, without asking. Pass the PR body draft from `/pre-dev`
(`pr-body-<slug>.md`) as `--body-file`. If the repo ships a body checker such
as `tools/ci/check-pr-body.mjs`, run it on the body first. Follow the
project's conventions for when PRs open and how they are labelled.

## Branch Cleanup

Clean up everything a branch's work claimed the moment it merges anywhere —
into its parent integration branch, staging, or main: the worktree and
branch, but also any scoped databases, dev processes, ports, or other
resources it held. Find the project's cleanup tooling (package scripts,
`tools/`, `AGENTS.md`) and use it immediately, branch by branch, rather than
batching cleanup for later.

A squash merge further up can erase every trace that a branch merged, and
cleanup after that is guesswork. Delete a branch only with evidence it
merged: `git branch -d` is blind to squash merges, and `-D` discards
unmerged commits.

After the merge, check that CI passed on the target branch, and close the
work item once every agent you started for it has finished.
