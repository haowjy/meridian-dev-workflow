---
name: architecture-map
description: 'Load when building or reshaping a codebase''s architecture map: the atlas of what runs, how the code is layered, what a person does and sees, the state machines and the dependency rules, with its arrows held to the code and kept current in the same commit as the change.'
metadata:
  type: reference
alwaysApply: false
---

# Architecture Map

Load `/meridian-dev-workflow:atlas` if it isn't already loaded: an architecture map is an atlas of
a codebase, and `/meridian-dev-workflow:atlas` holds how to draw its pages, build it and keep it
true. This skill holds what a codebase's map shows and how its arrows are
held to the code.

## What the Map Holds

- **System**: what runs (services, stores, external services), with the
  path of one request or job numbered from start to end, and the
  credentials each box holds under `Keys`.
- **Code**: the apps and packages as layers. Its arrows mean "uses".
- **A page for each service and package**, opened from its box, down to the
  domains and features inside it. A page's parent is the page whose box
  opens it.
- **Journeys**: what a person does and sees, step by step, each step linked
  to the boxes, screens and state machines behind it.
- **State machines**, beside the code that owns them
  (`resources/state-machines.md`), each linked from its box's `Machines`.
- **Dependencies**: the import rules, and a row for each place the code
  breaks one.

A map of a design not built yet uses the same pages, from the design's
contracts and docs: its boxes have no `Paths` until the code exists, and
the code checks stay off until then.

## Arrows and the Code

A solid arrow between two code boxes means the from box's code imports a
value from the to box's, and the check holds it to that once `arrows.imports`
is on. A dependency with no value import behind it (a port handed in, a
callback, a relation through types alone) is dotted, and its label says
which. An arrow to a store, a service or an external is what moves at run
time: SQL, HTTP, files.

Turn on the code checks in the config: `coverage` (every app, package and
feature directory under some box), `services`, `arrows.imports`,
`dependencies` and `stateMachines`. The engine's README gives each key.

Mark what is wrong where it is: a box's `Breaks` names a rule its code
breaks, and `Drift` where the map knowingly lags the code.

## Screenshots

A capture script, run by hand or by a prober and kept out of CI, writes the
screenshots and a manifest whose regions each name the box that explains
them; a box or journey step shows one with `Shot`. The app's build never
includes the map: it names secrets, code paths and accepted gaps.

## Keep It Current

Write these rules into the map's `README.md` and the project's `AGENTS.md`:

- A change that adds, removes or moves something the map names (an app, a
  package, a domain, a feature directory, a path a box names, a boundary)
  updates the map in the same commit.
- A change to what a person does or sees updates that journey.
- An import that breaks a rule adds its row to the dependencies page; the
  change that removes the last such import deletes the row.
- The check passing is not the test: read the boxes you touched and ask
  whether their words, arrows and `Keys` are still true at run time.

To draw a database's tables, open `resources/db-schema.md`.
