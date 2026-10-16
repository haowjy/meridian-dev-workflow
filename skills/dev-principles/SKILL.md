---
name: dev-principles
type: principle
description: "Load when implementing, reviewing, refactoring, or designing code: the engineering values every code decision is judged against."
model-invocable: true
---

# Dev Principles

## Core Beliefs

1. **Code is cheap; bad code is expensive.**  
   The real cost isn't writing code — it's the drag on every later change when code is inconsistent, bloated, or entangled. Spend the effort to keep code easy to change and delete.

2. **Consistency beats cleverness.**  
   Every novel pattern forces the next reader to learn a new dialect. Consistent patterns lower reasoning cost for humans and agents. Match what's there before inventing something new; a new idiom must be clearly worth its learning cost.

3. **Code is fluid.**  
   Requirements change; systems that resist change rot or get bypassed. Design clear seams, good boundaries, and minimal coupling so the next change is small and safe.

4. **Simplicity of the system, not of the change.**  
   Picking the smaller diff today accretes parallel mechanisms, ghost states, and compatibility layers — complexity compounds inside the system. Refactor and delete to reduce concepts, states, and moving parts, even when the diff is larger.

## Get It Right the First Time

The default agent failure is producing something plausible and moving on. The cost of wrong isn't one more generation; it's the mess every later agent inherits. Read the code before changing it. Follow the existing pattern before inventing one. Handle edge cases now. Investigate when unclear instead of guessing.

## Simplicity

Every boundary, type, and layer must earn its place by making future changes smaller and safer. The default failure mode is over-engineering: adding moving parts that don't create real independence.

Before adding a branch, flag, or mode for a new case, look for the model under which the case needs no special handling: a different owner, state model, or shared path.

Before adding structure: is this a separate concern, or one thing wearing two names? Things that always change together are one thing. Independence justifies a split; partitioning alone doesn't.

**Deep modules over shallow.** A deep module hides substantial complexity behind a simple interface. If an exported function wraps three lines, keep it in its caller. When 3+ shallow modules touch the same concept, bundle them into one deep module.

## Efficiency by Construction

Large efficiency bugs are rarely slow lines. They are a cost paid on every
event, or one that grows with accumulated state. On a hot path (per chunk,
per turn, per poll, per invocation), keep each run's cost proportional to
the work in front of it: write only what changed, poll with a cheap
check, process new events with only the prior state they need, and load only what this run uses.

A performance comparison is a claim. Before you report or act on one, name what
limits it and rule out errors, skipped work, and noise, per `/probe`'s
`resources/measurement.md`.

## Separation of Concerns

Group by concern; draw boundaries where things change independently. Smaller focused files cost less to read: an agent consumes the whole file, so a 500-line module with one relevant function wastes attention on the other 480.

When you see duplication across boundaries, suspect the boundaries before patching with extraction.

## Deletion

LLMs default to preserving code. Fight that. Dead code, stale imports, orphaned files: delete in the same change. When new code replaces old behavior, delete the old path in the same change instead of keeping it beside the new one as a fallback or compatibility layer, unless the repo's policy requires one. Obvious duplication: collapse it. Structural problems (circular dependencies, god modules, leaky abstractions): fix on sight. Rot compounds at agent speed.

## Comments

Comment what the code can't show: a hidden constraint, a surprising invariant, an external quirk, a race the code avoids. Put design rationale longer than a few lines in the directory's `.context/`, and the story of a change in its commit message. Let names and module boundaries carry structure, in place of section banners and comments that narrate the next line.

## Testing

Verify by listing how the change could fail and checking each failure on the running program, plus the existing tests that cover what you touched. A new automated test is the exception: load `/testing` before writing one, and write it only for a case it admits. As a delegated worker, write only the tests your brief names and report other candidates to your caller.

## Consistency

Read surrounding code first. Does the project already solve this? Prefer its patterns over introducing new ones. A good dependency deletes more code than it adds.
