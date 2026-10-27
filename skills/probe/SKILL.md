---
name: probe
description: "Load when you need to know what the system actually does: run it, exercise workflows, reproduce bugs. Reading code and passing tests don't show that."
model-invocable: true
metadata:
  type: mode-shift
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
directory and cite their paths. Keep raw captures (traces, HARs, profiles,
browser data, dumps) out of the work directory; save the excerpt that shows the finding.

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

## Share the Host

Other agents and the human share this machine's memory, CPU, and disk. When
memory runs out, the kernel kills whichever process it picks, often someone
else's. Probe the dev stack and browser already serving your source checkout. Start
your own only when none is running or your probe would contaminate it:
destructive steps, a clean baseline.

Put your run ID (the one your caller holds) in the names you choose: worktrees,
temp dirs, tmux sessions, databases, browser sessions. A probe that dies
mid-run never cleans up, and the ID is how its caller finds what it left.
Before you report, stop what you started and delete the scratch you created,
keeping the evidence your report cites. List anything you left running and
why.

## Measurements

Record the numbers the brief names, plus the few this task makes useful, so
the next run has something to compare against: wall-clock time, latency
(p50/p95), peak memory, CPU time, steps or clicks to finish a workflow,
retries, items processed, payload sizes, error counts, or others. Give each its unit, conditions, and how you got it. Vet every performance
comparison you report (faster, slower, a regression) with
`resources/measurement.md` before it goes in your report.

## Reporting

Separate reproduced defects from usability concerns and unconfirmed observations.
For each, include the evidence, user impact, and basis for the expectation.

**Probing:** discovered behavior, constraints, surprises, numbers, exact
commands and outputs, screenshot paths, open questions.

**Verification:** per-requirement outcomes with runtime evidence, numbers,
exact commands and outputs, screenshot paths, exploratory findings beyond stated
requirements, coverage gaps.
