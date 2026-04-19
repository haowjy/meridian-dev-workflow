# Dispensables

Dispensables are structures that add clutter, indirection, or maintenance cost
without paying for themselves.

## Common Patterns

- Dead code
- Lazy element or middle man
- Speculative generality
- Temporary field or scaffolding that outlived its purpose

## Why They Hurt

They obscure the real code path and waste attention. Agents have to consider
possibilities that are no longer relevant, which weakens discoverability and
raises the chance of editing around obsolete structure instead of simplifying it.

## Review Signals

- Unused or barely used code with no clear contract
- Abstractions that mostly forward calls without meaningful boundary value
- Optional machinery introduced "for the future" that no real path uses
- Deprecated logic with no exit condition

## Typical Moves

- Delete dead code
- Inline low-value indirection
- Remove speculative hooks that never matured into a real variation
- Isolate and mark remaining compatibility paths

## False Positives

Code that looks idle can still carry a real external contract or side effect.
When in doubt, identify the real constraint first, then simplify the structure
that carries it.
