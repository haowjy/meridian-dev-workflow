---
name: testing-principles
description: >
  Shared foundation for thinking about tests — tier selection, architecture
  patterns like functional core / imperative shell, and the tradeoffs behind
  each tier. Load when deciding what kind of test a change needs, when a
  test suite feels off (too brittle, too slow, too many mocks), or when
  routing work to @unit-tester, @integration-tester, or @smoke-tester.
---

# Testing Principles

Testing buys confidence that a change does what it claims and does not break what it didn't touch. Coverage percentages, mock counts, and test totals are instruments, not goals.

Different tiers answer different questions. The craft is matching tier to question, not stacking tiers for their own sake.

## The Three Questions

- **Pure logic, no I/O?** → unit test. Fast, exhaustive edge cases, no boundaries to fake.
- **Components composing, external systems fakeable?** → integration test. Medium speed, fakes at process/network boundaries.
- **Real runtime behavior matters?** → smoke / e2e. Real processes, real APIs, slower, closest to users.

Most code sits cleanly in one tier. When a change spans tiers, write tests at each tier rather than one sprawling test doing everything.

See `resources/tier-judgment.md` for the decision diagram and tradeoffs.

## Architecture Enables Testing

Testable code is not an accident. Functional core / imperative shell is the pattern worth internalizing: push decisions into pure functions, push I/O to the edges, test the core exhaustively and the shell shallowly.

Code that is hard to test usually has a structural problem. When you reach for heavy mocking, that is a smell about the architecture, not about testing.

See `resources/functional-core.md`.

## Judgment Over Rules

- **Confidence beats coverage.** 80% coverage where the 80% is implementation detail buys less than 40% coverage of the behavior users depend on.
- **Mocking is a tool, not a virtue.** A test that mocks ten collaborators is testing the mocks, not the code.
- **Target user-visible bugs.** Tests exist to catch what would break for someone downstream, not to exercise every line.
- **Delete tests that no longer earn their keep.** Tests pinned to removed paths, duplicated coverage, or implementation details create drag without protection.

See `resources/common-mistakes.md` for the recurring anti-patterns.

## When Each Tester Agent Applies

- `@unit-tester` — phase-scoped tests on the functional core, edge cases, regression guards.
- `@integration-tester` — composition across internal components with fakes at external boundaries.
- `@smoke-tester` — real runtime behavior against real interfaces. Two modes (probing vs verification) — see `/smoke-test`.
- `@verifier` — build-green baseline (tests pass, types check, lint clean). Not a tier; the floor.

Pick the tier that matches the question. Stack tiers only when the question spans them.
