---
name: issues
description: 'Load when you defer work, so each item lands where it will be found: a colocated .context/ file or a GitHub issue.'
metadata:
  type: reference
alwaysApply: false
---

# Issue Tracking

Deferred work goes where `/meridian-dev-workflow:knowledge-layers` places it: a directory's own
items in its `.context/TODO` or `FUTURE`, cross-cutting ones and those that
need outside visibility in a GitHub issue. Fix what you find first, and
defer only what needs a product decision or is a project of its own.

An issue says where it was found, what it is, and what should be done. Give
it the labels in `resources/gh-commands.md`, plus `work:<slug>` when a work
item is active. If `gh` is unavailable, say that filing was skipped and keep
the draft in the work directory.
