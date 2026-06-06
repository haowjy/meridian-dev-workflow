---
name: test-architecture
type: reference
description: Strict test structure audit — fixture sprawl, implementation-pinned tests, deletion targets, test file boundaries, deep test-module opportunities. Use when test code is making the codebase harder to change.
model-invocable: true
---

# Test Architecture Review

Use this skill for a strict audit of test code structure and maintainability.
The goal is making the codebase easier to change — tests that resist refactoring
or accumulate without earning their place are architectural debt, not safety.

Tests are first-class code. A test suite that pins implementation, sprawls
across fragmented files, or accumulates dead weight makes every future change
more expensive than it should be. This skill hunts that structural cost.

Be **ambitious** about test simplification. Actively search for the structural
move that makes the test suite dramatically simpler, smaller, and more resilient
to change.

## Core Prompt

Start from this baseline:

> Perform a structural audit of the test suite. Hunt for tests that pin
> implementation rather than behavior, flaky tests that erode CI trust,
> fixture architecture that makes tests hard to change, test files that
> sprawl past healthy boundaries, tests that don't actually test anything
> meaningful, and coverage that duplicates rather than composes. Be
> ambitious — look for the restructuring that deletes whole categories of
> test complexity while preserving or improving behavioral confidence.

## The Hunt

### Implementation-Pinned Tests

Tests that break when implementation changes, not when behavior changes.
These are the most expensive tests in the suite — they resist every refactor
and teach the team to fear structural improvement.

Signs:
- **Private-state assertions** — reaching into internals to verify fields
  or methods not part of the public contract
- **Mock call-count choreography** — asserting `called(3)` or `calledWith(x, y, z)`
  rather than asserting on outcomes
- **Exact-error-message matching** — pinning to a specific string that changes
  whenever copy improves
- **Order-dependent assertions** — tests that break if execution order shifts
  even though the final state is correct
- **Internal method spies** — stubbing methods on the class under test itself
- **Snapshot tests on unstable output** — snapshots of full JSON trees where
  only a few fields matter

For each, ask: what **behavioral contract** does this protect? If none exists,
it's a deletion candidate. If one exists, rewrite to assert on outcomes.

### Mock Architecture

Mocks are a design smell about the code being tested, not about testing.
Heavy mocking signals tangled dependencies or unclear boundaries.

Signs of mock rot:
- **Mock cascades** — stubbing A returns B returns C returns D to set up
  one assertion
- **Mock explosion** — a single test file defines 5+ mocks for unrelated
  dependencies
- **Mock divergence** — two tests mock the same dependency differently without
  documenting why
- **Mock-only test files** — entire test files that only verify mock behavior
  with no real assertions on outcomes
- **Unused mocks** — mocks declared in setup that only a subset of tests use

Prefer fakes (in-memory implementations with real logic) over mocks for
stable contracts. Prefer real instances when the dependency is cheap to
construct and side-effect-free.

### Flaky Tests

Flaky tests are the most corrosive form of test debt. A single flaky test
teaches the team to ignore CI failures — a few flaky tests and the entire
suite loses its signal.

Deletion candidates (flaky == broken, fix or delete):
- Tests that fail non-deterministically with no clear root cause
- Async work that sometimes completes before the assertion and sometimes doesn't
- Tests dependent on external state (current time, random values, file system
  order, network timing)
- Shared mutable state between cases — order-dependent failures
- Tests that time out intermittently under normal CI load

One flaky failure is a bug, not a fluke. A test that can't reliably tell you
whether the system works is worse than no test — it's a test that lies.

### Deletion Targets

The burden of proof is on keeping a test, not on deleting it. A test earns
its place by protecting a named behavioral contract that is cheaper to verify
automatically than manually.

**Dead tests:**
- Tests for removed features or deleted code paths
- Tests that pass vacuously (no assertions, or assertions that can never fail)
- Skipped tests older than one release cycle
- Tests whose production code is commented out or unreachable

**Duplicate coverage:**
- Two tests verifying the same behavior at the same tier
- Unit tests that duplicate coverage already provided by an integration test
  at a stronger boundary
- Parameterized tests where individual cases don't add distinct risk coverage

**Implementation-confidence tests:**
- Tests a coder wrote to gain confidence during implementation, not to protect
  a durable contract
- Tests that exist because "we should have a test for this" without a named
  risk they catch

**Vapid tests** — tests that pass but prove nothing:
- Framework tests — "renders without crashing" as the only assertion, verifying
  that a library function returns what its docs say
- Trivial-property tests — getters returning constructor values, one-line
  wrappers, assertions that pass by construction
- No-assertion tests — `expect(fn()).not.toThrow()` as the sole check,
  calls with no behavioral assertion, tests that exist only to bump coverage
- Configuration tests — "has the expected number of exports," testing things
  the type system already guarantees

**Fixture debt:**
- Factory functions or builders used by only one test
- Setup blocks that prepare state for a single test
- Helper abstractions that obscure more than they clarify

For each deletion candidate: if it fails, what real-world breakage does it
catch? If "nothing" or "a type error the compiler catches," delete it.

### File Sprawl

Test files have size boundaries too. A test file that sprawls becomes a
barrier to understanding what the system under test actually does.

**Size smells** (contextual, not hard cutoffs):
- A test file over 500 lines is suspect; over 1000 is a problem
- A `describe`/`context` block over 100 lines is hard to scan
- A test file testing more than one production module has lost focus
- A `__tests__` directory with 20+ files for one production module signals
  fragmentation

**Fragmented concerns:**
- Related behaviors tested across multiple files with duplicated setup
- Test helpers copied between files instead of extracted
- Integration tests that set up the same scenario independently in each file

**Shallow test modules:**
- Test files with high setup-to-assertion ratio
- Test files that group by technical similarity rather than behavioral coherence

### Deep Test Module Opportunities

When you find 3+ test files in the same area that duplicate setup, mock the
same dependencies, or test variations of the same behavior, consider bundling
them into fewer, deeper test modules.

A deep test module:
- Tests one coherent behavioral surface (a module, a service, an endpoint)
- Shares setup through well-named fixtures or factories, not inheritance
- Makes the contract visible — a reader can scan the `describe` blocks and
  understand what the system promises
- Is self-contained — no need to open three other test files to understand it

### Fixture Architecture

Test fixtures are part of the architecture. Bad fixture design produces tests
that are hard to write, hard to read, and hard to delete.

Signs of fixture problems:
- **Fixture inheritance** — `beforeEach` in a parent `describe` that some
  children override and others depend on
- **Mystery guest** — setup that creates state the reader can't see from
  the test body alone
- **Fixture sprawl** — factory functions that take 8+ parameters, most of
  which are irrelevant to any given test
- **Shared mutable state** — fixtures that mutate global state and require
  tests to run in a specific order
- **Over-factoring** — extracting a one-line helper that names an operation
  already clear from the test itself

## Approval Bar

Tests earn their place by protecting behavioral contracts. Approve when
the suite is a reliable change detector — it catches real breakage and
stays out of the way during safe refactors.

Presumptive blockers — structural problems that resist future change:
- Tests that pin implementation rather than behavior (without a documented
  legacy reason)
- Flaky tests — any test that has failed non-deterministically
- Vapid tests — framework behavior, trivial properties, type-level guarantees
- Dead tests, skipped tests older than one release, or vacuously passing tests
- Mock cascades or mock-only files with no outcome assertions
- Fixture inheritance chains that obscure setup
- Test files mixing concerns from unrelated production modules
- Fragmented concerns that should be bundled into deeper modules

Do not approve merely because tests pass and coverage is high.

## What to Flag

Prioritize findings by structural cost — what makes the next change hardest:

1. **Flaky tests** — erode CI trust; every flaky test is a bug
2. **Implementation-pinned tests** — resist structural improvement
3. **Deletion targets** — dead, duplicate, vapid, or confidence-only tests
4. **Mock architecture problems** — cascades, explosions, mock-only files
5. **File sprawl** — oversized files, fragmented concerns, shallow modules
6. **Fixture problems** — inheritance, mystery guests, over-factoring
7. **Missing deep modules** — opportunities to bundle scattered tests

For each finding:
- **What**: the specific test file, block, or fixture — with paths and line ranges
- **Why it matters**: the concrete cost — what change is harder because of this?
- **Recommended move**: one concrete action — "delete this test," "rewrite to
  assert on outcome X," "bundle files A, B, C into module D"

## Boundary

You audit test structure and report findings. You do not execute changes —
that's the coder's job. Your value is the structural lens: finding what makes
the next change harder than it needs to be and recommending the simplest path
to unfreeze it.

When the production code has testability problems (tight coupling, untestable
interfaces, missing seams), flag them but hand off to
`/improve-codebase-architecture` — your focus is the test code, not the
production architecture that constrains it.
