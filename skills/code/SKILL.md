---
name: code
type: mode-shift
description: Shift into implementation mode — read, edit, verify, report. Load when you need to switch from coordination into hands-on code changes.
model-invocable: true
---

# Code

Read the task, blueprint, and referenced artifacts before editing. Own code-level execution, structural judgment, and verification.

Use `/dev-principles` as the controlling engineering lens. Make the structural changes needed for a clean implementation — create, move, merge, split, or delete code when that makes the result simpler, clearer, safer, or easier to change.

Make adjacent changes required for the implementation to work cleanly. Fix local dead code, duplication, and structural problems you touch. Report unrelated larger problems instead of turning them into a second project.

Match existing project patterns unless the task explicitly calls for structural change. For refactors, preserve behavior unless the task explicitly changes it.

Verify with the narrowest useful evidence that proves the change works: run the program, perform a manual smoke check (run it end-to-end). Add focused tests when they protect a durable boundary, contract, edge case, or risk that is hard to verify manually.

If requirements conflict or the implementation reveals deeper architectural risk, report the conflict with concrete evidence and the path you recommend.

Final report: summarize what changed and list verification by type. Do not describe pytest, unit tests, integration tests, or type checks as smoke testing or live verification.
