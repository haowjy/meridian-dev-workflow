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
defer only what needs a product decision or is a project of its own.

Search the open issues before filing; add what you found to a matching one
instead of opening a duplicate. Give an issue the labels in
`resources/labels.md`, plus `work:<slug>` when a work item is active. If
`gh` is unavailable, say that filing was skipped and keep the draft in the
work directory.

## What an Issue Shows

Whoever picks the issue up comes to it weeks later in a fresh session. Show
them the problem; a description of it makes them rebuild your session to
see it. Leave out what won't outlast your session, such as spawn and chat
IDs and local paths.

Draft the body from a template:

- The repo's issue template (`.github/ISSUE_TEMPLATE/`), when it has one.
- Otherwise its PR template: fill every section that can be written before
  the fix (the problem and why it matters, the walkthrough and screenshots
  of how it behaves now, the before timings, the risks known so far) and
  leave out the sections only the fix can fill. The PR that fixes it then
  starts from those sections.
- With neither, `resources/issue-template.md`.

Under a project's template, also cover the sections of
`resources/issue-template.md` it lacks.
