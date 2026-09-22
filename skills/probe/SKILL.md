---
name: probe
type: mode-shift
description: |
  Runtime verification. Run real commands, exercise real workflows, report what
  happens. Two modes: probing (exploratory, "how does this behave?") and
  verification (confirmatory, "does this change work?"). Load when you need to
  shift from building or reviewing into actually running the thing.
model-invocable: true
---

# Probe

Run the real system and observe what happens. Real commands, real filesystem,
real network. Exercise the thing the way a user would.

## Two Modes

| Mode | When | Question |
|---|---|---|
| **Probing** | Research / design | "How does this system behave today?" |
| **Verification** | After a change | "Does this change work correctly?" |

Recognize the mode from context. The tools are identical; the intent differs.

### Probing

Exploratory. Run commands to map behavior, find constraints, surface surprises.

- Exercise normal paths, note what the system actually does
- Probe edges: boundaries, failure, unusual input
- Document discovered behavior and anything that contradicts assumptions

Report findings as observations, not pass/fail.

### Verification

Confirmatory. Verify the change delivers what the requirements describe.

- Treat each stated requirement as mandatory baseline coverage
- Verify each requirement, then probe beyond what's claimed

Report per-requirement outcomes with evidence.

## Execution

Run the built artifact, not the development toolchain. Start the server and
hit the endpoint. Run the CLI and read the output. Open the UI and click the
button. Never run test suites (`pytest`, `vitest`, `jest`, `cargo test`,
`npm test`, etc.): those verify developer assumptions, not user experience.

Run actual commands and capture exact output. Go adversarial after the happy
path: bad input, interruption, sequencing, boundary conditions, invalid state,
fresh-state variants. Focus on user-visible behavior: exit codes, error
messages, output shape, side effects.

Notice confusing or surprising behavior while using the interface, even when
the assigned checks pass: misleading feedback, inconsistent output, awkward
steps, or unclear next actions and recovery. Report incidental findings outside
the assertions without turning the run into an unrelated audit or fixing them.

Generate edge cases beyond what was described. When something fails, record
the exact command or UI actions, the actual result, and the expected behavior.
If the expectation is uncertain, report an observation or open question rather
than declaring a bug.

## Reporting

Separate reproduced defects from usability concerns and unconfirmed observations.
For each, include the evidence, user impact, and basis for the expectation.

**Probing:** discovered behavior, constraints, surprises, exact commands
and outputs, open questions.

**Verification:** per-requirement outcomes with runtime evidence, exact
commands and outputs, exploratory findings beyond stated requirements,
coverage gaps.
