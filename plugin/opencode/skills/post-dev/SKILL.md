---
name: post-dev
description: 'Run when implementation is done, before opening the PR: catches what would otherwise ship missing (PR body, changelog, review sign-off, deferred work, knowledge capture, cleanup).'
metadata:
  type: checkpoint
---

# Post-Dev Checkpoint

Run this when implementation is complete, before creating the PR. The After
merge section applies once the PR lands.

## Checks

### PR readiness
- `pr-body-<slug>.md` (from `/meridian-dev-workflow:pre-dev`) has every template section filled,
  including the before-state evidence captured at kickoff — top up whatever
  implementation added
- Evidence images link to the commit that last touched them, taken after
  the file is pushed (`git log -1 --format=%H -- <file>` in the repo that
  holds it), not to `main`: finished work is moved and later pruned, which
  breaks every `main` link into it
- The PR follows the project's release conventions, wherever its AGENTS.md or
  docs keep them: its labels and title rules
- `@cold-reader` has read the PR body, commissioned per `/meridian-dev-workflow:llm-writing`
  `resources/cold-read.md` with the PR's reviewer as its reader, and its
  valid findings are fixed

### Changelog
- The changelog is updated the way the project's conventions say
- Entries written in caveman style: terse, behavioral, filler-free
- Focus on what downstream users notice, not which lines moved

### Review
- The review passed on the commit it named, and each finding is fixed or explicitly accepted. Changes after that commit are small fixes you read yourself, doc updates, or scaffolding-test deletions; anything that restructured code or changed behavior got its own review.
- If the plan shifted during implementation, `DIVERGENCE/` in the work
  directory reflects it — reviewers and knowledge capture read from it

### Deferred work
- Mine conversation history, touched files, and review findings for anything
  deferred: TODOs, skipped improvements, known limitations, future ideas
- Record each deferral per `/meridian-dev-workflow:issues`
- Every `TODO` comment added or touched in this work must have a matching
  entry in `.context/TODO` or a GitHub issue — no orphan TODOs

### Knowledge capture
- Spawn `@kb-lead` after review fixes have landed, covering the whole
  change and anything an earlier capture left out.
- Brief it as its description asks, and pass any `DIVERGENCE/` logs with
  the decision records.
- Colocated guidance (`.context/`, `AGENTS.md`) passes `/meridian-dev-workflow:qi-maintenance`'s
  gap test.
- Before this checkpoint passes, verify any colocated doc updates
  (`.context/`, `AGENTS.md`) are present on the feature branch. Separate KB
  repository updates may land independently.

### Cleanup
- No stale files, dead code, or debug artifacts left behind
- Dev stacks, browsers, scratch worktrees, and temp dirs that you or your
  spawns started are stopped and deleted; restart a stack when a fix cycle
  needs it. Keep one running only when the human asked to use it.
- New tests the user didn't ask for are deleted (`/meridian-dev-workflow:testing`)

### After merge
- Verify CI passed on main
- Clean up what the work left behind (worktree, branch, scoped databases,
  dev processes and routes) per `/meridian-dev-workflow:dev-workflow` `resources/ship.md`; branch
  deletion needs merge evidence git can't supply alone: `-d` is blind to
  squash merges, `-D` discards unmerged commits.
- Close and archive the work item; confirm its delegated agents are terminal
  first
