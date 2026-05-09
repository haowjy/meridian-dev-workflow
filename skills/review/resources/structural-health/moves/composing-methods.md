# Composing Methods

Use these moves when a routine is doing too much or its phases are blended
together.

## Typical Moves

- Extract function for coherent substeps
- Split phase when one routine mixes separate transformations
- Replace temporary variables with clearer named steps where appropriate
- Make hidden policy steps explicit

## When To Reach For Them

- Long functions with several conceptual stages
- Repeated local logic that is truly the same
- A routine whose control flow hides the real story of the computation

## What Good Looks Like

After the refactor, the main flow should read as a sequence of meaningful steps,
and helper boundaries should expose the real concepts rather than merely slicing
by line count.
