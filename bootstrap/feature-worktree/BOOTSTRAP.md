# Feature Worktree Setup

Agents need permission to read and write inside worktree directories,
which live outside the main repo at `../<repo>.worktrees/`.

Add the worktree path to your project-level harness permissions. For
Claude Code, add to `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(git worktree *)",
      "Edit:../<repo>.worktrees/**",
      "Read:../<repo>.worktrees/**",
      "Write:../<repo>.worktrees/**"
    ]
  }
}
```

Replace `<repo>` with your actual repo directory name.

The tech-lead also needs `Bash(git worktree *)` to create and remove
worktrees. This is already included above.
