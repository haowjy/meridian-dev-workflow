# Bloaters

Bloaters are structures that became too large to scan, understand, or modify
safely.

## Common Patterns

- Long function
- Large class or module
- Long parameter list
- Data clumps

## Why They Hurt

Oversized structure hides where a concept begins and ends. It mixes unrelated
responsibilities, increases the amount of context needed for a safe change, and
makes it hard for agents to identify the smallest correct edit.

## Review Signals

- One routine mixes validation, transformation, policy, IO, and error handling.
- One class changes for unrelated reasons.
- The same set of values travels together repeatedly.
- Callers need many parameters because the surrounding concept boundary is weak.

## Typical Moves

- Extract function
- Extract module or class
- Introduce parameter object or value object
- Split phase so distinct transformations become explicit

## False Positives

Do not report size alone. A large module can be acceptable when it is still
cohesive and changes for one reason.
