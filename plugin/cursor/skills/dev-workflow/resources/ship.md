# Ship

Opening the PR and cleaning up after the merge.

## Pushing and PRs

Push a feature branch (never `main`) and open its PR as a draft at its
first commit, without asking, so anyone can see the work's state from the
PR. Pass the PR body draft from `/meridian-dev-workflow:pre-dev` (`pr-body-<slug>.md`) as
`--body-file`, and update the body as the work changes. When the branch is
complete, passes the full gate and `/meridian-dev-workflow:post-dev` is done, mark the PR ready.
If the repo ships a body checker such as `tools/ci/check-pr-body.mjs`, run
it on the body first. Follow the project's release conventions for labels.

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
