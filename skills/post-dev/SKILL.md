---
name: post-dev
type: checkpoint
description: "Ship readiness: PR template, changelog, review, deferred-work routing, knowledge capture, cleanup. Run when implementation is done."
model-invocable: true
---

# Post-Dev Checkpoint

Run this when implementation is complete, before creating the PR. The After
merge section applies once the PR lands.

## Checks

### PR readiness
- Read `.github/PULL_REQUEST_TEMPLATE.md` or similar template: fill every section
- Set a `release:*` label (default: `release:patch`)
- PR title under 70 characters, descriptive

### Changelog
- `CHANGELOG.md` has entries under `## [Unreleased]` for this work
- Entries written in caveman style: terse, behavioral, filler-free
- Focus on what downstream users notice, not which lines moved

### Review
- Has structural review passed? If not, spawn a reviewer first.
- Any review findings addressed or explicitly accepted?
- If the plan shifted during implementation, `DIVERGENCE/` in the work
  directory reflects it — reviewers and knowledge capture read from it

### Deferred work
- Mine conversation history, touched files, and review findings for anything
  deferred: TODOs, skipped improvements, known limitations, future ideas
- Record each deferral in the nearest `.context/TODO` (must-do) or
  `.context/FUTURE` (nice-to-have) to the code it affects — each entry
  names the affected path and concrete follow-up
- Cross-cutting items or items needing external visibility: file a
  GitHub issue (see `/issues`)
- Every `TODO` comment added or touched in this work must have a matching
  entry in `.context/TODO` or a GitHub issue — no orphan TODOs

### Knowledge capture
- A completed `@kb-lead` reconciliation covers the final changed source
  paths. If source changed after an earlier capture, run reconciliation again.
- Colocated guidance needs an update only when it — or the absence of needed
  guidance — would cause a cold agent to make a wrong decision. A changed path
  or missing `.context/` file is not itself a gap.
- Decisions, rejected alternatives, and design rationale go stale fast —
  capture them while context is live
- Pass the conversation, changed files, work directory, and any
  `DIVERGENCE/` logs as context
- Before this checkpoint passes, verify any colocated doc updates
  (`.context/`, `AGENTS.md`) are present on the feature branch. Separate KB
  repository updates may land independently.

### Cleanup
- No stale files, dead code, or debug artifacts left behind
- Scaffolding tests deleted: tests written to understand behavior that no
  longer protect a live risk (see `/testing`)

### After merge
- Verify CI passed on main
- Clean up worktree artifacts: remove merged worktrees, delete their
  local branches
- Complete or archive the work item per `/work-artifacts` and confirm attached
  spawns are terminal
