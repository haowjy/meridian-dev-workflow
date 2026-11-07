---
name: probe
description: 'Load when you need to know what the system actually does: run it, exercise workflows, reproduce bugs. Reading code and passing tests don''t show that.'
metadata:
  type: mode-shift
alwaysApply: false
---

# Probe

Run the real system and observe what happens: real commands, real
filesystem, real network. Use it as a real user would, and notice what's
weird. Read the project's testing instructions (README, AGENTS.md) first.

## Know the User

Before you run anything, settle who uses this part of the system, what
they came to do, and what they would look for: the result they expect,
how they'd know it worked, what would worry them. Take it from the brief,
or from the project's docs and the product itself where the brief doesn't
say. A writer moving a chapter and a script parsing JSON output notice
different things. Keep that person in mind for the whole run.

## Two Modes

**Probing** (research, design): how does the system behave today? Map what
it actually does, its constraints, and anything that contradicts what was
assumed. Report observations, not pass/fail.

**Verification** (after a change): does the change deliver what the
requirements describe, and does it work for the person using it? Use it
first as that user would, toward their goal, and notice what feels off:
misleading feedback, inconsistent output, awkward steps, a wait with no
sign of progress, unclear next actions or recovery. Then verify each
stated requirement, and probe beyond what's claimed. Report what's
abnormal without turning the run into an unrelated audit or fixing it.

## Execution

Run the built artifact the way its user reaches it, not the development
toolchain. The project's test suites (`pytest`, `vitest`, `jest`,
`cargo test`, `npm test`, etc.) are not evidence here: they verify developer
assumptions, not user experience. A throwaway test or script you write in a
scratch directory to reproduce one failure against the real stack is: use
one where a user can't create the condition, such as a race or a crash
mid-write.

After the happy path, go adversarial: bad input, interruption, sequencing,
boundaries, invalid state, fresh state. Watch what the user sees: exit
codes, error messages, output shape, side effects. When something fails,
record the exact command or UI actions, the actual result, and the
expected behavior; when the expectation is uncertain, report an
observation or open question rather than a bug.

When the result is visual (a web UI, a TUI, rendered output), take
screenshots at the states that matter: before and after the action, each
error, each viewport. Load `/meridian-dev-workflow:agent-browser` for web UIs. Look at each
screenshot yourself before you report it. Save them in the active work
directory and cite their paths. Keep raw captures (traces, HARs, profiles,
browser data, dumps) out of the work directory; save the excerpt that shows
the finding.

## Share the Host

Other agents and the human share this machine's memory, CPU, and disk. When
memory runs out, the kernel kills whichever process it picks, often someone
else's. Probe the dev stack and browser already serving your source
checkout. Start your own only when none is running or your probe would
contaminate it: destructive steps, a clean baseline.

Put your spawn ID (the one your caller holds) in the names you choose:
worktrees, temp dirs, tmux sessions, databases, browser sessions. A probe
that dies mid-run never cleans up, and the ID is how its caller finds what
it left. Before you report, stop what you started and delete the scratch
you created, keeping the evidence your report cites. List anything you left
running and why.

## Measurements

Record the numbers the brief names, plus the few this task makes useful,
so the next run has something to compare against: time, latency, memory,
steps or clicks to finish a workflow, retries, error counts. Give each its
unit, conditions, and how you got it. Vet every performance comparison you
report (faster, slower, a regression) with `resources/measurement.md`
first.

## Reporting

Open with the user you played: who they are, what they came to do, and
what they were looking for. Then a **What felt off** part, even when every
check passed: what confused, surprised, or slowed you as that user, and
where. Write "nothing" there only after you looked.

Separate reproduced defects from usability concerns and unconfirmed
observations, each with its evidence, user impact, and basis for the
expectation. Include exact commands and outputs, screenshot paths, numbers,
and coverage gaps. Verification adds per-requirement outcomes; probing adds
the constraints found and open questions.
