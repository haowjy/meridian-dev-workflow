---
name: diagnose
type: reference
description: Load when diagnosing hard bugs or performance regressions. Structured loop from feedback loop through instrumentation to fix.
model-invocable: false
---

# Diagnose

A discipline for hard bugs. Skip phases only when explicitly justified.

When exploring the codebase, check the project's KB vocabulary and context docs for a clear mental model of the relevant modules.

## Phase 1: Build a Feedback Loop

**This is the skill.** Everything else is mechanical. If you have a fast, deterministic, agent-runnable pass/fail signal for the bug, you will find the cause. If you don't, no amount of staring at code will save you.

Spend disproportionate effort here. Be aggressive. Be creative. Refuse to give up.

### Ways to construct one (try in roughly this order)

1. **Failing test** at whatever seam reaches the bug: unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright): drives the UI, asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** Run 1000 random inputs and look for the failure mode.
8. **Bisection harness.** If the bug appeared between two known states (commit, dataset, version), automate "boot at state X, check, repeat."
9. **Differential loop.** Run the same input through old-version vs new-version and diff outputs.
10. **HITL bash script.** Last resort. If a human must click, use `scripts/hitl-loop.template.sh` so the loop is still structured.

Build the right feedback loop, and the bug is 90% fixed.

### Iterate on the loop itself

Treat the loop as a product. Can you make it faster? Sharper signal? More deterministic?

A 30-second flaky loop is barely better than no loop. A 2-second deterministic loop is a debugging superpower.

### Non-deterministic bugs

The goal is a higher reproduction rate. Loop the trigger 100x, parallelize, add stress, narrow timing windows, inject sleeps. A 50%-flake bug is debuggable; 1% is not. Keep raising the rate.

### When you genuinely cannot build a loop

Stop and say so explicitly. List what you tried. Ask for: (a) access to the reproducing environment, (b) a captured artifact (HAR file, log dump, core dump, screen recording), or (c) permission to add temporary instrumentation. Do not proceed to hypothesize without a loop.

## Phase 2: Reproduce

Run the loop. Watch the bug appear. Confirm:
- The loop produces the failure mode the user described, not a different nearby failure.
- The failure is reproducible across multiple runs.
- You have captured the exact symptom so later phases can verify the fix.

## Phase 3: Hypothesise

Generate 3-5 ranked hypotheses before testing any. Single-hypothesis generation anchors on the first plausible idea.

Each hypothesis must be falsifiable: "If X is the cause, then Y will make the bug disappear / worse."

**Interactive mode:** Show the ranked list to the user before testing. They often have domain knowledge that re-ranks instantly. Don't block on it; proceed with your ranking if the user is AFK.

**Autonomous mode (spawned as subagent):** Skip the user check. Proceed with your ranking directly.

## Phase 4: Instrument

Each probe must map to a specific prediction from Phase 3. Change one variable at a time.

Tool preference: debugger / REPL > targeted logs > "log everything and grep."

Tag every debug log with a unique prefix (e.g. `[DEBUG-a4f2]`). Cleanup is a single grep.

For performance regressions, logs are usually wrong. Establish a baseline measurement first, then bisect.

## Phase 5: Fix + Regression Test

Write the regression test before the fix, but only if there is a correct seam for it. A correct seam exercises the real bug pattern as it occurs at the call site.

If no correct seam exists, that itself is the finding. Note it. The codebase architecture is preventing the bug from being locked down.

If a correct seam exists: turn the repro into a failing test, watch it fail, apply the fix, watch it pass, re-run the Phase 1 loop against the original scenario.

## Phase 6: Cleanup + Post-Mortem

Required before declaring done:
- Original repro no longer reproduces.
- Regression test passes (or absence of seam is documented).
- All `[DEBUG-...]` instrumentation removed.
- Throwaway POC code deleted.
- The correct hypothesis is stated in the commit / PR message.

Then ask: what would have prevented this bug? If the answer involves architectural change (no good test seam, tangled callers, hidden coupling), hand off to `/thermo-nuclear-review` with the specifics. Make the recommendation after the fix is in. You have more information now than when you started.
