---
name: dev-workflow
type: reference
description: "Commit discipline during implementation: commit after each passing step, changelog at commit time."
model-invocable: true
---

# Dev Workflow

Commit discipline during implementation.

## Commit Discipline

Commit after each step that passes checks. Don't accumulate changes across multiple steps.

1. Implement the change
2. Verify (lint, type-check, tests)
3. Commit with a descriptive message
4. Move to next step

Keep `CHANGELOG.md` current under `## [Unreleased]`: write entries at commit time, not retroactively.

## Deferrals

When you skip something during implementation — a cleanup, an edge case, a
better approach — route it immediately through `/issues`. Don't rely on
catching it at post-dev.

## Pushing and PRs

When a feature branch (never `main`) is complete and passes the full gate, push
it and open or update its PR without asking. Pass the PR body draft from
`/pre-dev` (`pr-body-<slug>.md`) as `--body-file` — the `gh` CLI's template
prompting doesn't apply once `--body-file` is passed, so that draft, filled
in as the work proceeded, is the source for the body. Fill in whatever it's
still missing before creating, and if the repo ships a body checker such as
`tools/ci/check-pr-body.mjs`, run it on the draft first. Set a `release:*`
label.

If `pr-body-<slug>.md` doesn't exist (pre-dev was skipped, or the work dir
was cleared), fall back to `.github/PULL_REQUEST_TEMPLATE.md` (or similar)
directly, fill it from the current diff and conversation, and note in your
report that before-state evidence was not captured.

## Do Not

- Do not merge directly into `main` or `staging`; normal feature-branch merges are allowed
- Push directly to main for feature work (use PRs)
- Create or push `v*` tags manually (CI owns tagging)
- Use `--no-verify` on push without explicit user permission
- Delete untracked files without asking (may be someone else's work)
- Edit `__version__` or `Cargo.toml` version for stable releases (CI-owned)
