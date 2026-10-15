---
name: post-dev
type: checkpoint
description: "Run when implementation is done, before opening the PR: catches what would otherwise ship missing (PR body, changelog, review sign-off, deferred work, knowledge capture, cleanup)."
model-invocable: true
---

# Post-Dev Checkpoint

Run this when implementation is complete, before creating the PR. The After
merge section applies once the PR lands.

## Checks

### PR readiness
- `pr-body-<slug>.md` (from `/pre-dev`) has every template section filled,
  including the before-state evidence captured at kickoff — top up whatever
  implementation added
- Set a `release:*` label (default: `release:patch`)
- PR title under 70 characters, descriptive

### Changelog
- `CHANGELOG.md` has entries under `## [Unreleased]` for this work
- Entries written in caveman style: terse, behavioral, filler-free
- Focus on what downstream users notice, not which lines moved

### Review
- The review passed on the commit it named, and each finding is fixed or explicitly accepted. Changes after that commit are small fixes you read yourself, doc updates, or scaffolding-test deletions; anything that restructured code or changed behavior got its own review.
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
- Spawn `@kb-lead` once, after review fixes have landed, covering the whole
  change.
- Pass the conversation, changed files, and work directory. Point it at the
  decision file and any `DIVERGENCE/` logs first; they are the cheapest
  record of what was decided and why.
- Colocated guidance needs an update only when it — or the absence of needed
  guidance — would cause a cold agent to make a wrong decision. A changed path
  or missing `.context/` file is not itself a gap.
- Before this checkpoint passes, verify any colocated doc updates
  (`.context/`, `AGENTS.md`) are present on the feature branch. Separate KB
  repository updates may land independently.

### Cleanup
- No stale files, dead code, or debug artifacts left behind
- Scaffolding tests deleted: tests written to understand behavior that no
  longer protect a live risk (see `/testing`)

### After merge
- Verify CI passed on main
- Clean up what the work left behind: worktree, branch, scoped databases, dev
  processes and routes, work item. These are linked, so deleting one by hand
  orphans the rest — find the project's cleanup tooling (package scripts,
  `tools/`, AGENTS.md) and follow its policy on what gets removed and how.
  Branch deletion needs merge evidence git can't supply alone: `-d` is blind to
  squash merges, `-D` discards unmerged commits.
- Mark the work item done: `meridian work done <slug>` (see `/work-artifacts`) —
  archives the work dir; confirm attached spawns are terminal first
