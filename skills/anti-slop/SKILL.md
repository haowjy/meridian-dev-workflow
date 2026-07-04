---
name: anti-slop
type: guardrail
description: "Guard against AI-generated UI tells: saturated defaults that appear regardless of brief. Always loaded when doing frontend work."
model-invocable: true
---

# Anti-Slop

If the interface reads as "AI made this," it failed. These patterns cut across briefs: they appear regardless of what the user asked for. Match and rewrite.

## Immediate Refuse

- **Cream / sand / beige body background.** The warm-neutral band (near-white, tinted warm, reads as cream/sand/parchment/paper) is the saturated AI default of 2026. Use a saturated brand color, true off-white at chroma 0, or a darker mid-tone instead.
- **Gray body text on tinted background.** Washed out, low contrast. Darker shade of the background's hue, or transparency of the text color.
- **Side-stripe borders.** >1px colored accent on cards, list items, callouts. Rewrite with full borders, background tints, or nothing.
- **Gradient text.** `background-clip: text` with a gradient. Use a single solid color.
- **Unmotivated purple gradients.** The default AI palette. If purple isn't in the brand, it shouldn't be in the background.
- **Glassmorphism.** Blur + glass cards used decoratively.
- **Hero-metric template.** Big number, small label, supporting stats, gradient accent.
- **Identical card grids.** Same-sized cards with icon + heading + text, repeated.
- **Tiny uppercase tracked eyebrow above every section.** The 2023-era kicker. One deliberate kicker is voice; on every section it's AI grammar.
- **Numbered section markers** (01 / 02 / 03) above every section. Same reflex. Numbers earn their place when the section IS a sequence and order carries information.

## Copy Tells

- **No em dashes.** Use commas, colons, semicolons, periods. Also not `--`.
- **No marketing buzzwords:** streamline, empower, supercharge, leverage, unleash, transform, seamless, world-class, enterprise-grade, next-generation, cutting-edge, game-changer, mission-critical. Pick specific nouns and verbs.
- **No aphoristic-cadence body copy.** The rhythm of "serious statement, then punchy short negation" repeated across sections.
- **Button labels: verb + object.** "Save changes" beats "OK." Link text needs standalone meaning: "View pricing" beats "Click here."

If three or more of these appear, the design is running on AI defaults, not the brief.
