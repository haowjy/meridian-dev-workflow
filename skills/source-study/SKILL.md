---
name: source-study
description: Load when you need evidence from real codebases before designing, scoping, or choosing an approach.
model-invocable: true
metadata:
  type: reference
---

# Source Study

Docs describe intent. Source code reveals what actually happens: edge cases, error paths, boundary decisions, real API shapes. Before forming requirements, sizing scope, or designing architecture, study the source of projects that solve similar problems.

## Method

1. **Find candidates**: start from the prior art and any projects the caller passed, and search for more, yourself or with `@web-researcher` for a wider sweep: projects that solve similar problems, competing libraries, reference implementations. Prefer actively maintained projects with real users.
2. **Clone** to the shared reference cache at `~/.meridian/ref/<name>`. Full clone by default (explorers need `git log` and `git blame`). Keep repos across sessions.
3. **Investigate**: spawn an `@explorer` for each area of a source worth studying, with targeted questions, not an open-ended "tell me about this codebase." Run explorers for different sources in parallel.
4. **Synthesize** the reports yourself into convergent patterns, divergent tradeoffs, surprises, and concrete implications for your work. Write into the work directory.

Load `resources/method.md` for clone mechanics, example prompts, and synthesis patterns.
