# Companion Walkthrough Capture

Load this when the walkthrough serves the `/unravel-codebase` mode. That mode is a
companion walk — human-paced, conversational, source read-only unless they ask. The
artifact follows that grain.

## Record the Actual Walk

`/unravel-codebase` produces shared understanding through dialogue. The artifact captures
what the two of you actually worked out — the path you took, the questions that came up,
the moments something clicked. It is the residue of the walk, not a textbook diagram of
the system in the abstract.

So build the artifact **during or after** the walkthrough, not instead of it. Walk first;
let the artifact grow to reflect the understanding as it forms. A diagram that shows a
flow you never traced together teaches a model the human doesn't hold.

## What to Capture

- **The actual path.** The entry points you started from, the modules you followed, the
  order you understood them in. Reading order is part of the lesson.
- **The anomalies you noticed.** When something looked off mid-walk — a layer violation,
  a god module, dead code, a name that means two things — annotate it where it occurs in
  the diagram. These are the highest-value marks in the artifact; they are what a fresh
  reader would miss.
- **Open questions.** What stayed murky to both of you. Flag it honestly in the artifact
  rather than papering over it. "Unclear how X reconnects here" is more useful than a
  confident wrong arrow.
- **The aha moments.** The connection that reframed how the system made sense. Make it
  prominent — it is usually the thing worth remembering.

## Annotate Honestly

Mark anomalies and uncertainty directly on the structure: a callout on the node, a
distinct edge style for a suspect dependency, a short note in the detail panel. The
artifact stays honest about what is solid and what is provisional.

## Doc Reconciliation

`/unravel-codebase` doubles as a cleanup pass on the docs you read along the way. When the
walk surfaces KB or vocab drift, follow `/qi-layer` and `/shared-dao` for where the
correction belongs. The artifact can flag "doc says X, code does Y" as an anomaly; edit
source docs only if the human asks.

## Link Back to Source

Every node maps to file paths the human can open. The artifact is a lens onto the real
code — they should always be able to jump from a node to the lines it describes and
confirm the understanding holds.
