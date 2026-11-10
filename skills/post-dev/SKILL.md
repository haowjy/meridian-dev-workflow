---
name: post-dev
description: "Run when implementation is done, before opening the PR: catches what would otherwise ship missing (PR body, changelog, review sign-off, deferred work, knowledge capture, cleanup)."
model-invocable: true
metadata:
  type: checkpoint
---

# Post-Dev Checkpoint

Run this when implementation is done, before opening the PR. The last item
applies once the PR merges.

- **PR body.** `pr-body-<slug>.md` from `/pre-dev` has every template section
  filled, with the before-state evidence and what the work added. Evidence
  images link to the commit that last touched them, taken after the push
  (`git log -1 --format=%H -- <file>`), not to a branch, where the file can
  later move. The PR follows the project's label and title rules. A
  `@cold-reader` has read the body, with the PR's reviewer as its reader,
  and the `docs/`, `AGENTS.md` and `.context/` prose the branch added or
  rewrote: one reader for all of them (`/llm-writing`
  `resources/cold-read.md`). Its valid findings are fixed.
- **User docs** describe the change: every page that names what it touched.
- **Changelog** updated the way the project says: what downstream users
  notice, in terse caveman style.
- **Review.** The review passed on the commit it named, and each finding is
  fixed or accepted. Later changes are small fixes you read yourself, doc
  updates, deleted scaffolding tests, or fixes that went through the
  re-review in `/agent-staffing` `resources/reviewers.md`. A plan that
  shifted shows in `DIVERGENCE/`.
- **Deferred work** from the conversation, the touched files and the review
  findings is recorded per `/issues`, and every `TODO` comment added or
  touched has an entry.
- **Knowledge.** `@kb-lead` is spawned after the review fixes land, briefed
  as its description asks, with any `DIVERGENCE/` logs. Colocated
  `AGENTS.md` and `.context/` updates pass `/qi-maintenance`'s gap test and
  are on the branch.
- **Cleanup.** No dead code, debug artifacts or stale files. Tests are
  kept or deleted as `/testing` Which Tests Stay says. Dev stacks, browsers, scratch
  worktrees and temp dirs you or your spawns started are stopped and
  removed, unless the human asked to keep one.
- **After merge.** CI passed on main. The branch's worktree, branch,
  databases and processes are cleaned up per `/dev-workflow`
  `resources/ship.md`; deleting the branch needs merge evidence, since `-d`
  is blind to squash merges and `-D` discards unmerged commits. The work item
  is closed once every agent you started for it has finished.
