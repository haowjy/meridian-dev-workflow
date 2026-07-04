---
name: tech-docs
type: reference
description: >-
  Use when writing design documents. Architecture specs, behavioral specs,
  component docs, feasibility reports.
model-invocable: true
---

# Tech Docs

Methodology for writing design documents: the artifacts under `design/` that architects produce and coders build from.

Load `/llm-writing` if it isn't already loaded.

## One Concept Per Document

One component, one interface, one interaction pattern, one decision per file. When a doc starts covering two things, split it. Name files by what they describe (`token-validation.md`), not when they were written (`auth-redesign-notes.md`).

## Hierarchical Structure

Depth matches complexity. A simple topic gets a flat file. A complex subsystem gets nested directories with an `overview.md` at each level that orients the reader.

## Linked Web

Link to related docs using relative paths: components link to what they interact with, interfaces they implement, tradeoffs that shaped them. Maintain links as you would imports.

## Style

Write docs that work in isolation: self-contained, enough inline context that a reader doesn't need three other docs first. Be concrete: file paths, function names, type signatures. State invariants explicitly.

Prefer mermaid diagrams for component relationships and data flows. Tables for comparisons. Capture what code can't tell you: dependency directions, data flows, why the system is shaped this way. Reference source locations rather than pasting code.

## Verification

Use `/md-validation` for link checking and diagram validation after writing or restructuring linked docs.
