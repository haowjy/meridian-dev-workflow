# Testers

Coders check their own work with the narrowest useful evidence. Beyond
that, delegate to `@prober`: attach `/agent-browser` for rendering, flows,
and console errors in a real browser, and `/poc` for a feasibility spike
(throwaway code, a verdict, then delete it).

## Model and Context Selection

Use `/agent-staffing`'s Model Selection policy. Confirm the configured route supports the required
inputs and tools; screenshot checks require image understanding. Submitted
context must also be approved for the route's data-use policy, including
training. Report a capability or data-use mismatch before sending the work
rather than silently substituting a model.

Use `@browser` for general website interaction or design research; use `@prober`
for independent verification against requirements.

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
work and the new behavior, on every viewport the change reaches. Checks
that would share state run one after another in that one run.

## When to Probe

Probe once, on the final code, after review has converged: a run before the
last fix shows only the code that fix replaced. Until then the coder checks
each fix on the real system, on what it changes and the screens or commands
next to it. What happens to the defects the probe finds, and where the loop
stops, is in `reviewers.md` After the Review.

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
