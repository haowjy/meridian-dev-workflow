---
name: design-craft
type: reference
description: "Frontend craft methodology: color, typography, layout, motion, interaction. Load for production-grade visual decisions."
model-invocable: true
---

# Design Craft

Follow the explicit brief and established product system. The guidance below gives defaults, not bans; apply only what is relevant to the task. Preserve accessibility and usability requirements. If a requested style may conflict with them, explain the tradeoff and work with the human on an acceptable choice rather than silently overriding the brief.

## Color

For new color decisions, prefer OKLCH when the project supports it. When extending an existing system, follow its token format rather than migrating formats as part of visual work.

**Contrast.** Body text needs at least 4.5:1 against its background. Large text (at least 18pt / 24 CSS px, or 14pt / about 18.67 CSS px when bold) needs at least 3:1. Placeholder text needs the same 4.5:1. Muted gray body text on a tinted near-white is a common contrast failure; check actual contrast and adjust when needed.

**Tinted neutrals** (backgrounds, surfaces): when developing a palette, subtle chroma toward the brand's hue can add depth. Don't add warmth or coolness without a reason.

**Dark vs light.** For a new visual identity, describe who uses it, where, under what ambient light, and in what mood. For an existing product, follow its established system unless the brief calls for a change.

**Color strategy** (for a new or replacement visual identity):
- **Restrained**: tinted neutrals + one accent <=10%. Product default.
- **Committed**: one saturated color carries 30-60% of the surface. Brand default.
- **Full palette**: 3-4 named roles, each deliberate. Campaigns, data viz.
- **Drenched**: the surface IS the color. Brand heroes, campaign pages.

## Typography

For a new type system, aim for body line lengths of 65-75ch, clear scale and weight contrast, and a small number of font families. For existing products, follow the established type scale.

Avoid pairing similar fonts without a clear reason; contrast or one family in multiple weights is often more cohesive. Use all-caps body copy, very large headings, or tight tracking only when they serve the brief and remain readable.

Use `text-wrap: balance` on h1-h3 and `text-wrap: pretty` on long prose where supported.

## Layout

Vary spacing for rhythm. Don't default to cards; use them when they make the content or interaction clearer. Nested card surfaces often add visual depth without useful hierarchy; use them when the relationship needs it. Flexbox is a good default for one-dimensional layouts, Grid for two-dimensional ones.

For responsive grids, auto-fitting columns often need fewer breakpoints.

Follow the project's semantic z-index scale. When none exists, establish one for the relevant layer; avoid arbitrary values like 999 or 9999.

Dropdowns need to escape clipping containers; render them outside the relevant stacking context.

## Motion

Prefer animating transform and opacity over layout properties. Ease-out curves are a useful default; bounce or elastic motion should fit the product's motion language and the interaction's purpose.

Respect reduced-motion preferences with a crossfade or instant alternative.

Reveal animations must enhance an already-visible default. Don't gate content visibility on a transition trigger; hidden tabs and headless renderers won't fire it.

## Copy

Every word earns its place. No restated headings, no intros that repeat the title.
