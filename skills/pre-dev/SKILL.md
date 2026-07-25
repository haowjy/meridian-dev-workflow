---
name: pre-dev
type: checkpoint
description: "Pre-implementation readiness: worktree, branch, workspace state. Run before handing off to implementation."
model-invocable: true
---

# Pre-Dev Checkpoint

Run this before handing off to an implementation agent. Verify the workspace
is ready for code changes.

## Checks

### Worktree isolation
Should this work be on a worktree? Prefer worktrees for:
- Any feature branch work
- Risky or experimental changes  
- Parallel work alongside other agents
- Changes spanning multiple files or subsystems

If not already in a worktree, create one:
```bash
git -C <repo> worktree add ../<repo>.worktrees/<slug> -b <branch>
meridian work task-dir ../<repo>.worktrees/<slug>
```

### Branch readiness
- Feature branch exists and is tracking remote
- Branch is up to date with main (or rebased)
- No stale worktrees from prior work on this branch

### Workspace state
- Working tree is clean (no uncommitted changes from other work)
- If other agents' uncommitted work is present, stop and report: do not
  proceed over someone else's changes

### Cross-repo awareness
- Does this work span multiple repos? If so, set up task-dirs for each.
- Are there dependency ordering constraints?

### PR body draft
Pre-fill the PR body when the worktree is created, so the work targets the
PR from the start:

```bash
cp <repo>/.github/PULL_REQUEST_TEMPLATE.md \
   "$MERIDIAN_ACTIVE_WORK_DIR/pr-body-<slug>.md"
```

The draft is the acceptance frame for the implementation handoff: sections
fill in as the work proceeds (Resulting Behavior as slices land,
Verification as gates run), and `gh pr create --body-file` takes it at the
end — GitHub's template auto-fill does not apply to `--body-file`, so this
draft is the only path by which the template reaches an agent-created PR.

Part of the template's evidence only exists right now: before/after means
the before-state must be captured (or its capture delegated) while it still
runs — screenshots of the current rendering for user-facing work, current
outputs, failure text, timings — and dropped into the draft. Once the
change lands, "before" costs a stack swap and a reconstructed fixture to
recover.

## After checks pass

Report readiness. The handoff can proceed.
