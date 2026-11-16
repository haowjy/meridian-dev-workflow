---
name: issues
description: 'Load when you defer work or file a GitHub issue: where each item lands (a colocated .context/ file or an issue), and what an issue shows so someone without your session can act on it.'
metadata:
  type: reference
---

# Issue Tracking

Deferred work goes where `/meridian-dev-workflow:knowledge-layers` places it: a directory's own
items in its `.context/TODO` or `FUTURE`, cross-cutting ones and those that
need outside visibility in a GitHub issue. Fix what you find first, and
defer only what needs a product decision or is a project of its own.

Search the open issues before filing; add what you found to a matching one
instead of opening a duplicate. Give an issue the labels in
`resources/labels.md`, plus `work:<slug>` when a work item is active. If
`gh` is unavailable, say that filing was skipped and keep the draft in the
work directory.

## What an Issue Shows

Whoever picks the issue up comes to it weeks later in a fresh session. Show
them the problem; a description of it makes them rebuild your session to
see it.

Lay the issue out by the repo's issue template (`.github/ISSUE_TEMPLATE/`).
Without one, use its PR template: fill every section that can be written
before the fix (the problem and why it matters, the walkthrough and
screenshots of how it behaves now, the before timings, the risks known so
far) and leave out the sections only the fix can fill. The PR that fixes it
then starts from those sections. With neither template, follow the order
below. Whatever the layout, the issue carries:

- **A bug:** steps that reproduce it from a clean start, what happened and
  what should have, and the commit or version it happened on. Paste error
  text and output verbatim. When you couldn't reproduce it, say what you
  saw and what you tried.
- **A gap or an improvement:** walk through one concrete case: what the
  user does, what they see, and where it goes wrong or costs them.
- **Anything visible** (a UI, a TUI, rendered output): a screenshot or a
  recording of it, with what to look at.
- **Who it hits and how often**, so whoever triages it can rank it.
- **Performance**, when the problem is slowness or its likely fix could
  cost speed or memory: the numbers, what they were measured on (data size,
  commit, machine load, runs), and the baseline they compare to
  (`/meridian-dev-workflow:probe` `resources/measurement.md`). A cost you expect but haven't
  measured is labeled as a guess.
- **Where to start:** the files and functions involved, and what you ruled
  out.
- **Done:** the check that will show it's fixed.

Leave out what won't outlast your session, such as spawn and chat IDs and
local paths. `gh` can't attach an image, so commit it to a repo (the
project's assets folder, or the work directory's repo) and link it at that
commit: a link to a branch breaks when the file moves or its work directory
is archived.
