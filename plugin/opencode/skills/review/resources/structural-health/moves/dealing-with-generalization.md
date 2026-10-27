# Dealing With Generalization

Use these moves when an abstraction, hierarchy, or shared helper has captured
the wrong commonality.

## Typical Moves

- Inline abstraction that no longer pays for itself
- Split a hierarchy or helper into more honest boundaries
- Remove speculative hooks and unused extension points
- Replace inheritance with composition or explicit strategy where the domain
  wants different behavior, not a stretched base class

## When To Reach For Them

- Shared helpers that keep gaining flags and branches
- Base types that many children partly ignore
- Generic layers that mostly forward calls plus special cases
- Abstractions retained only because they once seemed future-proof

## What Good Looks Like

After refactoring, the abstraction should reflect a real shared concept. If the
shared concept does not exist, a simpler and more direct structure is better.
