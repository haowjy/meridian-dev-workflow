---
name: probe
type: mode-shift
description: "Load when you need to know what the system actually does: run it, exercise workflows, reproduce bugs. Reading code and passing tests don't show that."
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

When the result is visual (a web UI, a TUI, rendered output), take
screenshots at the states that matter: before and after the action, each
error, each viewport you check. Load `/agent-browser` for web UIs. Look at
each screenshot yourself before you report it. Save them in the active work
directory and cite their paths.

Run actual commands and capture exact output. Go adversarial after the happy
path: bad input, interruption, sequencing, boundary conditions, invalid state,
fresh-state variants. Focus on user-visible behavior: exit codes, error
messages, output shape, side effects.

Notice confusing or surprising behavior while using the interface, even when
the assigned checks pass: misleading feedback, inconsistent output, awkward
steps, or unclear next actions and recovery. Anything abnormal is probably a
UX bug; report it. Report incidental findings outside the assertions without
turning the run into an unrelated audit or fixing them.

Generate edge cases beyond what was described. When something fails, record
the exact command or UI actions, the actual result, and the expected behavior.
If the expectation is uncertain, report an observation or open question rather
than declaring a bug.

## Measurements

Vet every number you report (timings, throughput, counts) with
`resources/measurement.md` before it goes in your report.

## Reporting

Separate reproduced defects from usability concerns and unconfirmed observations.
For each, include the evidence, user impact, and basis for the expectation.

**Probing:** discovered behavior, constraints, surprises, exact commands
and outputs, screenshot paths, open questions.

**Verification:** per-requirement outcomes with runtime evidence, exact
commands and outputs, screenshot paths, exploratory findings beyond stated
requirements, coverage gaps.
