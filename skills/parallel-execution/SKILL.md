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
3. Independent tasks are parallel candidates.
4. Mark merge points where parallel branches must converge.
5. Mark verify points: per-branch (in-worktree, parallel) and post-merge (integration check).

Sequential means it genuinely needs the prior step's output. Everything else is a parallelism opportunity. Test: "could this start from the spec alone, or does it need actual code from the other branch?"

Write the DAG into the work directory. The plan is the artifact you execute from.

## Adapt the Plan

The DAG is a living document. Add phases, split subphases, insert verification gates, or restructure agent teams as you learn more during execution. Findings from convergence gates, failed merges, or unexpected complexity are all signals to revise the plan. Update the written DAG when the shape changes.

## Execute with Worktrees

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state, no edit-lane coordination needed.

Git worktrees are siblings, not nested: `git worktree add` from any worktree creates a peer. The current worktree may itself be a worktree. Sequential phases run on the current worktree; parallel groups branch off into new worktrees.

## Merge and Verify

At each convergence point:

1. Verify each branch in its own worktree (parallel).
2. Merge branches back.
3. Integration check on the combined result: build, test, verify the branches compose correctly.

The orchestrator owns the merge. If integration fails, isolate which branch interaction caused it before re-spawning.

## Execution Pipeline

Load `resources/execution-model.md` for the phase/subphase pipeline: rolling implementation with lookahead, convergence gates, fix-cycle routing, and final gate.
