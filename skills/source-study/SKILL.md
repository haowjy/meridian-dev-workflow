---
name: source-study
description: Load when you need evidence from real codebases before designing, scoping, or choosing an approach.
type: reference
model-invocable: true
---

# Source Study

Docs describe intent. Source code reveals what actually happens: edge cases, error paths, boundary decisions, real API shapes. Before forming requirements, sizing scope, or designing architecture, study the source of projects that solve similar problems.

## When

- Scoping a feature and need to understand how others solved it
- Choosing between architectural approaches and want evidence
- Integrating with a library whose docs are incomplete
- Designing an API and want to study real-world contracts

## Method

1. **Find candidates**: projects that solve similar problems, competing libraries, reference implementations. `@web-researcher` can surface more. Prefer actively maintained projects with real users.
2. **Clone** to `~/.meridian/ref/<name>`. Full clone by default (explorers need `git log` and `git blame`). Keep repos across sessions.
3. **Investigate**: spawn `@explorer` agents with targeted questions, one focus area each. Fan out 3-5 in parallel. Targeted questions, not open-ended "tell me about this codebase."
4. **Synthesize**: one explorer merges reports into convergent patterns, divergent tradeoffs, surprises, and concrete implications for your work. Write into the work directory.

Load `resources/method.md` for clone mechanics, example prompts, and synthesis patterns.
