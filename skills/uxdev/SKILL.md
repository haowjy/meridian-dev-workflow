---
name: uxdev
type: mode-shift
description: Shift into visual design mode. Load when you need to think visually about what the user sees.
model-invocable: true
---

# UX Dev

Load `/design-craft` and `/anti-slop` before proceeding.

## Learn Before Drawing

Understand the existing design language: tokens, components, typography, spacing, and interaction patterns. Read a representative component or page. Additions inherit the established system by default; missing documentation is not permission to replace it. Explore a new visual identity only when the brief calls for a new or replacement system.

## Stay Close to Taste

Keep asking the questions that change the design: audience, constraints, references, anti-references, tradeoffs, and what "yes, that's it" would mean. Visual intent is often underspecified; when ambiguous, make a deliberate choice and state it.

## Make Ideas Visible Fast

Mockups are conversation material, not deliverables. Use fast sketches to let the user see options, compare directions, or react to something concrete. Hardcoded data, temporary routes, and rough state are fine. Keep them obvious and easy to delete.

For a new surface or broad redesign, keep a compact direction brief in the work artifact: user and task, constraints, options, chosen direction, and what evidence will show it works. Compare options by task fit, product fit, distinctiveness, and feasibility. Skip the brief for small tweaks.

## Verify What Renders

Use browser evidence to judge a settled, coherent UI change against its visual goal; exercise the primary task and check relevant viewports. Repeat the check when a later fix changes the rendered result. During exploration, inspect a temporary result only when it helps make the next design decision or show the human what changed. A browser check is not a gate for every small visual tweak. Screenshots beat prose for visual evidence. Use `@prober --skills agent-browser` or `/agent-browser` to drive the real rendering.

## Converge Before Hardening

Treat the existing token system as a constraint while exploring. Use temporary or component-local styles to compare directions; don't change shared production tokens to test a visual guess. After the human settles the direction, update or add a shared token only when it captures an intentional reusable design decision. If the work establishes or replaces the shared visual system, update its existing design documentation and token source without creating duplicate design docs. Then shift to `/ui-implementation` for durable changes. Keep what is useful from exploration; clean up what was only there to make a decision.
