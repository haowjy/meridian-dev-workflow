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
4. Mark verify points: per-branch (in-worktree, parallel) and post-merge (integration check).
5. Plan convergence gates at phase boundaries: spawn reviewers and probers, collect findings, fix, re-run affected checks, repeat until no blocking findings remain. Do not advance to the next phase until the gate passes.

Test each dependency: "could this start from the spec alone, or does it need actual code from the other branch?" If it needs actual code, it's sequential. Use your judgment on how much parallelism the work warrants.

Write the DAG into the work directory and execute from it.

## Adapt the Plan

The DAG is a living document. Add phases, split subphases, insert verification gates, or restructure agent teams as you learn more during execution. Findings from convergence gates, failed merges, or unexpected complexity are all signals to revise the plan. Update the written DAG when the shape changes.

If a convergence gate is not converging (review-fix cycles are looping, findings keep expanding, or fixes introduce new issues), you have authority to stop the loop and escalate: bring the problem back to the human, spawn design research to explore alternative approaches, or restructure the plan around the obstacle. Do not keep cycling a gate that is not making progress.

## Execute with Worktrees

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state.

Git worktrees are siblings, not nested: `git worktree add` from any worktree creates a peer. The current worktree may itself be a worktree. Sequential phases run on the current worktree; parallel groups branch off into new worktrees. Point each spawn at its worktree with `--task-dir <worktree-path>`. Track which worktree serves which DAG branch. Remove worktrees after their branch is merged and verified.

## Pipeline Review

Within sequential subphases, overlap review with the next coding step instead of blocking:

1. Subphase N completes on the working branch.
2. Create a review worktree from that commit.
3. Spawn reviewers and probers on the review worktree (`--task-dir`). They see a frozen snapshot; read-only, no edits.
4. Start subphase N+1 on the working branch immediately.
5. When review findings arrive, fold fixes into the current subphase or queue them for a fix pass.

Pipeline when review findings are typically additive: missing tests, edge cases, error handling. Wait when review might invalidate the next step's foundation: API shape, data model, core architecture. When uncertain, wait; rework costs more than idle time.

## Merge and Verify

At each convergence point:

1. Verify each branch in its own worktree (parallel).
2. Merge branches back.
3. Integration check on the combined result: build, test, verify the branches compose correctly.

You own the merge. If integration fails, isolate which branch interaction caused it before re-spawning.

After the last phase, run one final whole-change convergence gate. If it finds gaps, append new phases to the DAG.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
