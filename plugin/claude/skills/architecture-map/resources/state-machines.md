# State Machine Pages

A state machine is anything with named states and rules for moving between
them: a status column, a reducer, a connection, a lifecycle spread over two
fields. To find them all in an area too large to read, have explorers search
for each of those shapes.

- **Beside the code.** Each machine's page is the `state-machines.md` in the
  `.context/` beside the code that owns its transitions: a Mermaid
  `stateDiagram-v2` of the machine as the code has it, the rules with their
  reasons, and what a wrong edit breaks. Change the code and the diagram in
  the same commit, and say so in a comment where the transitions are.
- **One index.** `.context/state-machines/index.md` at the root lists every
  machine, grouped by where it lives, each with what it is the state of and
  a link to its page. The config's `stateMachines` holds the check to it.
- **Patterns.** A shape that recurs (an action whose request can go
  unanswered, durable work under a lease, a stream over a connection that
  drops) gets its own page under `.context/state-machines/`: the shape
  drawn once, its rules, and a table of how each instance differs from them.
- **Too complex.** A machine with more states or rules than its job needs,
  or one built several times over, gets a note in the `TODO` of the
  `.context/` beside it, saying what could go.
