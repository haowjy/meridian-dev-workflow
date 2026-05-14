# Testers

Different testers cover different failure modes. Coders self-verify (tests, lints, type checks) via `/reflection` before reporting — that's the baseline. Beyond that, match testing to what the phase touches.

Testers are not limited to the @coder's described checks. Generate independent edge cases, failure modes, and boundary-condition probes based on the change itself.

## Default Lanes

@smoke-tester — default for any phase touching process boundaries, state initialization, CLI behavior, IPC, or fresh-state workflows. Unit tests and type checks verify internal correctness, but orchestration bugs — process lifecycle, file locking, IPC, fresh-state initialization — only surface when real processes run in real environments. These are exactly the bugs that ship to users because "all tests passed." When the honest test requires a temp repo, temp config, temp server, or tiny helper script, the @smoke-tester should build it in a disposable scratch environment and prove the workflow end-to-end. Do not stop at the happy path — smoke-test realistic edge cases and failure paths as a default lane. **For integration phases** (code that talks to external binaries, APIs, or wire protocols), smoke testing is a mandatory behavioral lane. Pair it with other lanes when contract, structural, or design risks remain. Run against the real external system and test every supported target, not just one. Explicitly report which targets were tested and which were not.

@browser-tester — default for any phase touching frontend behavior. The frontend equivalent of @smoke-tester — verifies that UI changes actually work in a real browser, not just that component tests pass. Uses `playwright-cli` for browser interaction — snapshot-driven navigation, form filling, screenshotting, console/network inspection. Visual correctness, user flows, form interactions, console errors, and accessibility. When the honest test requires fresh state, a stub API, or a temp config, build it rather than testing against whatever happens to be running. Use `playwright-cli show --annotate` when the user should see and interact with the browser directly.

`@coder --skills unit-test,testing-principles` — for tricky logic, edge cases, and regression guards. Isolated, fast, exhaustive on boundary conditions. Not every phase needs new unit tests — but when there's complex pure logic that's hard to verify end-to-end, targeted unit tests pin down the behavior. Generate edge cases independently; don't only codify claimed EARS statements handed over by the coder.

`@coder --skills integration-test,testing-principles` — the middle tier between unit and smoke. Tests that internal components compose correctly — module boundaries, coordination logic, contracts between collaborators — with fakes at external system boundaries. Use when a phase introduces new interfaces, protocols, or state machines where the composition matters more than the isolated logic. Not the right fit for pure logic (use unit-test) or real runtime behavior against live systems (smoke-tester).

**Test retention during implementation:** Disposable probes and test harnesses
(scratch scripts, one-off verification fixtures) are removed after verification
passes. Durable unit and integration tests that protect key behavior or
interfaces stay — tech-lead judges which tests earn their place in the
permanent suite. @qa-lead is a specialist escalation for complex test-suite
structural work.

## Situational
