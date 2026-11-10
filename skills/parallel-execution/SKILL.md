---
name: parallel-execution
description: Load when work splits into lanes that can run in parallel or phases that build on each other. DAG planning, worktrees, merging, gates.
model-invocable: true
metadata:
  type: reference
---

# Parallel Execution

## Plan the DAG

Decompose work into a dependency graph before spawning:

1. List every task with its inputs and outputs.
2. Draw dependencies: B depends on A if B needs A's output.
3. Mark merge points where parallel branches must converge.
4. Mark verify points: per-branch focused checks on what the branch touched (in-worktree, parallel); at each merge, build the combined result.
5. Mark gates: a phase gate where later phases build on the phase's output, and the final gate on the last phase (see Gates).

Test each dependency: "could this start from the spec alone, or does it need actual code from the other branch?" If it needs actual code, it's sequential. Give each change to shared code one owner: land it first as an enabling step, or assign it to one lane and have the others build against its contract. Two lanes independently changing the same shared behavior merge cleanly and still break together; plan that out or run them in order.

Run a wide mechanical change (a rename or signature change across many callers) as expand, migrate, contract: land the new form beside the old as the enabling step, migrate callers in batches as parallel lanes, and delete the old form as the last phase of the same change.

Write the DAG into the work directory and execute from it.

Update the written DAG when the shape changes: review findings, failed merges, and unexpected complexity revise the plan.

## Execute with Worktrees

Each parallel branch gets its own worktree and dev stack; sequential phases run on the current worktree. Set them up per `resources/worktrees.md`, which also covers lanes that run long.

## Merge and Verify

At each convergence point:

1. Verify each branch in its own worktree (parallel).
2. Merge branches back: hand the whole convergence to one `@coder`, briefed
   per `/dev-workflow`'s merge hand-off, and have it merge the branches one
   after another.
If the coder reports a failed integration check, isolate which branch interaction caused it before re-spawning.

## Gates

A gate runs once a phase's branches merge, and the next phase starts only once it passes. A problem found at a phase gate costs one phase of rework; found at the end, every later phase is built on it. A phase nothing later builds on gains nothing from its own gate: the final gate covers it.

**Phase gate**: the suite, and your own read of the merged code: what the phase changed, and whether the next phase can build on it. Review lanes and the prober wait for the final gate, so the feature is reviewed once (`/agent-staffing` `resources/reviewers.md`).

**Final gate**, on the last phase: the full suite, then the feature's one review round from `reviewers.md`, on everything the change touched since the original base. Its findings are fixed inside that round, not as new phases: a new phase would earn its own final gate and repeat the review.
