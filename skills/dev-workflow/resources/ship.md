# Ship

Opening the PR and cleaning up after the merge.

## Pushing and PRs

Run `/post-dev` before opening the PR.

When a feature branch (never `main`) is complete and passes the full gate, push
it and open or update its PR without asking. Pass the PR body draft from
`/pre-dev` (`pr-body-<slug>.md`) as `--body-file` — the `gh` CLI's template
prompting doesn't apply once `--body-file` is passed, so that draft, filled
in as the work proceeded, is the source for the body. Fill in whatever it's
still missing before creating, and if the repo ships a body checker such as
`tools/ci/check-pr-body.mjs`, run it on the draft first. Follow the project's release
conventions for labels.

If `pr-body-<slug>.md` doesn't exist (pre-dev was skipped, or the work directory
is gone), fall back to `.github/PULL_REQUEST_TEMPLATE.md` (or similar)
directly, fill it from the current diff and conversation, and note in your
report that before-state evidence was not captured.

## Branch Cleanup

Clean up everything a branch's work claimed the moment it merges anywhere —
into its parent integration branch, staging, or main: the worktree and
branch, but also any scoped databases, dev processes, ports, or other
resources it held. Find the project's cleanup tooling (package scripts,
`tools/`, `AGENTS.md`) and use it immediately, branch by branch, rather than
batching cleanup for later.

Waiting is risky, not just untidy: many integration strategies collapse
history. A side-lane branch merged into an integration branch that is later
squash-merged leaves no provable trace of ever having merged — not a
matching PR, not ancestry. What would have been a one-line command becomes
manual, evidence-by-hand archaeology once that happens.

When the cleanup tool can't verify eligibility this way, check for a manual
verification guide near the tool (or write one) instead of guessing or
skipping cleanup.
