---
name: smoke-test
type: reference
description: >
  Use when you need to understand or verify runtime behavior against the real
  system — CLI invocations, HTTP requests, integration flows, race probes,
  interruption recovery. Two modes: probing (how does this behave?) and
  verification (does this change work?). Mandatory for integration boundaries.
model-invocable: false
---

# Smoke Testing

Run the real system and observe what happens. Real processes, real filesystem,
real network.

Load `/testing-principles` for tier selection. Use `/ears-parsing` for
per-pattern parsing and report format.

Check README, AGENTS/CLAUDE guidance, build files, and existing smoke/e2e tests
for canonical invocation patterns. Many projects keep smoke test guides as
markdown in `tests/e2e/` or `tests/smoke/` — check conventions before assuming
what format to use.

## Two Modes

| Mode | Phase | Question |
|---|---|---|
| **Probing** | Research / design | "How does this system behave today?" |
| **Verification** | Implementation | "Does this change work correctly?" |

Recognize the mode from the prompt. The tools are identical; the intent differs.

### Probing

Exploratory. Run commands to map behavior, find constraints, surface surprises.

- Exercise normal paths, note what the system actually does
- Probe edges: boundaries, failure, unusual input
- Document discovered behavior, constraints, and anything that contradicts
  stated assumptions

Report findings as observations, not pass/fail.

### Verification

Confirmatory. The phase claims specific EARS statements; produce evidence for
or against them.

- Read the phase blueprint's `Claimed EARS statements`
- Load referenced spec leaves
- Treat claimed IDs as mandatory baseline coverage
- Verify each claimed ID, then probe beyond the claim

Report per-ID outcomes (`verified` / `falsified` / `unparseable` / `blocked`).

## Execution

Run in the active worktree — the caller already placed you where the change
lives. Inspect `git status` and the working tree before probing so you know
what is already in flight. Use disposable environments (temp repo, throwaway
config) only for destructive probes or clean-baseline comparisons that would
contaminate the worktree.

Respect the shared workspace: do not reset, revert, stash, or clean the working
tree. Do not delete untracked files without ownership confirmation. Keep
generated artifacts and logs contained, and report their paths so cleanup is
explicit.

Go adversarial after the happy path: bad input, interruption, sequencing,
boundary conditions, invalid state, and fresh-state variants. Focus on
user-visible behavior: exit codes, error messages, output shape, on-disk side
effects.

## Reporting

**Probing:** discovered behavior, constraints, surprises, exact commands and
outputs, open questions.

**Verification:** per-claimed-ID outcomes with evidence, exact commands and
outputs, exploratory findings beyond claimed IDs, coverage gaps.

@tech-lead owns `plan/leaf-ownership.md` updates based on verification reports.
