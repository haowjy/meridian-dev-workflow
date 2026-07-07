---
name: post-dev
type: checkpoint
description: "Ship readiness: PR template, changelog, release label, cleanup. Run when implementation is done."
model-invocable: true
---

# Post-Dev Checkpoint

Run this when implementation is complete, before creating the PR.

## Checks

### Base sync
- Has the base branch moved since you branched? (`git log --oneline --first-parent
  $(git merge-base origin/<base> HEAD)..origin/<base>`)
- If yes, or the PR reports CONFLICTING: run `/branch-sync` before anything else —
  intent-aware merge of the base, semantic-conflict sweep, full gate on the result.

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

### Cleanup
- No stale files, dead code, or debug artifacts left behind
- No TODO comments added without corresponding issue

### After merge
- Prune merged worktrees (use the project's prune script; dry-run first)
- Verify CI passed on main
