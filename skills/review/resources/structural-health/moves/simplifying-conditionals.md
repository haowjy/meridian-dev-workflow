# Simplifying Conditionals

Use these moves when the same distinction is expressed with repeated branching
or when one conditional tree is doing too much conceptual work.

## Typical Moves

- Consolidate repeated branching behind one boundary
- Decompose complex conditionals into named predicates or owned policies
- Separate compatibility logic from normal logic
- Replace conditional sprawl with clearer dispatch when one concept truly owns
  the variation

## When To Reach For Them

- Repeated `if` or `match` trees for the same mode or type distinction
- Compatibility logic mixed into business logic
- Long conditionals encoding policy that has no named owner

## What Good Looks Like

After refactoring, one place should own the distinction, and callers should not
have to restate it in parallel.
