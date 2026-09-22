# Testers

Match testing to what the phase touches. Coders self-verify with the narrowest
useful evidence. Beyond that, spawn `@prober` with `--skills` for the
verification kind.

## Skill Picker

| Verification kind | Spawn | When |
|-------------------|-------|------|
| Quick manual smoke | `@prober` | CLI, process, non-UI behavior checks |
| Structured manual QA | `@prober --skills qa-test` | Convergence: regression + acceptance charters |
| Frontend / UI | `@prober --skills agent-browser` | Rendering, flows, console errors in a real browser |
| Feasibility spike | `@prober --skills poc` | Can we do X? Throwaway code, verdict, delete |
| Heavy / destructive env | `@prober` | Temp repos, clean-baseline comparisons |

Testers generate independent edge cases; don't only verify the requirements
handed over by the caller.

## Model and Context Selection

Use the prober's inexpensive default for CLI and process checks. For browser/UI
verification, attach `agent-browser` and select a route that supports the inputs
and tools the task needs; screenshot checks require image understanding.

Muse Contributor is an option for inexpensive visual probing when all submitted
context is approved for training. Make that decision before sending the brief,
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

`@coder` with `/testing` `resources/unit-patterns.md`: tricky logic, edge
cases, regression guards. Isolated, fast, exhaustive on boundary conditions.

`@coder` with `/testing` `resources/integration-patterns.md`: module
boundaries, coordination logic, contracts between collaborators.

## Test Retention

Disposable probes and one-off verification fixtures: removed after verification
passes. Durable unit and integration tests that protect key behavior: stay.
Tech-lead judges which tests earn their place. Uncertain coverage becomes a
better manual smoke guide before it becomes a permanent automated test.
