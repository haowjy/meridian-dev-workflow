---
name: dev-principles
type: principle
description: Core engineering values for all code decisions. Load when implementing, reviewing, refactoring, or designing code changes.
model-invocable: true
---

# Dev Principles

## Core Beliefs

1. **Code is cheap; bad code is expensive.** The real cost is code that's hard to change: inconsistent, bloated, entangled. Optimize for the cost that's real.
2. **Consistency beats cleverness.** Consistent patterns lower reasoning cost for every human and agent that follows. Match what's there before inventing something new.
3. **Code is fluid.** Optimize for change: clear seams, good boundaries, minimal coupling. The next change should be easy to make.

## Get It Right the First Time

The default agent failure is producing something plausible and moving on. The cost of wrong isn't one more generation; it's the mess every later agent inherits. Read the code before changing it. Follow the existing pattern before inventing one. Handle edge cases now. Investigate when unclear instead of guessing.

## Simplicity

Every boundary, type, and layer must earn its place by making future changes smaller and safer. The default failure mode is over-engineering.

Before adding structure: is this a separate concern, or one thing wearing two names? Things that always change together are one thing. Independence justifies a split; partitioning alone doesn't.

**Deep modules over shallow.** A deep module hides substantial complexity behind a simple interface. If an exported function wraps three lines, keep it in its caller. When 3+ shallow modules touch the same concept, bundle them into one deep module.

## Separation of Concerns

Group by concern; draw boundaries where things change independently. Smaller focused files cost less to read: an agent consumes the whole file, so a 500-line module with one relevant function wastes attention on the other 480.

When you see duplication across boundaries, suspect the boundaries before patching with extraction.

## Deletion

LLMs default to preserving code. Fight that. Dead code, stale imports, orphaned files: delete in the same change. Obvious duplication: collapse it. Structural problems (circular dependencies, god modules, leaky abstractions): fix on sight. Rot compounds at agent speed.

## Testing

Verify by running the program and the project's checks. Automated tests earn their place by protecting a durable boundary, contract, or risk that's hard to verify by running the system. See `/testing` for tier judgment.

## Consistency

Read surrounding code first. Does the project already solve this? Prefer its patterns over introducing new ones. A good dependency deletes more code than it adds.
