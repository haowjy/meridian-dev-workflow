---
name: react-architecture
type: reference
description: React structural lens. Load when building or reviewing React code for component composition, state architecture, and visual consistency.
model-invocable: true
---

# React Architecture

Applies `/dev-principles` and `/thermo-nuclear-review` to React code, adding what only frontend codebases need.

## Token Discipline

The design system's tokens are the source of visual consistency. Every ad hoc value (raw hex, hardcoded spacing, one-off font sizes) is a drift vector. Components consume tokens; tokens define the feel.

## State Architecture

Server state and client state are different concerns with different lifecycles. Mixing them creates state that's hard to reason about. Keep local state local, use context for low-velocity cross-tree data, and put navigation-meaningful selections in the URL.

## Component Composition

React components scale through composition, not through growing prop lists. Extract when the third use case appears, not the first. Each component does one thing: render, interact, or orchestrate.

## Import Boundaries

Unidirectional: `shared/` -> `features/` -> `app/`. Features don't import from other features' internals. Direct imports in app code; barrel files only for intentional public API surfaces.

## Component API Consistency

Consistent variant prop naming, composition patterns, and naming conventions across component families. Inconsistency means every new component is a learning curve.

## How to Apply

Orient first: read the project's design tokens, component library, and existing patterns. Prioritize by leverage: a token violation in a shared primitive affects every page. Report or fix depending on your role.

Load `resources/smells.md` for detailed hunt lists and stack-specific patterns.
