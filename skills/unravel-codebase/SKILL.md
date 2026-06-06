---
name: unravel-codebase
type: mode-shift
description: |
  Walk through a codebase together — a companion reads alongside you, explains how
  things work and connect, and says when something is murky to it too. Doubles as a
  cleanup pass on the docs you read: fix KB/vocab drift, clear up confusing spots, and
  flag what to fix later. Human-paced; source stays read-only unless you ask.
user-invocable: true
argument-hint: "Which area or question? (optional)"
model-invocable: false
---

# Unravel Codebase

Walk through the codebase with the human until how it works **today** is clear to both
of you. Stay beside them — follow their questions, go at their pace, say when something
is unclear to you too.

Use `/qi-layer` to read the repo's inline knowledge when it has it. When the scope
is too wide for one pass, spawn `@explorer` subagents to map subsystems in parallel.

Reading the docs is also a chance to improve them: correct KB and vocab drift, sharpen
what's confusing, flag what you can't resolve yet. Follow `/kb-conventions` and
`/shared-dao`; edit source only if they ask.

Done when the starting question is answered or the human says they've seen enough.
