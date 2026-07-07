---
name: test-architecture
type: reference
description: Strict test structure audit. Load when test code is making the codebase harder to change.
model-invocable: true
---

# Test Architecture Review

Tests are first-class code. A test suite that pins implementation, sprawls past healthy boundaries, or accumulates dead weight makes every future change more expensive. Hunt that structural cost.

Be ambitious about test simplification. Look for the restructuring that deletes whole categories of test complexity while preserving behavioral confidence.

## What to Hunt

- **Implementation-pinned tests**: break on refactoring, not on behavioral change. Private-state assertions, mock call-count choreography, exact error-message matching.
- **Mock rot**: cascades (A returns B returns C), explosions (5+ mocks per file), mock-only files with no outcome assertions. Heavy mocking signals tangled dependencies.
- **Flaky tests**: every flaky failure is a bug. A test that can't reliably tell you whether the system works is worse than no test. Fix or delete.
- **Deletion targets**: dead tests, duplicate coverage, vapid tests (renders-without-crashing, trivial property assertions, no-assertion tests), and implementation-confidence tests with no named risk.
- **File sprawl**: files over 500 lines, fragmented concerns with duplicated setup, test files covering multiple production modules.
- **Fixture problems**: inheritance chains, mystery guests, shared mutable state, over-factored helpers.
- **Regression-shape gaps**: tests that don't construct the pre-fix failing shape, wired features tested only through a domain facade, mocks that violate provider identity contracts.
- **Deep module opportunities**: 3+ test files in the same area duplicating setup or testing variations of the same behavior.

Each finding: what (file paths, line ranges), why it matters (what change is harder), one concrete move.

Prioritize by structural cost: flaky > implementation-pinned > deletion targets > mock rot > sprawl > fixtures.

When production code has testability problems, flag them but hand off to `/thermo-nuclear-review`; your focus is the test code.

Load `resources/smells.md` for detailed smell catalogs and examples.
