---
name: anti-slop
type: guardrail
description: "Guard against AI-generated UI tells: saturated defaults that appear regardless of brief. Always loaded when doing frontend work."
model-invocable: true
---

# Anti-Slop

If the interface reads as "AI made this," compare its choices with the brief.

## Defaults to Challenge

These patterns often appear without regard to the brief. Treat them as warning signs, not bans: follow the user's direction and established product identity. When neither calls for a pattern, choose a more specific alternative. If a requested choice may harm accessibility or usability, explain the tradeoff and offer a compliant option instead of silently overriding it.

- **Cream / sand / beige body backgrounds.** Often an unconsidered warm-neutral default. Choose them when they fit the brand and content; otherwise use a deliberate brand color, neutral, or darker surface.
- **Gray body text on tinted backgrounds.** Check actual contrast, not color names. If readability fails, adjust the text or surface to meet the project's accessibility standard.
- **Side-stripe borders** and **gradient text.** Often decorative defaults. Keep them when they communicate hierarchy or fit the visual language; otherwise try a quieter treatment.
- **Purple gradients** and **glassmorphism.** Use when they serve the brand or interaction, not as automatic signs of polish.
- **Hero-metric templates** and **identical card grids.** Use when the data or content benefits from those structures; avoid applying them as generic page scaffolding.
- **Tiny uppercase tracked eyebrows** and **numbered section markers.** Use when they help orientation or communicate a real sequence, not as decoration on every section.

## Copy Tells

These are editing cues, not voice bans. Follow the product's established language and the user's brief; prefer specific, useful copy over generic filler.

- Em dashes, repeated aphoristic cadence, and marketing buzzwords ("streamline," "empower," "seamless," "world-class") can make copy sound generic. Keep them only when they fit the voice or convey something precise.
- Button labels should say what the action does ("Save changes" rather than "OK"); links should make sense out of context ("View pricing" rather than "Click here").
- Don't use `•` as a decorative separator between labels or metadata. Separate them with layout and spacing instead; this doesn't apply to semantic bulleted lists.

Several tells together are a reason to compare the design with the brief, not proof that it is wrong.
