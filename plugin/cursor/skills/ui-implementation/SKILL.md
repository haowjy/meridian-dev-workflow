---
name: ui-implementation
description: Load when turning a settled visual direction (mockups, a spec, screenshots) into production UI, so the result matches the design and every state renders, not only the one in the mockup.
metadata:
  type: mode-shift
alwaysApply: false
---

# UI Implementation

Turn a settled visual direction into durable UI changes. Read the design
spec, mockups, and screenshots before editing, and build with the existing
design system's components and tokens. Use `/meridian-dev-workflow:design-craft` to keep
generated-UI defaults out and to write the words on screen.

Carry forward the user's intent and what the chosen mockups taught. Keep
what is useful from exploration; delete what was only there to make a
decision.

Build every state, not only the one in the mockup: loading, empty, error,
hover and focus, transitions, responsive widths, and scroll behavior. Where
the spec is silent, make a judgment call and name it in your report. Empty
is several states, each with its own words: first use, no results, filtered
to nothing, no permission, and failed to load. Each says what will appear
and how to get it. Missing data shows as missing, never as a zero, an empty
chart, or a green check.

Check what renders as you build with `/meridian-dev-workflow:agent-browser`, at the viewports the
brief names, read the console for errors, and run `/meridian-dev-workflow:design-craft`'s page
checks. A passing build doesn't show the UI looks right.

Report what changed, the judgment calls you made, what exploration material
was kept or removed, and the rendering evidence. List each hint, subtitle,
or helper text kept on the screens you changed, with what it tells the user
that the screen can't show, or say there are none.
