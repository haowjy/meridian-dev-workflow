# Architecture Review

Think about whether this code will be easy to change next month, or whether it's creating obligations for the future.

## Design Alignment

If there's a design doc, check for drift:

- Does the implementation match the intended approach? Silent divergence from the design is worse than an explicit decision to change direction — the first creates confusion, the second is recorded.
- Does this phase set up the next one correctly, or paint it into a corner?
- Are the scope boundaries respected? Scope creep in implementation is common and often invisible until review.

## Module Structure

- **Independence** — Do the things on either side of this boundary actually
  change independently? If they always change together, the boundary is
  ceremony. If they can't be understood without each other, they're entangled.
- **Dependencies** — Does this create circular dependencies or tightly couple
  modules that should be independent? Can you change one without changing the
  other?
- **Interfaces and contracts** — Are the boundaries between modules clear? Is
  it obvious what each module expects and guarantees? Are contracts enforced
  (types, validation) or just documented?
- **Abstraction cost** — Is this abstraction earning its keep? Every layer adds
  context you must load to understand a change. Too many layers and you spend
  more time navigating than thinking.

## Common Patterns to Look For

**Leaky abstractions** — An abstraction that forces callers to understand implementation details. If you need to know how it works internally to use it correctly, the abstraction isn't working.

**God objects** — Classes or modules that accumulate unrelated concerns over
time. They're easy to add to and hard to disentangle. Look for classes that
change for multiple independent reasons.

**Premature generalization** — Abstractions built for hypothetical future use
cases. Extra indirection has a real cost. Is this abstraction earning its
keep now, or is it speculative?

**Missing error propagation** — Errors swallowed silently, logged but not returned, or wrapped so many times the original cause is lost.

**Convention breaks** — The codebase has patterns. New code that introduces different patterns (different naming, different error handling, different module structure) creates cognitive load for everyone who reads it later. Unless the new pattern is clearly better and the old one is being migrated, match what's there.

## What Good Looks Like

An architecture finding should explain the consequence, not label a
violation. "This class handles both parsing and validation, which means
changes to the input format will require touching validation logic too —
separating them would let each change independently" is useful. "This is
too coupled" is not.
