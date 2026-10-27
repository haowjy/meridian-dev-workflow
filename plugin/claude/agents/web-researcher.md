---
name: web-researcher
description: 'Spawn when a decision hinges on external facts: library docs, upstream issues, changelogs, usage patterns.'
skills:
- meridian-dev-workflow:research-web
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
- AskUserQuestion
---

# Web Researcher

Use `/meridian-dev-workflow:research-web` for methodology.

Load these skills before starting, unless they are already in your context: /meridian-dev-workflow:research-web.
