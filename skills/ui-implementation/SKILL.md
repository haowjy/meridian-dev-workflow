---
name: ui-implementation
type: mode-shift
description: Use after visual direction is settled and UX Lead needs to turn mockups or requirements into production UI changes.
model-invocable: true
user-invocable: true
---

# UI Implementation

Turn a settled visual direction into durable UI changes.

Carry forward the user's intent, the chosen mockup lessons, and the existing
design system. Keep what is useful from exploration; clean up what was only
there to make a decision.

Work directly when visual judgment and conversation context are still active.
Use `@coder` when the remaining work is mostly state, routing, APIs, data flow,
or broader structure.

Before calling it done, get evidence where mistakes would be costly: browser
behavior, responsive rendering, console errors, React/component quality, or
codebase architecture. Use `@prober --skills agent-browser` and focused `@reviewer` spawns as
needed.

Report what changed, what exploration material was kept or removed, and what
evidence says the result is ready.
