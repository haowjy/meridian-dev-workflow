---
name: probe
type: mode-shift
description: |
  Runtime verification — run real commands, exercise real workflows, report what
  happens. Two modes: probing (exploratory — "how does this behave?") and
  verification (confirmatory — "does this change work?"). Load when you need to
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

Run actual commands and capture exact output. Go adversarial after the happy
path: bad input, interruption, sequencing, boundary conditions, invalid state,
fresh-state variants. Focus on user-visible behavior: exit codes, error
messages, output shape, side effects.

Generate edge cases beyond what was described. When something fails, record
the exact command, the actual output, and what the correct behavior should be.

## Reporting

**Probing:** discovered behavior, constraints, surprises, exact commands
and outputs, open questions.

**Verification:** per-requirement outcomes with runtime evidence, exact
commands and outputs, exploratory findings beyond stated requirements,
coverage gaps.
