---
name: architecture
description: 'Load when a decision places a boundary, a dependency direction, or a data model, or when a design needs settling: entanglement, tradeoff dimensions, structural risk.'
metadata:
  type: reference
alwaysApply: false
---

# Architecture

## Entanglement

Judge a design by what it braids together that could be independent: state
with value, what with how, policy with mechanism. Simple means untangled,
and you can point at it in the code; familiar only means the reader has seen
it before. More parts hanging straight beat fewer parts tied in a knot, so
merge components only when their concerns stay apart.

Boundaries, data models and contracts are expensive to move once code builds
on both sides. Spend the scrutiny there, not on the inside of a well-bounded
module.

## Settling a Design

Edge cases, failures and boundaries are requirements: list them before
committing. "Find out during implementation" is a risk flag; run the
cheapest probe instead. Before proposing a mechanism the project doesn't
have yet, find out how others built it (search the web, or spawn a researcher), and record in the design what you
found and what you take from it. When you're unsure between options, build
variants concrete enough to choose between: converging on one with low
confidence defers the decision to implementation, where it costs more.
