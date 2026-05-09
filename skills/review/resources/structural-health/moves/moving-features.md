# Moving Features

Use these moves when behavior lives far from the concept it mostly serves.

## Typical Moves

- Move function
- Move field
- Introduce a clearer owner for a cross-cutting concept
- Hide delegate or shorten traversal chains

## When To Reach For Them

- Feature envy
- Message chains
- Policy implemented in callers instead of in the owning concept
- Two modules that co-evolve because one owns data and the other owns logic

## What Good Looks Like

After the move, the concept should own its own policy, and callers should need
less knowledge of internal structure to get work done.
