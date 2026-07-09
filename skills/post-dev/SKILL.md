---
name: post-dev
type: checkpoint
description: "Ship readiness: PR template, changelog, release label, cleanup. Run when implementation is done."
model-invocable: true
---

# Post-Dev Checkpoint

Run this when implementation is complete, before creating the PR.

## Checks

### PR readiness
- Read `.github/PULL_REQUEST_TEMPLATE.md` or similar template: fill every section
- Set a `release:*` label (default: `release:patch`)
- PR title under 70 characters, descriptive

### Changelog
- `CHANGELOG.md` has entries under `## [Unreleased]` for this work
- Entries written in caveman style: terse, behavioral, filler-free
- Focus on what downstream users notice, not which lines moved

### Review
- Has structural review passed? If not, spawn a reviewer first.
- Any review findings addressed or explicitly accepted?
- If the plan shifted during implementation, `DIVERGENCE/` in the work
  directory reflects it — reviewers and knowledge capture read from it

### Cleanup
- No stale files, dead code, or debug artifacts left behind
- Scaffolding tests deleted: tests written to understand behavior that no
  longer protect a live risk (see `/testing`)
- No TODO comments added without corresponding issue

### After merge
- Prune merged worktrees (project script if one exists, else `git worktree remove`)
- Verify CI passed on main
