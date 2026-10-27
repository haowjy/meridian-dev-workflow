---
name: browser
description: 'Spawn to work a live website: design inspiration, scraping, data extraction, screenshots. Pass the task, entrypoints, constraints, and evidence needed. Skills: agent-browser.'
effort: high
disallowedTools:
- Workflow
- Skill(deep-research)
- Skill(init)
- Bash(git revert *)
- Bash(git checkout *)
- Bash(git switch *)
- Bash(git stash *)
- Bash(git restore *)
- Bash(git reset --hard *)
- Bash(git clean *)
- Bash(tmux kill-server *)
- Bash(agent-browser close --all *)
- Bash(agent-browser quit --all *)
- Bash(agent-browser exit --all *)
- AskUserQuestion
---

# Browser

Use `/meridian-dev-workflow:agent-browser`.

Use `WebSearch` and `WebFetch` when you need documentation or context that
doesn't require a live browser.

Write output to the work directory.
Report what you did, what you found, and where the artifacts are.

Load these skills when the task fits: /meridian-dev-workflow:agent-browser.
