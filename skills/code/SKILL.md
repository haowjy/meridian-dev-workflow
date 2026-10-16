---
name: code
type: mode-shift
description: "Load when you switch from coordinating or designing to changing code yourself, so the change follows the project's patterns, deletes what it replaces, and is verified on the real system."
model-invocable: true
---

# Code

Read referenced artifacts and the task context before editing.

Use `/dev-principles` as the controlling engineering lens. Make the structural changes needed for a clean implementation: create, move, merge, split, or delete code when that makes the result simpler, clearer, safer, or easier to change.

Make adjacent changes required for the implementation to work cleanly. Fix local dead code, duplication, and structural problems you touch. Report unrelated larger problems instead of turning them into a second project.

Match existing project patterns or make new patterns and delete the old ones unless the task explicitly calls for structural change. For refactors, preserve behavior unless the task explicitly changes it.

Verify on the real system. List the ways the change could fail: bad input, partial failure, ordering and concurrency, stale state, and the callers and seams it touches. Check each one by running the program end to end; for an edge the running program can't reach cheaply, use an existing test, and report any failure mode you left unverified. Run the existing tests that cover the code you touched; the full suite belongs to the merge or ship gate. Write new tests only when your brief names them.

If requirements conflict or the implementation reveals deeper architectural risk, report the conflict with concrete evidence and the path you recommend.

Final report: summarize what changed, list the failure modes you exercised and what each showed, and list verification by type. Call it smoke testing or live verification only when you ran the program end to end; pytest, unit and integration tests, and type checks are tests.