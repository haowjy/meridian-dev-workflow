---
name: pre-dev
description: 'Run before implementation starts: before your first source edit, or before handing off to an implementation agent. It is the only point where before-state evidence still exists.'
metadata:
  type: checkpoint
alwaysApply: false
---

# Pre-Dev Checkpoint

Run this before implementation starts, yours or a handoff's. Verify the
workspace is ready for code changes.

## Checks

### Worktree isolation
Should this work be on a worktree? Prefer worktrees for:
- Any feature branch work
- Risky or experimental changes  
- Parallel work alongside other agents
- Changes spanning multiple files or subsystems

If already in a worktree, confirm it is this task's: a worktree from another
task is not this one's. If this work belongs on a
worktree and you aren't in one, create one:
```bash
git -C <repo> worktree add ../<repo>.worktrees/<slug> -b <branch>
```

Make the worktree this task's default checkout: the one delegated agents work
in unless you assign them another.

Then build the generated artifacts the project's checks need in this
worktree, so the first check doesn't fail on a missing build.

### PR body draft
When the work will end in a PR, copy the repo's PR template to
`pr-body-<slug>.md` in the work directory now, before any code changes land,
if it doesn't already exist there — whether or not the worktree itself was
newly created this pass.

Use the nearest match if that exact path doesn't exist
(`.github/pull_request_template.md`, repo root, `docs/`); if the repo has no
template, start the draft blank instead of skipping the step.

This draft is the acceptance frame the implementation handoff targets —
sections fill in as work proceeds — and it's the only path by which the
template reaches an agent-created PR: the `gh` CLI's template prompting
doesn't apply once `--body-file` is passed, so nothing else populates the
body.

Capture before-state evidence into the draft now, while it still exists —
screenshots of the current rendering for user-facing work, current outputs,
failure text, timings. Delegate to a browser or probe agent if you can't
take it yourself: once the change lands, "before" costs a
stack swap and a reconstructed fixture to recover.

### Branch readiness
- Feature branch exists and is tracking remote
- Branch is up to date with main (or rebased)
- No stale worktrees from prior work on this branch

### Workspace state
- Working tree is clean (no uncommitted changes from other work)
- If other agents' uncommitted work is present, stop and report: do not
  proceed over someone else's changes

### Cross-repo awareness
- Does this work span multiple repos? If so, set up task-dirs for each.
- Are there dependency ordering constraints?

## After checks pass

Report readiness. The handoff can proceed.
