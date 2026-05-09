# OO Abusers

These patterns force object-oriented or generalized structure into shapes that
the actual domain does not support.

## Common Patterns

- Repeated switching on type or mode
- Refused bequest or inheritance that does not fit
- Alternative classes or hierarchies doing nearly the same thing with awkward
  specialization

## Why They Hurt

The abstraction boundary no longer matches the true variation. New cases require
threading conditionals everywhere or contorting subclasses that do not want the
shared contract.

## Review Signals

- The same `if` or `match` distinction appears in many places.
- Subclasses override or ignore most of the base behavior.
- A supposedly shared hierarchy keeps adding exceptions and one-off hooks.

## Typical Moves

- Replace repeated switching with one owned variation boundary
- Push behavior down or pull shared behavior up only where it truly belongs
- Split a hierarchy that captured the wrong commonality
- Prefer composition or explicit strategy boundaries over awkward inheritance

## False Positives

Not every conditional is a smell. It becomes one when the same distinction is
repeated across the codebase or when the hierarchy is actively resisting the
domain.
