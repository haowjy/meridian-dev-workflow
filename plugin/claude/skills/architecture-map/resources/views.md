# The Views of an Architecture

Each view is one page, or a page with children. Pick by the question a
reader brings; a view nobody would ask about is not drawn.

## Where It Runs

The question: what processes and stores exist, what runs in each, and what
survives when one of them dies.

- **Frames**: one for each place code runs or data rests. Typical frames: the
  browser or client; each server process; a worker that exists once per item
  (per thread, per room, per tenant), saying what the item is; the stores;
  a queue or scheduler. Services outside the system stay unframed, drawn as
  external boxes.
- **Boxes**: the modules that run in each frame, and each store as its own
  box. A module that is code linked into several processes is drawn once,
  in the frame that owns it, and its text says where else it runs.
- **Arrows**: what crosses between frames at run time (a request, a query,
  a push, a queue message), labelled with what moves. The main request's
  path is numbered.
- **Say on the page**: for each frame, what it holds that nothing else
  holds. A frame that holds nothing durable can be lost and rebuilt, and
  the page should say from what. Name the one authority for each kind of
  record.
- **Leave off**: folders, teams, and libraries with no process of their
  own.

## Code

The question: what depends on what, and which way may a dependency point.

- **Boxes**: apps, packages, then the domains or features inside each on a
  child page.
- **Arrows**: "uses". Solid when an import backs it, dotted when the
  dependency is handed in.
- **Say on the page**: the layering rule in one sentence, and the dependencies
  page holds the rules the check enforces.
- **Leave off**: run-time traffic. An arrow here is an import, never a
  request.

## Data

The question: what is recorded, what owns what, and what a record can
never do (change, be deleted, lose its origin).

- **Boxes**: the kinds of record a reader must know, not every table. A
  record that derives from others shows what it derives from.
- **Arrows**: owns, refers to, is made from.
- **Say on the page**: which records never change, what a deletion removes,
  and which store holds each. For the tables themselves open
  `db-schema.md`.

## A Request's Path

The question: what happens, in order, when someone does the main thing.

- On the System page, number the arrows of one real request or job from
  start to end. One path; other paths are unnumbered.
- For each journey, a flow page: a sequence diagram whose participants are
  boxes on the map, with the calls in order.
- **Say on the page**: where the path waits, where it can fail, and what
  the person sees while it does.

## Lifecycles

The question: what states can this be in, and what moves it between them.

- One state machine per thing that has states, beside the code that owns
  it (`state-machines.md`).
- Keep an arrow's label to a few words and put its condition in a table
  under the diagram: a sentence on an arrow collides with its neighbours.
- **Leave off**: a loop that changes no state. Say it in the text.

## Boundaries

The question: what can read or reach what, and where credentials sit.

- **Frames**: one for each zone of trust: what an anonymous visitor
  reaches, what a signed-in member reaches, what an agent or plugin
  reaches, what has network access and what has none.
- **Arrows**: only where something may cross a boundary, labelled with
  what is checked there.
- **Boxes** carry `Keys`: the credentials each holds.
- **Say on the page**: each rule as what cannot happen ("a sandbox has no
  network", "a run cannot read another run"), and where it is enforced.

## Limits

The question: what bounds cost, load or time, and what happens at the
bound.

- **Boxes**: the limit, what draws on it, and what is stopped, queued or
  refused when it is reached.
- **Say on the page**: who can change the limit, and the one function or
  setting that decides admission.

## Journeys

The question: what a person does and sees.

- Steps in the order the person meets them, each with what they do, what
  they see, the screen (`Shot`) and the box or flow behind it (`Map`).
- One journey per goal a person arrives with, not per screen.

## A Design Not Built Yet

The same views, drawn from the design's contracts and docs. Boxes have no
`Paths` until the code exists. Add a build-order page: the steps as boxes,
arrows meaning "enables", each step naming what is true when it is done.
