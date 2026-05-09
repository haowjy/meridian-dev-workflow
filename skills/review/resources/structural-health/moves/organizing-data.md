# Organizing Data

Use these moves when loose primitives or repeated bundles of fields are standing
in for a better concept boundary.

## Typical Moves

- Introduce parameter object
- Introduce value object
- Replace primitive codes with domain-specific structure where justified
- Normalize scattered shape handling behind one boundary

## When To Reach For Them

- Data clumps passed through several calls
- Long parameter lists
- Repeated validation or normalization for the same bundle of values
- Behavior split awkwardly because the data concept has no home

## What Good Looks Like

After refactoring, the data boundary should communicate intent, reduce argument
noise, and give behavior a more obvious home.
