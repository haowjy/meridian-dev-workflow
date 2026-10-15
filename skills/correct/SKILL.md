---
name: correct
type: mode-shift
description: "Use when the human wants the mistakes agents keep repeating fixed for good. Works the KB corrections register: fixes each recurring class at the highest level that holds (architecture, types, a lint, a test, docs last), proves each check catches a real past mistake, and updates the register."
user-invocable: true
argument-hint: "A correction or class to start from (optional)"
model-invocable: false
---

# Correct

The human keeps correcting agents for the same mistakes. Change the code or
the prompts so the next agent can't make them.

Assume every contributor is an agent that sees only the files it opened,
copies the nearest example, and takes the shortest path that works. Design so
a change that looks right from one file is right for the whole system.

## Find the Classes

Start from the KB corrections register (`/knowledge-layers`
`resources/corrections/`; `code.md` says how to record enforcement) and any
correction the human just gave. Add what the register missed: mine recent sessions with `@session-miner`, and read
recent reverts and review findings. A class counts once it has happened
twice; record a single occurrence as a candidate.

## Fix Each Class at the Highest Level That Holds

1. **Architecture.** Give each piece of state one owner and each task one
   supported way. Hide internals so the wrong import fails. Replace
   hand-synced lists with one source of truth. Delete the old way and the
   dead code an agent would copy.
2. **Types**, so the bad state can't be written.
3. **A lint or CI check** whose error names the file, type, or function to
   use instead. Where the pattern is already common, fail only on additions.
4. **A test of the behavior.** Fix or delete any test that still passes when
   that behavior breaks, or fails when only internals change.
5. **A permission** in the agent profile, for a class of agent behavior a
   tool rule can block (a denied command, a read-only tool set).
6. **Docs or a prompt rule, last**, for judgment calls nothing can check. Put
   the rule where the agent reads it at the moment of choice: the nearest
   `AGENTS.md`, or the skill or agent prompt that governs that step, edited
   in its source package with `/prompt-principles`.

## Fix and Prove

Fix the most frequent classes first, one commit each. Prove each new check
fails on a real past mistake: replay the change that made it and show the
error. Run the check the same way locally and in CI. An exception goes on
the offending line with a reason and the human's approval.

## Update the Register

Set each class's **Enforced by** to what now catches it. Delete a row once
its mistake can no longer happen. A class enforced only by a doc that recurs
moves up a level in the same change.

## Report

Each class with its evidence, the level you picked, and why a higher level
didn't work.
