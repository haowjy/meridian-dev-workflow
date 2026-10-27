# Change Preventers

These patterns make the next feature or fix fan out across too much code.

## Common Patterns

- Divergent change
- Shotgun surgery
- Parallel inheritance or mirrored branching hierarchies

## Why They Hurt

They broaden the change surface. One concept no longer has one obvious home, so
each new case requires a checklist of coordinated edits. This is especially
dangerous for agents because partial updates become much more likely.

## Review Signals

- One concept requires edits in many files every time it changes.
- One module absorbs unrelated changes from several feature streams.
- New variants require touching several parallel structures in lockstep.

## Typical Moves

- Re-home behavior so one concept owns one kind of change
- Consolidate repeated branching behind one boundary
- Break apart modules that change for unrelated reasons
- Collapse parallel structures if one boundary can own the variation

## False Positives

Some cross-file changes are normal at integration boundaries. The smell appears
when the fan-out is recurring and structural, not when one legitimate cross-cut
touches a few well-separated seams.
