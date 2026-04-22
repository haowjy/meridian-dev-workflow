---
name: context-handoffs
description: Context scoping for agent spawns — use when deciding what context a spawned agent should receive, whether ephemeral reasoning should be materialized before handoff, and how much to pass. Poor context handoffs are the #1 cause of wasted agent work.
---

# Context Handoffs

- `/meridian-spawn` covers command mechanics.
- This skill covers scoping judgment.

## Choose Mechanism

- `-f`: default. Folders for structure, specific files for content.
- `--from`: use for reasoning/history not yet materialized. Takes a spawn id for predecessor reasoning, or `$MERIDIAN_CHAT_ID` to pull the top-level primary session — the root conversation at the top of the chat tree, available at any spawn depth.
- Materialize first when context is critical.

```bash
# Good: folder for map, specific files for content
meridian spawn -a coder -p "Implement auth middleware" \
  -f src/middleware/ \
  -f src/middleware/base.py \
  -f <work_dir>/phase-2.md

# Bad: broad dump
meridian spawn -a coder -p "Implement auth middleware" \
  -f <work_dir>/*.md -f src/**/*.py
```

```bash
# Good: reasoning context from prior spawn
meridian spawn -a reviewer --from p203 -p "Review against design intent"

# Top-level conversation gives framing; files still supply scope
meridian spawn -a coder \
  --from $MERIDIAN_CHAT_ID \
  -f plan/phase-2.md \
  -f src/auth/ \
  -p "Implement phase 2 per the approach discussed at the primary"

# Materialize critical reasoning before spawn
meridian spawn -a coder -p "Implement event store" -f <work_dir>/approach.md
```

## Scope Tightly

- Pass overview plus task-specific files.
- Typical: 2-4 files.
- Six is heavy. Ten means poor handoff.
- Point to where more context lives instead of attaching everything.
- Prompt should name concrete files/sections and expected behavior.

## Cross-Phase Handoff

```bash
meridian spawn -a coder \
  --from p301 \
  -f src/auth/ \
  -f src/auth/tokens.py \
  -f <work_dir>/phase-2.md \
  -p "Implement token refresh, building on phase 1 token validation"
```

- Use `--from` for predecessor reasoning.
- Use `-f` folders for structure, specific files for content.
