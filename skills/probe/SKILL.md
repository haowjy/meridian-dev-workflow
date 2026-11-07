---
name: probe
description: "Load when you need to know what the system actually does: run it, exercise workflows, reproduce bugs. Reading code and passing tests don't show that."
model-invocable: true
metadata:
  type: mode-shift
---

# Probe

Run the real system and observe what happens. Real commands, real filesystem,
real network. Use it as a real user would, and notice what's weird. Read the project's
testing instructions (README, AGENTS.md) before starting.

## Know the User

Before you run anything, settle who uses this part of the system, what
they came to do, and what they would look for along the way: the result
they expect to see, how they'd know it worked, what would worry them.
Take it from the brief; where the brief doesn't say, from the project's
docs and the product itself. A writer moving a chapter, an operator
reading a failed run's logs, and a script parsing JSON output each notice
different things. Keep that person in mind for the whole run.

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

Confirmatory. Does the change deliver what the requirements describe, and
does it work for the person using it?

- Use it first as that user would, toward their goal, and
  notice what feels off: misleading feedback, inconsistent output, awkward
  steps, a wait with no sign of progress, unclear next actions or recovery.
  Anything abnormal is probably a UX bug; report it, even when every
  assigned check passes, without turning the run into an unrelated audit
  or fixing it.
- Treat each stated requirement as mandatory baseline coverage: verify
  each, then probe beyond what's claimed.

Report per-requirement outcomes with evidence, and what felt off.

## Execution

Run the built artifact, not the development toolchain. Start the server and
hit the endpoint. Run the CLI and read the output. Open the UI and click the
button. The project's test suites (`pytest`, `vitest`, `jest`, `cargo test`,
`npm test`, etc.) are not evidence here: they verify developer assumptions,
not user experience. A throwaway test or script you write in a scratch
directory to reproduce one failure against the real stack is: use one where
a user can't create the condition, such as a race or a crash mid-write.

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

Put your spawn ID (the one your caller holds) in the names you choose: worktrees,
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

Open with the user you played: who they are, what they came to do, and
what they were looking for. Separate reproduced defects from usability concerns and unconfirmed observations.
For each, include the evidence, user impact, and basis for the expectation.

Every report has a **What felt off** part, even when every check passed:
what confused, surprised, or slowed you as the user, with where it happened.
Write "nothing" there only after you looked.

**Probing:** discovered behavior, constraints, surprises, numbers, exact
commands and outputs, screenshot paths, open questions.

**Verification:** per-requirement outcomes with runtime evidence, numbers,
exact commands and outputs, screenshot paths, exploratory findings beyond stated
requirements, coverage gaps.
