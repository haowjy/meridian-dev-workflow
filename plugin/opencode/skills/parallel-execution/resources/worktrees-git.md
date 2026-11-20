# Worktrees with `git worktree`

Use when no higher-level worktree tool is configured. Place linked worktrees as siblings of the repo (for example `../<repo>.worktrees/<branch>`) rather than inside it.

```bash
git worktree add ../<repo>.worktrees/<branch> -b <branch>   # create a new branch worktree
git worktree list                                           # list all worktrees for this repo
git worktree remove <path>                                  # remove a clean worktree
git worktree prune                                          # clear stale admin records
```

- Removing a worktree does not delete its branch. Delete the branch only with evidence it merged: `git branch -d` misses squash merges, and `-D` discards unmerged commits.
- Never pass `--force` to `git worktree remove` on a worktree with uncommitted or unmerged work without asking.
