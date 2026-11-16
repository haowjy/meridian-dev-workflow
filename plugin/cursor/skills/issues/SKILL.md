---
name: issues
description: 'Load when you defer work or file a GitHub issue: where each item lands (a colocated .context/ file or an issue), and what an issue shows so someone without your session can act on it.'
metadata:
  type: reference
alwaysApply: false
---

# Issue Tracking

Deferred work goes where `/meridian-dev-workflow:knowledge-layers` places it: a directory's own
items in its `.context/TODO` or `FUTURE`, cross-cutting ones and those that
need outside visibility in a GitHub issue. Fix what you find first, and
defer only what waits on the human's decision (`/meridian-dev-workflow:explore-and-engage`) or is
a project of its own.

Search the open issues before filing; add what you found to a matching one
instead of opening a duplicate. Give an issue the labels in
`resources/labels.md`, plus `work:<slug>` when a work item is active. If
`gh` is unavailable, say that filing was skipped and keep the draft in the
work directory.

## Writing an Issue

Whoever picks the issue up comes to it weeks later in a fresh session, so
show the problem rather than describe it. Draft the body from the repo's
issue template (`.github/ISSUE_TEMPLATE/`). Without one, use the sections of
its PR template that can be written before the fix (the problem, how it
behaves now, before timings), so the fixing PR starts from them. Without
either, use `resources/issue-template.md`. Delete a section only when it
can't apply.

`gh` can't attach images: commit each to a repo (the project's assets
folder, or the work directory's repo) and link it at that commit, since a
branch link breaks when the file moves. Leave out spawn and chat IDs and
local paths, which mean nothing outside your session.
