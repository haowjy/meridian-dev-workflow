# Ship

Opening the PR and cleaning up after the merge.

## Pushing and PRs

When a feature branch (never `main`) is complete, passes the full gate and
`/meridian-dev-workflow:post-dev` is done, push it and open its PR, or mark it ready if it is a
draft, without asking. Pass the PR body draft from `/meridian-dev-workflow:pre-dev`
(`pr-body-<slug>.md`) as `--body-file`. If the repo ships a body checker such
as `tools/ci/check-pr-body.mjs`, run it on the body first. Follow the
project's conventions for when PRs open and how they are labelled.

Screenshots and videos go up with the PR, never into a commit. Reference
each in the draft by its path relative to the draft
(`![Before: the empty state](shots/before.png)`) and pass the file with
`--attach` on `gh pr create` or `gh pr edit`: `gh` uploads it and rewrites
the reference to the upload. When an upload fails, `gh` still opens or
updates the PR and exits non-zero; attach the missing file again with
`gh pr edit --attach`. Uploads can't be deleted, and on a public repo anyone
with the link can open them.

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
