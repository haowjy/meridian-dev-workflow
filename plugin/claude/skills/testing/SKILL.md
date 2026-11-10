---
name: testing
description: 'Load when deciding whether to write a test, and at which tier: keep none the user didn''t ask for, and delete tests you wrote to check your work.'
metadata:
  type: principle
---

# Testing

Retained tests add run time to every gate and upkeep to every refactor.
Verify a change by listing how it could fail (bad input, partial failure,
ordering and concurrency, stale state, the callers and seams it touches) and
checking each failure by running the program end to end. For an edge the
running program can't reach cheaply, use an existing test. Run the existing
tests that cover the code you touched, and report any failure mode you left
unverified.

## Which Tests Stay

Keep no new test unless the user asked for it, directly or through your
brief. A test you write to understand or check behavior is scaffolding:
delete it before you finish. A new parameterized case or an extension of an
existing test counts as new. Propose a test you think would earn a permanent
place, with the failure it would guard; the user decides. Existing tests get
no protection for already being there: delete one that costs more than the
failure it guards.

For a test the user asked for, aim it at the failure it guards and extend or
replace the existing test of that behavior rather than adding a duplicate.
Write the cheapest test that reaches the failure: cost rises steeply from
pure-logic unit tests to tests that touch the filesystem, subprocesses or a
database. Assert on outcomes, not on private state or mock call counts.

A regression test for a bug fix must fail before the fix: run it first and
paste the red output, or say that you couldn't.

Production code never branches just to make a test pass, such as on a
fixture value; give it a real abstraction instead.

For depth: `resources/tier-judgment.md` to choose a tier,
`resources/functional-core.md` when code is hard to test,
`resources/unit-patterns.md` and `resources/integration-patterns.md` when
writing one, `resources/common-mistakes.md` for anti-patterns.
