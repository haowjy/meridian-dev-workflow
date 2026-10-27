---
name: uxdev
description: Load when the work needs visual thinking about what the user sees, so design choices come from the brief and the existing design language, not defaults.
metadata:
  type: mode-shift
alwaysApply: false
---

# UX Dev

Load `/meridian-dev-workflow:design-craft` and `/meridian-dev-workflow:anti-slop` before proceeding.

## Learn Before Drawing

Understand the existing design language: tokens, components, typography, spacing, and interaction patterns. Read a representative component or page. Additions inherit the established system by default; missing documentation is not permission to replace it. Explore a new visual identity only when the brief calls for a new or replacement system.

## Stay Close to Taste

Keep asking the questions that change the design: audience, constraints, references, anti-references, tradeoffs, and what "yes, that's it" would mean. Visual intent is often underspecified; when ambiguous, make a deliberate choice and state it.

## Make Ideas Visible Fast

Mockups are conversation material, not deliverables. Use fast sketches to let the user see options, compare directions, or react to something concrete. Hardcoded data, temporary routes, and rough state are fine. Keep them obvious and easy to delete.

For a new surface or broad redesign, keep a compact direction brief in the work artifact: user and task, constraints, options, chosen direction, and what evidence will show it works. Compare options by task fit, product fit, distinctiveness, and feasibility. Skip the brief for small tweaks.

## Verify What Renders

Use browser evidence to judge a settled, coherent UI change against its visual goal; exercise the primary task and check relevant viewports. Repeat the check when a later fix changes the rendered result. During exploration, inspect a temporary result only when it helps make the next design decision or show the human what changed. A browser check is not a gate for every small visual tweak. Screenshots beat prose for visual evidence. Drive the real rendering with `/meridian-dev-workflow:agent-browser`; delegate to `@prober` and attach `/meridian-dev-workflow:agent-browser` only when you can't run it yourself.

## Converge Before Hardening

Treat the existing token system as a constraint while exploring. Use temporary or component-local styles to compare directions; don't change shared production tokens to test a visual guess. After the human settles the direction, update or add a shared token only when it captures an intentional reusable design decision. If the work establishes or replaces the shared visual system, update its existing design documentation and token source without creating duplicate design docs. Then shift to `/meridian-dev-workflow:ui-implementation` for durable changes. Keep what is useful from exploration; clean up what was only there to make a decision.
