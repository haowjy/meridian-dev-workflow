---
name: pre-dev
description: Run before the first source edit of a change, yours or a spawned implementer's. It is the only point where before-state evidence still exists.
metadata:
  type: checkpoint
---

# Pre-Dev Checkpoint

Run this before implementation starts, while the before-state still exists.

- **Checkout.** Put feature work in a worktree of its own unless the
  project's `AGENTS.md` says otherwise, and make it the task's default
  checkout for delegated agents; a worktree from another task is not this
  one's. Build there the generated artifacts the
  project's checks need, so the first check doesn't fail on a missing build.
  If another agent's uncommitted work is in the way, stop and report it.
- **PR body draft.** When the work ends in a PR, copy the repo's PR template
  to `pr-body-<slug>.md` in the work directory now, or start it blank if the
  repo has none. An agent opens its PR with `--body-file`, which skips the
  template, so this draft is the only way the template reaches the PR.
- **Before-state evidence.** Capture into the draft what the change will
  alter: screenshots of the current rendering, current output, failure text,
  timings. Delegate to a browser or probe agent what you can't take yourself. Once the change lands, recovering "before" costs a stack swap and
  a rebuilt fixture.
- **Several repos.** Set up a checkout for each, and note the order they
  must land in.
