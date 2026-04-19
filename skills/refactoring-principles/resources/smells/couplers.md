# Couplers

Couplers are patterns where modules know too much about each other or behavior
lives far from the concept it mostly serves.

## Common Patterns

- Feature envy
- Message chains
- Inappropriate intimacy
- Excessive indirection between caller and real behavior

## Why They Hurt

Bad locality means the correct edit site is no longer obvious. The agent has to
chase chains or read across several modules to understand one behavior, which
slows work and increases the risk of incomplete reasoning.

## Review Signals

- A function mostly manipulates another object's data.
- Callers repeatedly traverse several layers to do one thing.
- Two modules know each other's internals and co-evolve implicitly.
- A wrapper exists mainly to bounce calls elsewhere with little added value.

## Typical Moves

- Move function or field
- Hide delegate or reduce traversal depth
- Extract a clearer boundary or ownership point
- Inline low-value middle layers

## False Positives

A wrapper can be load-bearing when it centralizes auth, tracing, retries,
normalization, or protocol adaptation. Do not remove it unless the real value is
absent.
