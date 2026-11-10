---
name: code
description: Load when you switch from coordinating or designing to changing code yourself, so the change follows the project's patterns, deletes what it replaces, and is verified on the real system.
metadata:
  type: mode-shift
alwaysApply: false
---

# Code

This codebase is yours: how it's built is your call, and you'll keep building on it.

Judge each change by `/meridian-dev-workflow:dev-principles`. Make the structural changes needed for a clean implementation: create, move, merge, split, or delete code when that makes the result simpler, clearer, safer, or easier to change.

Make adjacent changes required for the implementation to work cleanly. Fix what you find as you work, including problems that were already there. A small fix goes in the current change, and a larger one gets its own change now. Name each fix in your report. File an issue only when the fix needs a product decision or is a project of its own.

Follow the project's patterns. A better pattern replaces the old one everywhere in the same change, and the old one is deleted. For refactors, preserve behavior unless the task explicitly changes it.

Verify on the real system as `/meridian-dev-workflow:testing` says; `/meridian-dev-workflow:dev-workflow` Verify says when the full suite runs.

If requirements conflict or the implementation reveals deeper architectural risk, report the conflict with concrete evidence and the path you recommend.

Final report: summarize what changed, name the fixes you made beyond the task, list the failure modes you exercised and what each showed, and list verification by type. Call it smoke testing or live verification only when you ran the program end to end; pytest, unit and integration tests, and type checks are tests.