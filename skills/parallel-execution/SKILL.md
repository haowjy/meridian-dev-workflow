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
4. Mark verify points: per-branch focused checks on what the branch touched (in-worktree, parallel); at each merge, build the combined result.
5. Mark gates: a phase gate at the end of every phase, and the final gate on the last one (see Gates). Gate phases, never subphases or single branches.

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
3. Integration check on the combined result: build it and run focused checks on where the branches meet.
You own the merge. If integration fails, isolate which branch interaction caused it before re-spawning.

## Gates

A gate runs on a phase's final commit, after its branches merge, and the next phase starts only once it passes. A problem found at a phase gate costs one phase of rework; found at the end, every later phase is built on it. Spawn the gate's lanes together, each reviewer on a model family other than every model that wrote what it reviews. Confirm the stack the prober runs was built from that commit, and tell each lane to use its own test data and not to reset or restart shared services.

**Phase gate**, at the end of every phase, sequential or merged:
- `@reviewer` across everything the phase changed: correctness, regressions, behavior.
- `@reviewer` with `/thermo-nuclear-review`, focused on structure. Code drifts from `/dev-principles` even when its writer loaded them; a reviewer focused there catches what a general pass skims.
- `@prober` exercising what the phase built on the real system.

**Final gate**, on the last phase, covers the whole change against the original base and fans out wider:
- The three phase-gate lanes, on the whole change.
- One more `@reviewer` for each risk the change carries: `/test-architecture` for test changes, `/review-alignment` against the design or requirements, `/react-architecture` for React, the efficiency lane named in the brief for hot paths.
- The `@prober` runs the user-facing workflows end to end, not only what the last phase built.
- The full suite, once.

Final-gate reviewers must use a model family free of every phase's implementers and your own integration edits; when no one family is, split the review by surface. Gaps the final gate finds become new phases in the DAG.

Fix blocking findings before the gate passes. When the fixes restructured code or changed behavior, run the whole gate again on the new commit; check smaller fixes yourself.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
