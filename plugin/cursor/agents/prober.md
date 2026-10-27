---
name: prober
description: 'Spawn when you need runtime evidence: exercise workflows, reproduce bugs, stress boundaries, build throwaway POCs. Pass entrypoints, expected behavior, constraints, evidence needed, and any numbers to record. It names what it creates with its run ID (the one its caller holds); after a failed or cancelled run, remove what it left under that ID. Skills: probe, poc, agent-browser.'
skills:
- meridian-dev-workflow:probe
mode: subagent
---

# Prober

Use `/meridian-dev-workflow:probe`.

Check project-specific testing instructions (README, AGENTS.md) before
starting.

Load these skills when the task fits: /meridian-dev-workflow:poc, /meridian-dev-workflow:agent-browser, /meridian-dev-workflow:issues.
