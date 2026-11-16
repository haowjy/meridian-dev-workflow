---
name: work-artifacts
description: 'Load when work must survive compaction, crashes or a new session, or be shared with other agents: the work directory holds the current state, and what the work moved past is deleted.'
metadata:
  type: principle
---

# Work Artifacts

The work directory is the shared state between you, the user, and other
agents; what isn't on disk doesn't survive a crash, a compaction or a new
session. Keep the state you own current as you go, each decision with its
reason, the alternatives it beat and whether it is settled, and delete what
the work has moved past instead of logging it: the next session needs where
things stand, not how they got there. Commit where it is version-controlled. Source edits go in the source
checkout, not the work directory.

This work item's artifacts go in the work directory; project-wide reference
goes in the knowledge base. Keep raw files (traces, HARs, dumps, build output)
out of the work directory: record the excerpt that carries the finding.

The agent that started a work item owns its state; leave it alone unless
your brief says otherwise.

## Maintain the Work Directory

A work item carries one goal, stated as what is true when it is done. When the
work's goal shifts, update the goal: an item whose goal no longer matches its
work misleads every agent that reads it.

Give it an `AGENTS.md` that orients a delegated agent arriving cold: the goal, the artifact
layout, and what is settled versus still moving. Keep it current as the work
shifts, following `/meridian-dev-workflow:qi-layer`.

Decisions scoped to one change go with it, in its commit message or a note
beside what they explain; structural decisions go in the work directory. When
the plan shifts, update the plan and record the change as a decision with
its reason, so reviewers check the code against the plan as it stands.
