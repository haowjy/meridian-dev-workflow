---
name: unravel-codebase
description: Use when the human wants to understand how a codebase works today by walking through it together. Human-paced; source stays read-only unless asked; fixes the docs it reads along the way.
disable-model-invocation: true
metadata:
  type: mode-shift
argument-hint: Which area or question? (optional)
---

# Unravel Codebase

Load `/meridian-dev-workflow:qi-layer` if it isn't already loaded.

Walk through the codebase with the human until how it works **today** is clear to both
of you. Stay beside the user: follow their questions, go at their pace, say when something
is unclear to you too.

Use `/meridian-dev-workflow:qi-layer` to read the repo's inline knowledge when it has it. When the scope
is too wide for one pass, spawn `@explorer` subagents to map subsystems in parallel.

Reading the docs is also a chance to improve them: correct KB and vocab drift, sharpen
what's confusing, flag what you can't resolve yet. Follow `/meridian-dev-workflow:knowledge-layers` and
`/meridian-dev-workflow:shared-dao`; edit source only if the user asks.

Done when the starting question is answered or the user says they've seen enough.
