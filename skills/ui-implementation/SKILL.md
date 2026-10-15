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

Do the work directly, including most refactors, while visual judgment and
conversation context matter. Delegate only a big frontend refactor:
`@frontend-coder` for visual work, `@coder` for state, routing, and data
flow, each with a bounded brief.

Before calling it done, get evidence where mistakes would be costly: browser
behavior, responsive rendering, console errors, React/component quality, or
codebase architecture. Check rendering yourself with `/agent-browser`.

Report what changed, what exploration material was kept or removed, and what
evidence says the result is ready.
