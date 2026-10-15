---
name: ui-implementation
type: mode-shift
description: "Load when turning a settled visual direction (mockups, a spec, screenshots) into production UI, so the result matches the design and every state renders, not only the one in the mockup."
model-invocable: true
user-invocable: true
---

# UI Implementation

Turn a settled visual direction into durable UI changes. Read the design
spec, mockups, and screenshots before editing, and build with the existing
design system's components and tokens. Use `/anti-slop` to keep generated-UI
defaults out.

Carry forward the user's intent and what the chosen mockups taught. Keep
what is useful from exploration; delete what was only there to make a
decision.

Build every state, not only the one in the mockup: loading, empty, error,
hover and focus, transitions, responsive widths, and scroll behavior. Where
the spec is silent, make a judgment call and name it in your report.

Check what renders as you build with `/agent-browser`, at the viewports the
brief names, and read the console for errors. A passing build doesn't show
the UI looks right.

Report what changed, the judgment calls you made, what exploration material
was kept or removed, and the rendering evidence.
