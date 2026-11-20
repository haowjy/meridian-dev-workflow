# Worktrees with worktrunk (`wt`)

Use when `wt` is installed and configured for the repo or machine. Worktrees are addressed by branch name and placed according to `worktree-path` in `~/.config/worktrunk/config.toml` (or the repo config).

```bash
wt switch -c <branch>     # create a worktree for a new branch
wt list                   # list worktrees and status for the current repo
wt remove <branch|path>   # remove one worktree and its branch
wt step prune --dry-run   # preview merged, clean worktrees and stale local branches
wt step prune             # remove them (catches squash merges; skips dirty worktrees)
```

- `wt` operates per repo — run `wt list` and `wt step prune` from the target repo root (or pass `-C <repo>`).
- Only use `wt step copy-ignored` on copy-on-write filesystems (APFS, btrfs, XFS). On ext4 it falls back to a full copy and duplicates build outputs.
- Never remove a worktree with uncommitted or unmerged work without asking.
