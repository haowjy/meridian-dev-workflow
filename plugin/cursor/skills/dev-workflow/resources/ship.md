# Ship

Opening the PR and cleaning up after the merge.

## Pushing and PRs

When a feature branch (never `main`) is complete and passes the full gate, push
it and open or update its PR without asking. Pass the PR body draft from
`/meridian-dev-workflow:pre-dev` (`pr-body-<slug>.md`) as `--body-file` — the `gh` CLI's template
prompting doesn't apply once `--body-file` is passed, so that draft, filled
in as the work proceeded, is the source for the body. Fill in whatever it's
still missing before creating, and if the repo ships a body checker such as
`tools/ci/check-pr-body.mjs`, run it on the draft first. Follow the project's release
conventions for labels.

## Branch Cleanup

Clean up everything a branch's work claimed the moment it merges anywhere —
into its parent integration branch, staging, or main: the worktree and
branch, but also any scoped databases, dev processes, ports, or other
resources it held. Find the project's cleanup tooling (package scripts,
`tools/`, `AGENTS.md`) and use it immediately, branch by branch, rather than
batching cleanup for later.

A squash merge further up can erase every trace that a branch merged, and
cleanup after that is guesswork.
