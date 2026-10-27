---
name: testing
description: 'Load when deciding whether to write a test, and at which tier: keep none the user didn''t ask for, and delete tests you wrote to check your work.'
metadata:
  type: principle
---

# Testing Principles

Retained tests add run time to every full-suite gate and upkeep to every refactor, and a slow suite stalls every agent waiting on it. Verify a change by listing how it could fail and checking each failure on the running system, plus the existing tests that cover the code you touched. Report any failure mode you left unverified.

Tests are guardrails: every bug found in the field passed the tests. No suite makes tangled code easier to change; being able to reason about the code is primary. If your only confidence in a change is that the suite stayed green, the code needs simplifying.

## New Tests

Keep no new test unless the user asked for it, directly or through your
brief. A test you write to understand or check behavior while you work is
scaffolding: delete it before you finish. A new parameterized case or an
extension of an existing test counts as a new test. When you think a test
would earn a permanent place, propose it with the failure it would guard;
the user decides.

For a test the user asked for, aim it at the failure it guards (a
boundary, an error path, an adversarial input), and extend or replace the
existing test of the same behavior rather than adding a duplicate.

## Tier Selection

- **Pure logic, no I/O?** Unit test. Fast, exhaustive edge cases, no boundaries to fake.
- **Components composing, external systems fakeable?** Integration test. Medium speed, fakes at process/network boundaries.
- **Real runtime behavior matters?** Manual smoke / e2e. Real processes, real APIs, closest to users.

Cost rises with the tier. A pure-logic unit test runs in milliseconds; an integration test that touches the filesystem, subprocesses, or a database costs orders of magnitude more on every run. Write the cheapest test that reaches the failure, and leave whole workflows to probes and smoke scripts. Automated E2E is for critical user journeys only.

When tier choice is unclear, improve the manual smoke instructions first. Promote to automated tests only when the risk is hard to verify manually and the test protects a named contract cheaply.

See `resources/tier-judgment.md` for the decision diagram.

## Test Behavior, Not Implementation

Assert on outcomes (return values, state changes, side effects), not implementation paths. Tests that verify private state or mock call counts break on correct refactoring. If tests break on a refactor that doesn't change behavior, they're testing the wrong thing.

## Architecture Enables Testing

Functional core / imperative shell: push decisions into pure functions, push I/O to the edges, test the core's edge cases and leave the shell to probes. Code that's hard to test usually has a structural problem. Heavy mocking is a smell about the architecture, not about testing.

See `resources/functional-core.md`.

## Hermetic by Default

No external network calls, no shared state between tests, deterministic inputs. Each test is self-contained with its own setup and teardown.

## DAMP Over DRY

Test code should be descriptive and readable in isolation, not aggressively DRY. Shared setup code becomes a hidden dependency that breaks tests in unexpected ways.

## Pre-Fix-Failing Contract

When writing a regression test for a bug fix: run the test *before* the fix
and confirm it fails. Paste the red output. A test that passes pre-fix proves
nothing about the fix. If you cannot demonstrate pre-fix failure, say so
explicitly.

## No Test-Specific Branches in Production Code

Never add logic that exists solely to make a specific test pass — e.g.,
checking for a fixture-specific string, special-casing a test token, or
branching on a value that only appears in test data. If the test needs
special behavior, the production code needs a real abstraction for it.

## Tier Resources

- **Unit**: `resources/unit-patterns.md`
- **Integration**: `resources/integration-patterns.md`
- **Runtime**: `/meridian-dev-workflow:probe` skill, `@prober` agent
- **Anti-patterns**: `resources/common-mistakes.md`
