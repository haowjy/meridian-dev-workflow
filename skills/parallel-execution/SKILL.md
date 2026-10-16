---
name: parallel-execution
type: reference
description: Load when decomposing work into phases that can run in parallel. DAG planning, worktree isolation, merge/verify.
model-invocable: true
---

# Parallel Execution

## Plan the DAG

Decompose work into a dependency graph before spawning:

1. List every task with its inputs and outputs.
2. Draw dependencies: B depends on A if B needs A's output.
3. Mark merge points where parallel branches must converge.
4. Mark verify points: per-branch focused checks on what the branch touched (in-worktree, parallel); at each merge, build and probe the combined result; the full suite once, on the final merged change.
5. Mark review points: one `@reviewer` pass at the end of each phase, on its final commit, never one per branch, on a model family other than every model that wrote what it reviews. For the last phase's whole-change review, that is every phase's implementers and your own integration edits; when no one family is free of all of them, split the review by surface. The last phase's review covers the whole change against the original base with at least two reviewers: a default `@reviewer`, and one with `/thermo-nuclear-review` on structure alone.

Test each dependency: "could this start from the spec alone, or does it need actual code from the other branch?" If it needs actual code, it's sequential. Give each change to shared code one owner: land it first as an enabling step, or assign it to one lane and have the others build against its contract. Two lanes independently changing the same shared behavior merge cleanly and still break together; plan that out or run them in order.

Run a wide mechanical change (a rename or signature change across many callers) as expand, migrate, contract: land the new form beside the old as the enabling step, migrate callers in batches as parallel lanes, and delete the old form as the last phase of the same change.

Write the DAG into the work directory and execute from it.

## Adapt the Plan

The DAG is a living document. Add phases, split subphases, insert verification gates, or restructure agent teams as you learn more during execution. Review findings, failed merges, and unexpected complexity are signals to revise the plan. Update the written DAG when the shape changes.

When review-fix cycles loop, findings keep expanding, or fixes introduce new issues, stop the loop: bring the problem back to the human, spawn design research for alternative approaches, or restructure the plan around the obstacle.

## Execute with Worktrees

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state.

Git worktrees are siblings, not nested: `git worktree add` from any worktree creates a peer. The current worktree may itself be a worktree. Sequential phases run on the current worktree; parallel groups branch off into new worktrees. When you create a lane's worktree, build the generated artifacts its checks need there; ignored build outputs don't carry across worktrees. Point each spawn at its worktree with `--task-dir <worktree-path>`. Track which worktree serves which DAG branch. Remove worktrees after their branch is merged and verified.

## Merge and Verify

At each convergence point:

1. Verify each branch in its own worktree (parallel).
2. Merge branches back.
3. Integration check on the combined result: build and probe the real system to confirm the branches compose.
You own the merge. If integration fails, isolate which branch interaction caused it before re-spawning.

End every phase, sequential or merged, with a `@reviewer` pass on its final commit. Fix blocking findings before the next phase builds on it. When fixes restructured code or changed behavior, run the integration check and the review again on the new commit; read smaller fixes yourself.

After the last phase, run the full suite once on the whole change. If it finds gaps, append new phases to the DAG.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
