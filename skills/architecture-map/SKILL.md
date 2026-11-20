---
name: architecture-map
description: "Load when building or reshaping a codebase's architecture map: which views of a system to draw (where it runs, code, data, a request's path, lifecycles, boundaries, limits, journeys), what goes on each, examples by kind of system, with its arrows held to the code and kept current in the same commit as the change."
model-invocable: true
user-invocable: true
metadata:
  type: reference
---

# Architecture Map

Load `/atlas` if it isn't already loaded: an architecture map is an atlas of
a codebase, and `/atlas` holds how to draw its pages, build it and keep it
true. This skill holds what a codebase's map shows and how its arrows are
held to the code.

## Choose the Views

A system has several architectures at once, and one diagram can show only
one of them. Each view below answers a different question. Draw the first
two for any codebase; add another when the system has something a reader
would get wrong without it.

| View | The question it answers | Frames and boxes |
|---|---|---|
| **Where it runs** | What processes and stores exist, and what runs in each? | A frame for each place code runs or data rests (browser, server, a per-item worker, database, object store); the modules inside; outside services unframed |
| **Code** | What depends on what? | Apps and packages as layers; arrows mean "uses" |
| **Data** | What is recorded, and what owns what? | The records and how they nest; a frame for each store when there are several |
| **A request's path** | What happens, in order, when someone does the main thing? | The numbered arrows on the System page, and a flow per journey |
| **Lifecycles** | What states can this be in, and what moves it? | One state machine per thing that has states |
| **Boundaries** | What can read or reach what, and where do secrets sit? | A frame for each zone of trust; arrows only where something may cross |
| **Limits** | What bounds cost, load or time, and what happens at the bound? | The budget or quota, what draws on it, what stops when it runs out |
| **Journeys** | What does a person do and see? | Steps, each with its screen |

`resources/views.md` says, for each view, what to put on the page, what its
arrows mean and what to leave off. `resources/systems.md` gives examples of
systems (a web app with workers, an agent system, a data pipeline, a
library, an event-driven backend, a client that syncs) with the views each
needs and the frames its "where it runs" page uses.

The System page is the "where it runs" view: frame it by where each part
runs, not by team or folder, and name a frame for its role ("Actor host"),
with today's vendor in the box's text. A frame is a Mermaid `subgraph`.

## What the Map Holds

- **System**: what runs (services, stores, external services), framed by
  where each part runs, with the path of one request or job numbered from
  start to end, and the credentials each box holds under `Keys`.
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
