---
name: integration-test
type: reference
description: Use when verifying that internal components compose correctly — module boundaries, coordination logic, contracts between collaborators — with fakes at external system boundaries. The middle tier between unit and smoke. Not the right fit for pure logic (unit-test) or real runtime behavior against live systems (smoke-test).
model-invocable: false
---

# Integration Testing

Test that components compose correctly with fakes at external boundaries — no
real process spawning, network, or disk I/O outside controlled temp space.

Load `/testing-principles` for tier selection. Use `/ears-parsing` for EARS
parse contract and per-ID reporting.

## Fakes

Fakes implement the same interface as the real collaborator and reproduce the
behaviors the test relies on (success, failure, edge cases). Keep them
deterministic, fast, and close to the tests that use them. When a fake drifts
from the real system, add a contract test that pins the real behavior — but
that's a smoke test, not an integration test.

## Acceptance Contract

When spawned for a phase:
- Read the phase blueprint's `Claimed EARS statements` list
- Treat claimed IDs as mandatory baseline coverage
- Add compositional tests beyond claimed IDs where coordination risk is high
- If claimed IDs are missing or unresolved, report a planning/ownership gap

## Execution

Identify the composition under test and which boundaries are faked. Exercise
the happy path, then failure modes that composition reveals — partial failure,
retry behavior, ordering, error propagation. Confirm observable outcomes.

## Reporting

- Per-claimed-ID outcomes (`verified` / `falsified` / `unparseable` / `blocked`)
- Compositional tests added beyond claimed IDs and why
- Fakes used and any drift risk
- Failures with diagnosis
