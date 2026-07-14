---
name: issues
type: reference
description: "Route deferred work: colocated .context/ files for directory-scoped items, GitHub issues for cross-cutting or externally visible work."
---

# Issue Tracking

Route deferred work by scope. Directory-scoped deferrals go to colocated
`.context/TODO` or `.context/FUTURE`. Cross-cutting items or anything
requiring external visibility gets a GitHub issue.

GitHub Issues are a visibility layer on top of spawn reports and work-scoped
notes. If `gh` is unavailable, report that issue filing was skipped and log
the draft locally.

## When to File a GitHub Issue

All items below assume the item is cross-cutting or needs external
visibility; directory-scoped items go to `.context/TODO` or `.context/FUTURE`.

- Bug in adjacent code spanning multiple areas or needing triage
- Unexpected behavior that isn't broken enough to stop for but needs
  visibility beyond the local directory
- Backlog items that cross directory boundaries or need team coordination
- Deferred design decisions that need broader context or discussion
- Review findings marked non-blocking that affect multiple subsystems

Quick rule: fix it if < 5 minutes and you're in the area. Otherwise, route
by scope per the policy above.

## Mechanics

Check `gh` availability before creating:

```bash
gh auth status 2>/dev/null && gh repo view --json name 2>/dev/null
```

Use consistent labels so the team can filter by category. Tag every issue with
the discovering work item (`work:<slug>`) when an active work item exists.
Every issue body answers: where was this found, what is it, what should be
done.

See [`resources/gh-commands.md`](resources/gh-commands.md) for the label
taxonomy, issue body template, and `gh` CLI commands.
