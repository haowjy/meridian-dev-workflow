# Worktrees for Parallel Lanes

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state.

Worktrees are siblings, not nested: creating one from any worktree makes a peer (the current checkout may itself be a worktree). Sequential phases run on the current worktree; parallel groups branch off into new worktrees. When you create a lane's worktree, build the generated artifacts its checks need there unless a build cache handles them; ignored build outputs don't carry across worktrees by default. Point each delegated lane's source checkout at its worktree, track which worktree serves which DAG branch, and remove worktrees after their branch is merged and verified. Use the worktree tool configured for the repo or machine.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
