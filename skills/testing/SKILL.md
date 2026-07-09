---
name: testing
type: principle
description: Restraint-first testing discipline. Tier selection, when NOT to write tests, functional core patterns.
model-invocable: true
---

# Testing Principles

Testing buys confidence that a change does what it claims and does not break what it didn't touch. Coverage percentages, mock counts, and test totals are instruments, not goals.

Tests are guardrails, not steering: every bug found in the field passed the
tests. No suite makes tangled code easier to change — being able to reason
about the code is primary. If your only confidence in a change is that the
suite stayed green, that's a simplicity problem, not a coverage gap.

## Test for Risk, Not Completeness

Match test effort to risk, not coverage targets. High-risk areas (data integrity, auth, payment, integration boundaries): comprehensive coverage with edge cases and error conditions. Low-risk areas (formatting, simple CRUD): manual smoke check or nothing.

## Tier Selection

- **Pure logic, no I/O?** Unit test. Fast, exhaustive edge cases, no boundaries to fake.
- **Components composing, external systems fakeable?** Integration test. Medium speed, fakes at process/network boundaries.
- **Real runtime behavior matters?** Manual smoke / e2e. Real processes, real APIs, closest to users.

Modern practice leans integration-heavy ("Testing Trophy"): integration tests offer the best ROI because they test behavior the way users invoke it. Unit tests are for pure logic. Automated E2E is for critical user journeys only.

When tier choice is unclear, improve the manual smoke instructions first. Promote to automated tests only when the risk is hard to verify manually and the test protects a named contract cheaply.

See `resources/tier-judgment.md` for the decision diagram.

## Test Behavior, Not Implementation

Assert on outcomes (return values, state changes, side effects), not implementation paths. Tests that verify private state or mock call counts break on correct refactoring. If tests break on a refactor that doesn't change behavior, they're testing the wrong thing.

## Architecture Enables Testing

Functional core / imperative shell: push decisions into pure functions, push I/O to the edges, test the core exhaustively and the shell shallowly. Code that's hard to test usually has a structural problem. Heavy mocking is a smell about the architecture, not about testing.

See `resources/functional-core.md`.

## Hermetic by Default

No external network calls, no shared state between tests, deterministic inputs. Each test is self-contained with its own setup and teardown.

## DAMP Over DRY

Test code should be descriptive and readable in isolation, not aggressively DRY. Shared setup code becomes a hidden dependency that breaks tests in unexpected ways.

## Pre-Fix-Failing Contract

When writing a regression test for a bug fix: run the test *before* the fix
and confirm it fails. Paste the red output. A test that passes pre-fix proves
nothing about the fix. If you cannot demonstrate pre-fix failure, say so
explicitly — don't claim coverage you haven't shown.

## No Test-Specific Branches in Production Code

Never add logic that exists solely to make a specific test pass — e.g.,
checking for a fixture-specific string, special-casing a test token, or
branching on a value that only appears in test data. If the test needs
special behavior, the production code needs a real abstraction for it.

## Tests as Scaffolding

Unit tests written to understand behavior during development are scaffolding.
Once the behavior is understood and covered by integration tests or the
implementation itself makes the risk obvious, delete the scaffolding. Tests
that no longer protect a live risk are maintenance cost, not safety.

## LLM-Generated Test Caveats

LLM-generated tests tend to verify what's already working rather than probe failure modes. Explicitly target: boundary conditions, error paths, adversarial inputs. Generate, execute, analyze gaps, regenerate iteratively.

## Tier Resources

- **Unit**: `resources/unit-patterns.md`
- **Integration**: `resources/integration-patterns.md`
- **Runtime**: `/probe` skill, `@prober` agent
- **Anti-patterns**: `resources/common-mistakes.md`
