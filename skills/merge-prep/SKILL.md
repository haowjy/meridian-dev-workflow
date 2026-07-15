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
rejected alternatives, the constraints that shaped the design. Don't undo
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

**Ask the human.** When the written sources don't give you enough to
resolve a conflict confidently, ask. Name what you're uncertain about. A
wrong guess during merge is harder to find than a wrong guess during
implementation.
