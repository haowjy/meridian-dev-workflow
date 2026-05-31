---
name: source-context
description: Build richer decision context by studying real source code — clone open source repos, spawn explorers, synthesize findings.
type: reference
model-invocable: true
---

# Source Context

Docs and blog posts describe intent. Source code reveals what actually
happens — edge cases, error paths, boundary decisions, real API shapes.
Don't plan from thin air. Before forming requirements, sizing scope, or
designing architecture, build richer context by studying the source of
projects that solve similar problems.

## When

- You're scoping a feature and need to understand how others solved it
- You're choosing between architectural approaches and want evidence
- You're integrating with a library and its docs are incomplete
- You're designing an API and want to study real-world contracts

## Method

### Find Candidates

Start from what you already know — projects that solve similar problems,
competing libraries, reference implementations. `@web-researcher` can
surface additional candidates. Prefer projects with a track record:
active maintenance, real users, non-trivial scope.

### Clone

```bash
mkdir -p ~/.meridian/ref
git clone --depth 1 <url> ~/.meridian/ref/<name>
```

Shallow clone is enough for investigation. Repos persist across sessions
— you only clone once.

### Investigate

Spawn `@explorer` agents with targeted questions, not open-ended "tell me
about this codebase." Each spawn gets one focus area:

- "How does <project> handle auth across its API surface? Trace the
  middleware chain and report the pattern."
- "What are the module boundaries in <project>? Map the top-level
  directory structure and how they import each other."
- "How does <project> structure its error types? Find the error hierarchy
  and how errors propagate to callers."
- "What's the data model for <concept> in <project>? Trace the types from
  storage through to API response."

Fan out in parallel — 3-5 explorers covering different angles.

### Synthesize

Spawn one explorer to merge the individual reports into a synthesis:

- Patterns that appear across projects (convergent design)
- Tradeoffs different projects made (divergent design)
- Surprises — things you wouldn't have thought of from docs alone
- Concrete implications for your own work

Write the synthesis into the work directory as a reference artifact.

## Keep Repos

Don't delete after investigation. `~/.meridian/ref/` accumulates over time.
A repo studied once may be relevant again. Disk is cheap; re-cloning wastes
time.
