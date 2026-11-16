---
name: architecture
description: "Load when a decision places a boundary, a dependency direction, or a data model, or when a design needs settling: entanglement, tradeoff dimensions, structural risk."
model-invocable: true
metadata:
  type: reference
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
cheapest probe instead. Before proposing a new mechanism, field or table,
find the one the project already has and extend or replace it: a second
copy of a concept drifts from the first. Before proposing one the project
doesn't have yet, find out how others built it, and study each reference
the human names the same way: how it actually works, from its source, its
docs and its builders' own write-ups, not from what you remember of it
(`/source-study`, or a researcher). Record in the design what you read and
what you take from it.

Settle a boundary, data model or contract by comparing real alternatives, the first one
you found among them, each with what it costs. When the comparison on paper
doesn't settle it, build variants concrete enough to choose between:
converging with low confidence defers the decision to implementation, where
it costs more.
