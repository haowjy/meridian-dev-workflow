---
name: visualize-codebase
type: reference
description: Build a structured artifact that maps a codebase — structure, data flow, connections, and where something looks off.
user-invocable: true
argument-hint: "Which area, flow, or question? (optional)"
model-invocable: false
---

# Visualize Codebase

Load `/qi-layer`, `/information-hierarchy`, and `/structured-artifact` if they
aren't already loaded.
When invoked with `/unravel-codebase`, also load `resources/unravel-codebase.md`.

Match what you show to what the human is trying to learn — a single flow needs Behavior,
an onboarding overview needs all four dimensions. Build the mental model they couldn't get
from reading files one at a time. Start with orientation (what is this system, where does
execution begin — one screen), then teach progressively: Structure → Behavior → Health.
Each level navigable on its own.

## Dimensions

- **Structure** — what exists. Entry points (routes, CLI handlers, event listeners,
  `main`), module boundaries, layers (API / service / domain / data / infrastructure).
- **Behavior** — how it moves. Data flow from entry to persistence to response, request
  traces across modules, state stores (DB, cache, session, in-memory) and what mutates
  them, async boundaries where execution leaves the request thread.
- **Relationships** — what connects to what. The dependency graph and its direction,
  coupling hotspots (high fan-in or fan-out), and the data model (tables/collections and
  their relations). Relationships surface as the arrows within Structure and Behavior
  diagrams. For DB schemas, see `resources/db-schema.md` — introspect a live database
  into Mermaid ER scoped to the relevant tables.
- **Health** — what could break. Circular dependencies, layer violations, god modules,
  dead code, race conditions. Annotate these on the structure diagram in place (distinct
  styling on the suspect node or edge) rather than a separate graph.

## Splitting the Artifact

Give each level its own page and link between them — orientation first, then one page per
dimension or sub-area the viewer drills into. Each page should make sense on its own (title,
context sentence, diagram) so someone arriving from a link doesn't need the parent open.
Split further when a single diagram outgrows a phone screen.
