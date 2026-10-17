# Common Testing Mistakes

Patterns that look like testing but buy little confidence. Watch for these in code under review and in your own test authoring.

## Testing Implementation Instead of Behavior

Tests that break whenever the code is refactored, even when behavior is unchanged, are pinned to implementation. They impose a tax on every structural improvement and rarely catch real bugs.

**Sign:** "I changed the internal structure and had to update 30 tests."

**Fix:** Test through the module's public contract. Let the internals vary.

## Mock-Heavy Unit Tests

A unit test with many mocks is usually testing the mocks, not the code. If the real collaborator changes behavior, the mock still passes and the test lies.

**Sign:** Setting up mocks takes more lines than the test itself.

**Fix:** Refactor so the decision under test is pure (functional core), or move the test up a tier to integration.

## Tautological Assertions

Tests that pass regardless of whether the code is correct. Common when assertions mirror the implementation verbatim, or when a mock is asserted to return the value it was configured to return.

**Sign:** You could delete the code under test and the test still passes.

**Fix:** Assert on observable outcomes, not intermediate values the code itself produced.

## Coverage Chasing

Writing tests to hit lines rather than to answer a question. Produces tests that exercise code without validating anything meaningful.

**Sign:** Tests named after functions rather than scenarios; assertions that just check the function "returned something."

**Fix:** Start with "what could go wrong here?", check those failures on the running system, and keep a test only when the user asked for it.

## Integration Tests Pretending to be Unit Tests

Fast-looking tests that actually depend on filesystem state, process spawning, or network. They are slow, flaky, and their failures are hard to localize.

**Sign:** Tests labeled "unit" that need `beforeEach` to clean up `/tmp`, or that fail when run in parallel.

**Fix:** Either move them to the integration lane where their cost is acknowledged, or isolate the logic from the I/O.

## Smoke Tests for Internal Logic

Verifying string formatting or parsing via full CLI invocations. Slow, expensive to maintain, and a weaker assertion than the equivalent unit test would give.

**Sign:** A smoke test that checks the exact wording of an error message.

**Fix:** Smoke-test the behavior boundary (command fails with non-zero exit) and leave the exact wording unpinned.

## Tests That Never Fail Meaningfully

Tests that pass on both correct and broken code. Usually because they assert only that a function was called, or that no exception was thrown.

**Sign:** Deleting the function body doesn't break the test.

**Fix:** Assert on outcomes that would differ if the behavior changed.

## Stale Tests

Tests for code paths that no longer exist, behaviors no longer required, or edge cases that were superseded. They run, they pass, they cost maintenance, they protect nothing.

**Sign:** When failing, the first instinct is to delete or rewrite rather than diagnose.

**Fix:** Prune actively. A deleted test that was not earning its keep is a win.

## Conflating Pytest Counts With Smoke/Regression Testing

Reporting pytest unit/integration test counts as "regression tests" or "e2e coverage" when the project's actual smoke tests are manual execution guides (markdown in `tests/e2e/` or `tests/smoke/`).

**Sign:** "Ran 236 regression tests" when all you did was `pytest tests/unit`.

**Fix:** Check the project's testing conventions FIRST. Look for:
- `tests/AGENTS.md` or `tests/CLAUDE.md`: project-specific guidance
- `tests/e2e/` or `tests/smoke/`: if these contain markdown guides, they are MANUAL tests that require actually running CLI commands, not pytest
- CI config: what does the pipeline consider "smoke" vs "unit"?

Automated pytest tests verify internal logic. Manual smoke tests verify user-facing behavior actually works end-to-end. They are not interchangeable. Claiming one as the other gives false confidence.

**The difference:**
- Pytest: `assert parse_config(data) == expected`: tests logic in isolation
- Smoke: `meridian spawn -a coder -p "test"` then verify it actually ran: tests real behavior

Both are necessary. Neither substitutes for the other.
