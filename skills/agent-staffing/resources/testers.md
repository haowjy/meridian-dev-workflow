# Testers

Match testing to what the phase touches. Coders self-verify with the narrowest
useful evidence. Beyond that, delegate to `@prober` and attach the skill for the
verification kind.

## Skill Picker

| Verification kind | Spawn | When |
|-------------------|-------|------|
| Quick manual smoke | `@prober` | CLI, process, non-UI behavior checks |
| Structured manual QA | `@prober` | Verify affected existing behavior and new requirements; brief it as below |
| Frontend / UI | `@prober`; attach `/agent-browser` | Rendering, flows, console errors in a real browser |
| Feasibility spike | `@prober`; attach `/poc` | Can we do X? Throwaway code, verdict, delete |
| Heavy / destructive env | `@prober` | Temp repos, clean-baseline comparisons |

Testers generate their own edge cases beyond the requirements the caller
hands over.

## Model and Context Selection

Use `/agent-staffing`'s Model Selection policy. For browser/UI verification,
attach `/agent-browser`. Confirm the configured route supports the required
inputs and tools; screenshot checks require image understanding. Submitted
context must also be approved for the route's data-use policy, including
training. Report a capability or data-use mismatch before sending the work
rather than silently substituting a model.

Use `@browser` for general website interaction or design research; use `@prober`
for independent verification against requirements. Both can use the same browser
tools without having the same assignment.

## Briefing a Prober

Lead with the user: who they are, what they are trying to get done, and what
changed for them. Then name the risky areas: where the change could show the
wrong thing, lose work, or leave the user stuck. Ask the prober to use the
system as that user would and report anything odd, not only what the brief
predicts. A script of steps with expected results turns it into a checklist
runner that checks the rows and stops noticing. Write exact steps only for
conditions a user can't create by hand, such as a held or refused request,
going offline, or a second session acting at the same time, and give the
mechanism for each.

One brief covers both the existing flows near the change that must still
work and the new behavior, on every viewport the change reaches. Split it
across probers only when their runs would share state you can't separate.

## When to Probe

Probe once, on the final code, after review has converged: a run before the
last fix shows only the code that fix replaced. Until then the coder checks
each fix on the real system, on what it changes and the screens or commands
next to it. Defects the prober finds go back to the coder; send the prober
back only to what those fixes change.

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
