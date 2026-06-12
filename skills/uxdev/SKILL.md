---
name: uxdev
type: mode-shift
description: Shift into visual design mode — learn the design language, iterate with taste, verify what renders. Load when you need to think visually about what the user sees.
model-invocable: true
---

# UX Dev

Load `/design-craft` and `/anti-slop` before proceeding.

## Learn Before Drawing

Understand the existing design language — tokens, components, typography, spacing, interaction patterns. Read at least one representative component or page. Use what's there when it works; branch out when the UX wins.

## Stay Close to Taste

Keep asking the questions that change the design: audience, constraints, references, anti-references, tradeoffs, and what "yes, that's it" would mean. Visual intent is often underspecified — when ambiguous, make a deliberate choice and state it.

## Make Ideas Visible Fast

Mockups are conversation material, not deliverables. Use fast sketches to let the user see options, compare directions, or react to something concrete. Hardcoded data, temporary routes, and rough state are fine — keep them obvious and easy to delete.

## Verify What Renders

A UI change is not understood until it has been opened in a browser, checked at the relevant viewport, and compared against the visual goal. Screenshots beat prose for visual evidence. Use `@browser-prober` or `/playwright-cli` to drive the real rendering.

## Converge Before Hardening

Lock visual direction before production code commits to it. When the direction is clear, shift to `/ui-implementation` for durable changes. Keep what is useful from exploration; clean up what was only there to make a decision.
