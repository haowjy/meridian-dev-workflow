---
name: handoff
description: 'Use when work belongs to a new interactive lead the user will steer, or your own work needs a fresh session: writes the new session''s opening brief, runs applicable pre-phase checks, and has the user start it.'
metadata:
  type: mode-shift
alwaysApply: false
---

# Handoff

Start a new interactive lead on a piece of work. Usually you keep working
alongside it; you stop only when it takes over your own work. Treat an
argument as the requested lead or focus; otherwise infer both from the work.

## Write the Brief

The brief is the new lead's opening prompt, read without this conversation.
Start with `/meridian-dev-workflow:intent-modeling`, then give the lead:

- The goal: what is true when its work is done
- What it now owns, and what stays with you
- Current state, decisions with their reasons, and open questions
- The artifact paths to read first

Keep artifact content in its files and point to them.

## Run Pre-* Checks

Check for `pre-*` checkpoint skills that apply to the new lead's work, such as
`pre-dev` before implementation. Load and run each one so the lead starts with
its prerequisites ready.

## Hand Off

Give the user the chosen lead and the exact path to the brief; the user starts
the new session. What the brief handed over is the new lead's to change; keep
to what stays with you.
