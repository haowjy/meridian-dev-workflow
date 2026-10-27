# Worktrees for Parallel Lanes

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state.

Git worktrees are siblings, not nested: `git worktree add` from any worktree creates a peer. The current worktree may itself be a worktree. Sequential phases run on the current worktree; parallel groups branch off into new worktrees. When you create a lane's worktree, build the generated artifacts its checks need there; ignored build outputs don't carry across worktrees. Point each delegated lane's source checkout at its worktree. Track which worktree serves which DAG branch. Remove worktrees after their branch is merged and verified.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
