---
name: post-dev
description: 'Run when implementation is done, before the PR is ready for review: catches what would otherwise ship missing (PR body, changelog, review sign-off, deferred work, knowledge capture, cleanup).'
metadata:
  type: checkpoint
alwaysApply: false
---

# Post-Dev Checkpoint

Run this when implementation is done, before the PR is ready for review.

- **PR body.** `pr-body-<slug>.md` from `/meridian-dev-workflow:pre-dev` has every template section
  filled, with the before-state evidence and what the work added. Evidence
  images link to the commit that last touched them, taken after the push
  (`git log -1 --format=%H -- <file>`), not to a branch, where the file can
  later move. The PR follows the project's label and title rules. A
  `cold-reader` has read the body, with the PR's reviewer as its reader,
  and the `docs/`, `AGENTS.md` and `.context/` prose the branch added or
  rewrote: one reader for all of them (`/meridian-dev-workflow:llm-writing`
  `resources/cold-read.md`). Its valid findings are fixed.
- **User docs** describe the change: every page that names what it touched.
- **Changelog**, where the project keeps one, updated per its conventions.
- **Review.** The review passed on the commit it named, and each finding is
  fixed or accepted. Later changes are small fixes you read yourself, doc
  updates, deleted scaffolding tests, or fixes that went through the
  re-review in `/meridian-dev-workflow:agent-staffing` `resources/reviewers.md`.
- **Deferred work** from the conversation, the touched files and the review
  findings is recorded per `/meridian-dev-workflow:issues`, and every `TODO` comment added or
  touched has an entry.
- **Knowledge.** `kb-lead` is spawned after the review fixes land, briefed
  as its description asks. Colocated
  `AGENTS.md` and `.context/` updates pass `/meridian-dev-workflow:qi-maintenance`'s gap test and
  are on the branch.
- **Cleanup.** No dead code, debug artifacts or stale files. Tests are
  kept or deleted as `/meridian-dev-workflow:testing` Which Tests Stay says. Dev stacks, browsers, scratch
  worktrees and temp dirs you or your spawns started are stopped and
  removed, unless the human asked to keep one.
