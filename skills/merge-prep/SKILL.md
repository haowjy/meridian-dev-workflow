---
name: merge-prep
description: "Load before merging or rebasing a branch. Build comprehension of what each side intended so conflict resolution serves the work, not the text."
model-invocable: true
metadata:
  type: checkpoint
---

# Merge Prep

Every conflict resolution is a judgment about intent, so learn what each
side meant before you run a merge or rebase. Read the PR and what it links
to (sessions, work items, threads), or, with no PR, the whole commit series
from the branch point. Read what landed on the target since the branch
diverged: a rename or convention change there often merges cleanly while the
branch's new code still uses the old pattern, so carry the target's patterns
into it.

When the sources don't settle a conflict, stop on it and name what you're
unsure of: to the human in a session, in your report when spawned. A clean
textual merge proves nothing about the combined code: build the result and
run the focused checks where the two sides meet.
