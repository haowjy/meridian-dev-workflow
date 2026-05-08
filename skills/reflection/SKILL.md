---
name: reflection
description: >
  Use before reporting results. Step back, review your own output as if
  evaluating someone else's work, fix what you find. Catches issues while
  context is still loaded, without a separate reviewer spawn.
model-invocable: true
---

# Reflection

Before reporting, review your own work. The goal is to catch what a
reviewer would catch, while you still have full context.

## The Loop

1. **Verify** — check your output against its acceptance criteria using
   whatever tools are available. For code: tests, linters, type checkers,
   build. For documents: re-read the requirements and check coverage.
2. **Reflect** — review your output as if evaluating someone else's work:
   - What did you intend to deliver that isn't there?
   - What did the brief ask for that you skipped or under-delivered?
   - What did you add that wasn't asked for?
   - Where did you break consistency with existing patterns or conventions?
3. **Fix** — address what you found. Don't just list problems.
4. **Re-verify** — check again after fixes.
5. **Report** — what you delivered, what you're unsure about, and any
   concerns you couldn't resolve yourself.
