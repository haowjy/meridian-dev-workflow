# Test Architecture Smells

Detailed smell catalogs for each structural dimension.

## Implementation-Pinned Tests

Signs:
- Private-state assertions: reaching into internals to verify fields not part of the public contract
- Mock call-count choreography: asserting `called(3)` or `calledWith(x, y, z)` rather than outcomes
- Exact-error-message matching: pinning to strings that change with copy improvements
- Order-dependent assertions: tests that break if execution order shifts even though final state is correct
- Internal method spies: stubbing methods on the class under test itself
- Snapshot tests on unstable output: full JSON tree snapshots where only a few fields matter

For each: what behavioral contract does this protect? If none, delete. If one exists, rewrite to assert on outcomes.

## Mock Architecture

Prefer fakes (in-memory implementations with real logic) over mocks for stable contracts. Prefer real instances when the dependency is cheap and side-effect-free.

Signs of rot:
- Mock cascades: stubbing A returns B returns C returns D for one assertion
- Mock explosion: 5+ mocks for unrelated dependencies in one file
- Mock divergence: two tests mocking the same dependency differently without documenting why
- Mock-only files: entire test files that only verify mock behavior
- Unused mocks: mocks in setup that only a subset of tests use

## Deletion Targets

The burden of proof is on keeping a test, not on deleting it.

**Dead tests**: tests for removed features, vacuously passing tests (no assertions or unfailable assertions), skipped tests older than one release, tests whose production code is commented out.

**Duplicate coverage**: two tests verifying the same behavior at the same tier, unit tests that duplicate integration coverage at a stronger boundary.

**Vapid tests**: framework tests ("renders without crashing"), trivial-property tests (getters returning constructor values), no-assertion tests (`expect(fn()).not.toThrow()` as sole check), configuration tests (things the type system guarantees).

**Fixture debt**: factories used by one test, setup blocks for a single test, helper abstractions that obscure more than they clarify.

For each candidate: if it fails, what real-world breakage does it catch? If "nothing" or "a type error the compiler catches," delete it.

## File Sprawl

Size smells (contextual, not hard cutoffs):
- Test file over 500 lines is suspect; over 1000 is a problem
- `describe`/`context` block over 100 lines is hard to scan
- Test file testing more than one production module has lost focus
- `__tests__` directory with 20+ files for one module signals fragmentation

Fragmented concerns: related behaviors tested across multiple files with duplicated setup, test helpers copied between files, integration tests setting up the same scenario independently.

## Deep Test Module Opportunities

A deep test module tests one coherent behavioral surface, shares setup through well-named fixtures (not inheritance), makes the contract visible through `describe` block structure, and is self-contained.

## Fixture Architecture

Signs of problems:
- Fixture inheritance: `beforeEach` in a parent `describe` that some children override
- Mystery guest: setup creating state the reader can't see from the test body
- Fixture sprawl: factory functions taking 8+ parameters
- Shared mutable state: fixtures requiring test execution order
- Over-factoring: extracting a one-line helper naming what's already clear
