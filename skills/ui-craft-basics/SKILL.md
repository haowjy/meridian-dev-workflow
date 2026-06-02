---
name: ui-craft-basics
type: principle
description: Lightweight UI craft guardrails for mockups and production frontend work — preserve intent, respect the design system, verify what renders.
model-invocable: true
---

# UI Craft Basics

Frontend work starts from intent and the existing product. Preserve the user's
visual goal, the project's design language, and any supplied mockup,
screenshot, or design brief.

Use existing components, tokens, spacing, typography, and interaction patterns
when they fit. Branch out only when the requested direction or user experience
needs it. Avoid generic defaults: unmotivated purple gradients, identical card
grids, gray-on-tint body text, decorative glass, and visual effects that do not
serve the interaction.

Look at real rendering. A UI change is not understood until it has been opened
in a browser, checked at the relevant viewport, and compared against the visual
goal. Screenshots beat prose for visual evidence.

For mockups, keep shortcuts obvious and disposable. For production work, clean
up exploration artifacts and leave durable code.
