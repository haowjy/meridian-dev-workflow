# Test Quality Review

Evaluate whether tests earn their maintenance cost. The test writer already
believes their tests are useful: your value comes from finding the ones that
aren't.

## Are They Testing the Right Things?

**Edge cases over happy paths.** The happy path usually works: that's what
the coder verified during implementation. Tests earn their place by catching
what's hard to see: boundary conditions, off-by-one errors, empty inputs,
overflow, unexpected types, partial failure, ordering assumptions.

A suite of happy-path tests gives false confidence and still costs run
time on every check. Flag happy-path tests that guard no named risk.

**Behavior over implementation.** Tests that assert on return values, state
changes, and observable side effects survive refactoring. Tests that reach
into private state, assert mock call counts, or mirror the implementation
line-by-line break on every structural change. If a correct refactor would
break the test, it's testing the wrong thing.

**Earned place.** High-risk paths (data integrity, auth, integration
boundaries, state machines) need their edge cases checked: by a probe, or by
a test the user asked for.
Low-risk paths (formatting, simple getters) deserve nothing or a manual smoke
check. Flag tests with no named continuing risk, and weaker duplicates of tests
that stay. A passing probe does not retire a test kept for a named
regression or an external contract. A missing test is not a finding: report the unverified
failure mode, and the lead decides whether a probe or a test answers it.

## Would They Catch a Real Bug?

**Tautological assertions.** Tests that pass regardless of whether the code
is correct: asserting a mock returns what it was configured to return,
asserting that a function "returned something," or mirroring the
implementation verbatim. Delete the code under test mentally: would this test
still pass?

**Tests that never fail meaningfully.** Assertions that only check "no
exception was thrown" or "function was called." These pass on both correct and
broken code.

**Mock-dominated tests.** When mock setup is longer than the test itself, the
test is verifying the mocks, not the code. If the real collaborator changes
behavior, the mock still passes and the test lies. Flag for refactoring
(extract pure logic) or tier promotion (move to integration).

## Structural Health

**Tier placement.** Is this test at the right level? Unit tests that need
filesystem setup are integration tests in disguise. Integration tests that
spin up real databases are manual smoke checks or automated e2e tests, not
ordinary integration tests. Manual smoke checks that verify exact string formatting
should be dropped.

**Hermetic isolation.** Tests that share state, depend on execution order,
or call real network endpoints are flaky by design. Each test should be
self-contained.

**Stale tests.** Tests for code paths that no longer exist, behaviors no
longer required, or edge cases superseded by structural changes. They pass,
they cost maintenance, they protect nothing.

## Report Format

For each finding: what test, what's wrong, why it matters, what to do about
it. Group by severity: tests that give false confidence are more dangerous
than tests that are merely wasteful.
