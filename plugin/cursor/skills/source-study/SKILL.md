---
name: source-study
description: Load when you need evidence from real codebases before designing, scoping, or choosing an approach.
metadata:
  type: reference
alwaysApply: false
---

# Source Study

Docs describe intent; source shows what actually happens: edge cases, error
paths, boundary decisions, real API shapes. Before forming requirements or a
design, study projects that solve a similar problem.

Start from the prior art and any projects the caller named, and search for
more; prefer maintained projects with real users. Clone each into the shared
reference cache at `~/.meridian/ref/<name>`, and keep it
across sessions. Read the code yourself, and spawn an `@explorer` per source
with targeted questions when a source is too large to read. Write into the
work directory what converges, what diverges and why, the surprises, and
what it means for your work. `resources/method.md` has clone mechanics and
example questions.
