---
name: feature-worktree
description: >
  Load when starting a work item that will produce a PR. Covers creating
  a feature worktree, working in it, and shipping via PR to main.
model-invocable: true
---

# Feature Worktree

All non-trivial work happens in a feature worktree, not on main.

## Setup

```bash
git worktree add ../<repo>.worktrees/feature-name -b feature/feature-name
```

Branch naming: `feature/<work-item-slug>` or `fix/<work-item-slug>`.
Worktree path: `../<repo>.worktrees/<slug>`.

## Ship

```bash
git push -u origin feature/feature-name
gh pr create --base main --title "..." --body "..."
```

## Cleanup

After the PR merges:

```bash
git worktree remove ../<repo>.worktrees/feature-name
git branch -d feature/feature-name
```
