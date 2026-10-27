# Integration Testing

Test that components compose correctly with fakes at external boundaries: no
real process spawning, network, or disk I/O outside controlled temp space.

Load `/meridian-dev-workflow:testing` for tier selection.

## Fakes

Fakes implement the same interface as the real collaborator and reproduce the
behaviors the test relies on (success, failure, edge cases). Keep them
deterministic, fast, and close to the tests that use them. When a fake drifts
from the real system, add a contract test that pins the real behavior, but
that is a manual test, not an integration test.

## Scope

Write the tests your brief names. This resource shapes how to write them;
`/meridian-dev-workflow:testing` decides which tests exist. Requirements are verified by checking
the running system.

## Execution

Identify the composition under test and which boundaries are faked. Exercise
the happy path, then failure modes that composition reveals: partial failure,
retry behavior, ordering, error propagation. Confirm observable outcomes.

## Reporting

- Per-requirement outcomes with evidence
- Compositional tests added beyond stated requirements and why
- Fakes used and any drift risk
- Failures with diagnosis
