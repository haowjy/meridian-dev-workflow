# Testers

Match testing to what the phase touches. Coders self-verify with the narrowest
useful evidence. Beyond that, spawn `@prober` with `--skills` for the
verification kind.

## Skill Picker

| Verification kind | Spawn | When |
|-------------------|-------|------|
| Quick manual smoke | `@prober` | CLI, process, non-UI behavior checks |
| Structured manual QA | `@prober` | Verify affected existing behavior and new requirements; pass scenarios and expected outcomes |
| Frontend / UI | `@prober --skills agent-browser` | Rendering, flows, console errors in a real browser |
| Feasibility spike | `@prober --skills poc` | Can we do X? Throwaway code, verdict, delete |
| Heavy / destructive env | `@prober` | Temp repos, clean-baseline comparisons |

Testers generate their own edge cases beyond the requirements the caller
hands over.

## Model and Context Selection

Use the prober's inexpensive default for CLI and process checks. For browser/UI
verification, attach `agent-browser` and select a route that supports the inputs
and tools the task needs; screenshot checks require image understanding.

A free endpoint whose description says it may train on submitted context is
an option for inexpensive visual probing when all submitted context is
approved for training. Make that decision before sending the brief,
screenshots, or tool output. Otherwise choose an approved alternative route;
do not let price or a profile default override the data-use constraint.

Use `@browser` for general website interaction or design research; use `@prober`
for independent verification against requirements. Both can use the same browser
tools without having the same assignment.

## Regression vs Acceptance

Use separate prober prompts for major runtime changes:

- **Regression**: affected existing behavior still works. Give canonical smoke
  guides, nearby old flows, fresh-state and edge cases likely to regress.
- **Acceptance**: new or changed behavior satisfies requirements. Give the
  requirement list and ask for real commands, outputs, and failure cases.

Run in parallel when they can use isolated state. If shared runtime state
could interfere, give each prober a separate temp project or run sequentially.

## Automated Tests

Automated gates (typecheck, lint, `pnpm test`) stay on `@coder`, not prober.

Spawn a test-writing coder only for tests the user asked for, and name each
test in the brief.

`@coder` with `/testing` `resources/unit-patterns.md`: pure-core edges and
named regressions. Isolated and fast.

`@coder` with `/testing` `resources/integration-patterns.md`: module
boundaries, coordination logic, contracts between collaborators.

## Test Retention

Disposable probes, one-off fixtures, and tests written to check the work:
removed once verification passes. Tests the user asked for: stay. Uncertain
coverage becomes a better manual smoke guide, or a test you propose to the
user.
