---
name: architecture
type: reference
description: Use when designing or reasoning about system boundaries, dependencies, and structural risk.
model-invocable: true
---

# Architecture

## Entanglement

The objective design test: which concerns are braided together that could be
independent — state with value, what with how, policy with mechanism? Simple
means untangled, and you can point at it in the code. Familiar is relative to
the reader; never defend or reject a design on familiarity.

Simplicity is not counting. More parts hanging straight beat fewer parts
tied in a knot — don't merge components to lower the count if merging
entangles their concerns.

## Boundaries

A good boundary has high cohesion within and loose coupling between. Types: module (code organization, import direction), process (separate runtime, IPC/network), trust (authenticated vs unauthenticated, internal vs external), API/contract (versioned interface callers depend on).

Boundaries are expensive to move once code builds on both sides.

## Dependencies

Direction matters more than count. Depend toward stability: things that change less. When a volatile component depends on a stable one, changes stay local. When a stable component depends on a volatile one, changes ripple.

Watch for: circular dependencies, stable code depending on volatile code, leaking internal representation across a boundary.

## Tradeoff Dimensions

Pick the ones that match what could actually go wrong:

- **Reversibility**: how expensive to change this later?
- **Coupling**: how many things break when this changes?
- **Complexity**: total ownership cost (code, tests, failure modes, onboarding)
- **Migration path**: how do you get from here to there?
- **Integration risk**: undocumented behavior, version-specific quirks, implicit contracts
- **Testability**: can the design be verified at natural seam points?

## Structural Risk

Wrong calls are expensive in proportion to how much code builds on top. Highest risk: component boundaries, data model shape, trust boundaries, API contracts. Lower risk: internal implementation within a well-bounded module.

Match scrutiny to risk.
