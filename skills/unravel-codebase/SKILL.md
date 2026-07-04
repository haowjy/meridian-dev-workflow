---
name: unravel-codebase
type: mode-shift
description: |
  Walk through a codebase together: a companion reads alongside you, explains how
  things work and connect, and says when something is murky to it too. Doubles as a
  cleanup pass on the docs you read: fix KB/vocab drift, clear up confusing spots, and
  flag what to fix later. Human-paced; source stays read-only unless you ask.
user-invocable: true
argument-hint: "Which area or question? (optional)"
model-invocable: false
---

# Unravel Codebase

Load `/qi-layer` if it isn't already loaded.

Walk through the codebase with the human until how it works **today** is clear to both
of you. Stay beside the user: follow their questions, go at their pace, say when something
is unclear to you too.

Use `/qi-layer` to read the repo's inline knowledge when it has it. When the scope
is too wide for one pass, spawn `@explorer` subagents to map subsystems in parallel.

Reading the docs is also a chance to improve them: correct KB and vocab drift, sharpen
what's confusing, flag what you can't resolve yet. Follow `/knowledge-layers` and
`/shared-dao`; edit source only if the user asks.

Done when the starting question is answered or the user says they've seen enough.
