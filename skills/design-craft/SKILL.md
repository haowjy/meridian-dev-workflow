---
name: design-craft
type: reference
description: Frontend craft methodology: color, typography, layout, motion, interaction. Load for production-grade visual decisions.
model-invocable: true
---

# Design Craft

## Color

Use OKLCH for all colors.

**Contrast.** Body text >= 4.5:1 against background. Large text (>=18px or bold >=14px) >= 3:1. Placeholder text needs the same 4.5:1. Muted gray body text on a tinted near-white is the most common failure: bump it toward the ink end of the ramp.

**Tinted neutrals** (backgrounds, surfaces): add 0.005-0.015 chroma toward the brand's hue. Don't default-tint toward warm or cool "because the brand feels that way."

**Dark vs light.** Not a default. Write one sentence of physical scene (who uses this, where, under what ambient light, in what mood) and let the scene decide.

**Color strategy** (pick before picking colors):
- **Restrained**: tinted neutrals + one accent <=10%. Product default.
- **Committed**: one saturated color carries 30-60% of the surface. Brand default.
- **Full palette**: 3-4 named roles, each deliberate. Campaigns, data viz.
- **Drenched**: the surface IS the color. Brand heroes, campaign pages.

## Typography

Cap body line length at 65-75ch. Hierarchy through scale + weight contrast (>=1.25 ratio between steps). Cap font-family count at 3 (display + body + optional mono).

Don't pair fonts that are similar but not identical (two geometric sans-serifs). Pair on a contrast axis (serif + sans, geometric + humanist) or use one family in multiple weights.

No all-caps body copy. Reserve uppercase for short labels (<=4 words) and badges.

Display heading ceiling: clamp() max <= 6rem (~96px). Letter-spacing floor: >= -0.04em.

Use `text-wrap: balance` on h1-h3, `text-wrap: pretty` on long prose.

## Layout

Vary spacing for rhythm. Cards are the lazy answer: use them only when truly the best affordance. Nested cards are always wrong. Flexbox for 1D, Grid for 2D.

For responsive grids, prefer auto-fitting column counts over manual breakpoints.

Build a semantic z-index scale (dropdown -> sticky -> modal-backdrop -> modal -> toast -> tooltip). Never arbitrary values like 999 or 9999.

Dropdowns must escape overflow containers: render outside the stacking context.

## Motion

Animate transform and opacity; avoid animating layout properties. Ease out with exponential curves (ease-out-quart / quint / expo). No bounce, no elastic.

Reduced motion is not optional. Provide a crossfade or instant transition alternative.

Reveal animations must enhance an already-visible default. Don't gate content visibility on a transition trigger; hidden tabs and headless renderers won't fire it.

## Copy

Every word earns its place. No restated headings, no intros that repeat the title.
