# Review Translation

Turn structural observations into findings that another agent can act on.

## Finding Shape

For each finding, answer:

- **What is wrong?** Name the structural pattern and the concrete sites.
- **Why does it matter?** Explain how it broadens future change, hides the real
  concept, or increases regression risk.
- **What move should improve it?** Recommend the smallest useful
  behavior-preserving refactoring direction.
- **How severe is it?** Judge by the cost and risk it imposes on future work.

## Good Structural Finding

Good:
- "Adding a new provider now requires edits in five files because provider
  selection is implemented with repeated branching in each adapter. Consolidate
  provider dispatch behind one boundary so new cases land in one place."

Bad:
- "This area feels messy and could be simplified."

## Severity Heuristics

- **High** when the problem broadens nearly every change in the area, preserves
  misleading legacy structure, or strongly increases odds of incomplete edits.
- **Medium** when the problem is local but recurring and already imposing extra
  change cost.
- **Low** when the issue is real but mostly contained and not yet distorting
  normal work.

## Fix Direction Guidance

Prefer concrete structural moves:

- extract function or module
- move function or field
- rename to expose the real concept
- introduce a value object or parameter object
- isolate compatibility logic
- inline or split a bad abstraction
- replace repeated branching with a better boundary

Avoid redesign slogans such as "clean this up" or "use better architecture."
