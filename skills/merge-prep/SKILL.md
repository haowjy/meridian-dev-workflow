---
name: merge-prep
type: checkpoint
description: "Load before merging or rebasing a branch. Build comprehension of what each side intended so conflict resolution serves the work, not the text."
model-invocable: true
---

# Merge Prep

Understand what you're integrating before you run any merge or rebase
command. Every conflict resolution is a judgment call about intent. You
cannot make it without knowing what each side was trying to do and why.

## Read for Intent

**Read the PR, and follow the links.** PRs reference session IDs, work
items, or discussion threads. Read those too. The PR body summarizes what
the branch does. The linked conversations carry why: the reasoning, the
rejected alternatives, the constraints that shaped the design. Preserve
choices the author deliberately made.

**Read the commits.** When there's no PR, the commit log is the primary
source. Either way, read the full series from the branch point, not just
the latest. Early commits establish direction. Later ones refine or
course-correct.

**Read the target.** What landed since the branch diverged? Look for
in-progress patterns: refactors, renames, convention changes. These often
merge cleanly with no conflict, but the branch's new code uses the old
pattern. A clean merge that introduces inconsistency is a bug. Continue
the target's patterns into the branch's new code.

**Escalate what the sources don't settle.** When the written sources
don't give you enough to resolve a conflict confidently, stop on that
conflict and name what you're uncertain about: to the human in a session,
in your report when spawned. A wrong guess during merge is harder to find
than a wrong guess during implementation.

## Check the Result

A clean textual merge proves nothing about the combined code. Build the
result and run the focused checks where the two sides meet before you call
the merge done.
