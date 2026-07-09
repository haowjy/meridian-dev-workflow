# Redesign Escalation

When to say frame-rot instead of filing another round of findings, and how
to write the escalation so the orchestrator can act on it. The escalation
shape below is the **Redesign Brief** — the same format whether a reviewer
escalates frame-rot or an implementation lead escalates a seam that won't
converge.

## Signals That Patching Won't Converge

One of these is a smell; several pointing at the same seam is frame-rot.

- **Fixes accumulate special cases.** Each fix adds a branch, flag, or
  exception at the same boundary instead of simplifying it.
- **Findings regenerate.** New findings appear at the same rate fixes close
  them, and they cluster around one component or seam.
- **Shotgun fixes.** A conceptually small fix keeps touching many files —
  the responsibility lives in the wrong place.
- **The invariant can't be stated.** Nobody can say in one sentence what the
  component guarantees; the code enforces fragments of several guesses.
- **Tests fight the structure.** Every test of the area needs heavy mocking
  of the same dependency, or asserts implementation details because the
  behavior has no clean surface.
- **The design doc no longer describes the code.** `DIVERGENCE/` entries pile
  up in one area, each one bending the plan a little further.

## The Redesign Brief

The receiver needs enough to route a redesign, not a full design. Open by
classifying the problem — **design-problem** (the design itself is wrong;
routes to a design lead) or **scope-problem** (the requirements shifted;
routes to whoever owns them) — then four parts, one paragraph each:

1. **The structural problem.** What is wrong with the frame — not the
   symptoms, the shape. Use `/architecture` vocabulary: the misplaced
   boundary, the wrong ownership split, the missing seam.
2. **Evidence.** The findings that share this root, cited. This is what
   separates a frame-rot verdict from a hunch.
3. **Recommended direction.** Where the boundary should be instead, or which
   alternative the design already rejected that now looks right. A direction,
   not a spec.
4. **What survives.** The parts of the current implementation a redesign can
   keep. Redesign is not restart; say what's salvageable.
