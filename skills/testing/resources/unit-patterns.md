# Unit Testing

Write the tests your brief names. This resource shapes how to write them; `/testing` decides which tests exist.

Load `/testing` for tier selection and the functional core /
imperative shell pattern.

## Test Value Model

Most unit tests are disposable implementation guards. Durable tests are the priority for regression-critical behavior: bug fixes, easy-to-forget edge cases, and module contracts.

## Scope

Requirements are verified by checking the running system. A unit test covers
a requirement only when the requirement's edges live in pure logic the
running system can't reach without a harness.

## What to Prioritize

- bug-regression guards
- parsing / state-machine edge cases
- module contract boundaries
- failure and boundary inputs

Test behavior callers rely on, and consolidate equivalent coverage; tests that mirror implementation details break on refactors without catching bugs. See `/testing` `resources/common-mistakes.md` for recurring anti-patterns.

## Authoring Craft

- Keep tests isolated, fast, and single-purpose.
- Test behavior through the module's contract, not its internals.
- Use clear names so failure output explains what broke.
- Follow existing project fixture and assertion patterns for the language and framework in use.
- Add short comments only when the edge case rationale is non-obvious.

## Pruning

Actively remove obsolete tests when your scope changes structure:

- tests for removed paths
- tests pinned to invalid internals
- vacuous tests that pass regardless of behavior
- redundant tests with weaker signal than an existing case

Report pruned tests and rationale.

## Reporting

Return:
- per-requirement outcomes with evidence
- tests added beyond stated requirements and why
- failures with diagnosis
- pruned obsolete tests and rationale
