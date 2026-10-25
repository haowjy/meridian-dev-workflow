---
name: parallel-execution
type: reference
description: Load when work splits into lanes that can run in parallel or phases that build on each other. DAG planning, worktrees, merging, gates.
model-invocable: true
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

## Adapt the Plan

The DAG is a living document. Add phases, split subphases, insert verification gates, or restructure agent teams as you learn more during execution. Review findings, failed merges, and unexpected complexity are signals to revise the plan. Update the written DAG when the shape changes.

Before another review-fix cycle at a gate, check the limits in `/agent-staffing` `resources/reviewers.md`.

## Execute with Worktrees

Each parallel branch gets its own worktree and dev stack (server, database, etc.). No shared mutable state.

Git worktrees are siblings, not nested: `git worktree add` from any worktree creates a peer. The current worktree may itself be a worktree. Sequential phases run on the current worktree; parallel groups branch off into new worktrees. When you create a lane's worktree, build the generated artifacts its checks need there; ignored build outputs don't carry across worktrees. Point each delegated lane's source checkout at its worktree. Track which worktree serves which DAG branch. Remove worktrees after their branch is merged and verified.

## Merge and Verify

At each convergence point:

1. Verify each branch in its own worktree (parallel).
2. Merge branches back: hand the whole convergence to one `@coder` with
   `/merge-prep` attached, merging the branches one after another.
If the coder reports a failed integration check, isolate which branch interaction caused it before re-spawning.

## Gates

A gate runs once a phase's branches merge, and the next phase starts only once it passes. A problem found at a phase gate costs one phase of rework; found at the end, every later phase is built on it. A phase nothing later builds on gains nothing from its own gate: the final gate covers it.

Before staffing a gate, open `/agent-staffing` `resources/reviewers.md` and staff the lanes the gate's work needs.

**Phase gate**: lanes focused on what the phase changed and the code around it.

**Final gate**, on the last phase: lanes focused on everything the change touched since the original base, the `@prober` running the user-facing workflows end to end when the change alters them, and the full suite, once.

Gaps the final gate finds become new phases in the DAG.

Fix blocking findings before the gate passes; `reviewers.md` says which lanes rerun after a fix.

## Long-Running Lanes

For mining and multi-file audit lanes, have the spawn write partial
findings to disk as it works, so truncation or credit exhaustion cannot
zero the work.
