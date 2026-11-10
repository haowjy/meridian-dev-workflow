---
name: diagnose
description: Load when diagnosing hard bugs or performance regressions. Structured loop from feedback loop through instrumentation to fix.
metadata:
  type: reference
alwaysApply: false
---

# Diagnose

Find the root cause of a hard bug. Fix it only when your brief assigns the
fix; otherwise remove your instrumentation and throwaway code and report the
cause with its evidence.

## Build a Feedback Loop First

A fast, deterministic pass/fail signal you can run yourself is most of the
work: with one, the cause falls out; without one, reading code rarely finds
it. Spend most of your effort here, and keep trying new kinds of loop before
you fall back to reading code: a CLI run diffed against known-good output,
an HTTP script, a failing test at the seam, a headless browser, a replayed
captured trace, a bisection between known states, old against new. Make the
loop faster and sharper as you go. For a flaky bug, raise the reproduction
rate: loop the trigger, add stress, narrow timing windows. When a human has
to act inside the loop, structure it with `scripts/hitl-loop.template.sh`.

Confirm the loop shows the failure the user described, not a nearby one. If
you can't build a loop, say so, list what you tried, and ask for access to
the reproducing environment, a captured artifact, or permission to
instrument. Working from an artifact alone, each hypothesis must predict
something it shows, and the cause stays unconfirmed until a loop reproduces
it.

## Find the Cause

Rank the competing explanations before testing any; testing the first
plausible one alone anchors on it. Make each falsifiable: "if X, then Y
makes the bug disappear." With the human in the conversation, show them the
ranking; they often re-rank it at once. Change one variable at a time, and
tag every debug log with a unique prefix (`[DEBUG-a4f2]`) so cleanup is one
grep. For a performance regression, measure a baseline first, vetted per
`/meridian-dev-workflow:probe`'s `resources/measurement.md`, then bisect.

## Fix and Clean Up

Apply the fix with the loop failing, watch it pass, then rerun the original
scenario. Put the repro command with its inputs, and the cause, in the
commit message. Keep the loop as a regression test only when the user asked
for one, with its red output from before the fix; otherwise delete it with
the instrumentation and throwaway code. When no seam reproduces the bug
cheaply, or the fix exposes tangled callers or hidden coupling, report that
as a structural finding (`/meridian-dev-workflow:thermo-nuclear-review`).
