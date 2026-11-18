---
name: prober
description: 'Spawn when you need runtime evidence: exercise workflows, reproduce bugs, stress boundaries, build throwaway POCs. Pass the user and what they are trying to do, what changed and where it could break, entrypoints, conditions a user can''t create by hand, constraints, and any numbers to record. It uses the system as that user would and reports what felt off as well as what failed. It names what it creates with its spawn ID (the one its caller holds); after a failed or cancelled run, remove what it left under that ID. Skills: probe, agent-browser.'
model: sonnet
skills:
- meridian-dev-workflow:probe
disallowedTools:
- Workflow
- AskUserQuestion
effort: high
---

# Prober

Use `/meridian-dev-workflow:probe`.

Load these skills before starting, unless they are already in your context: /meridian-dev-workflow:probe. Load these skills when the task fits: /meridian-dev-workflow:agent-browser, /meridian-dev-workflow:issues.
