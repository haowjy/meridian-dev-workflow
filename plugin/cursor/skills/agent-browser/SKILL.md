---
name: agent-browser
description: 'Use when a task needs a live browser: scraping, extracting data or design tokens, filling forms, verifying frontend rendering and flows, capturing screenshots, or reproducing a UI bug. Accessibility-tree snapshots let you act on a page in a few hundred tokens instead of parsing HTML.'
metadata:
  type: reference
alwaysApply: false
---

# agent-browser

Fast browser automation CLI. Chrome/Chromium over CDP, accessibility-tree
snapshots with compact `@eN` refs: interact with a page in a few hundred
tokens instead of parsing HTML.

For specialized flows (dogfood, electron, slack, cloud sandboxes), load the
matching skill with `agent-browser skills get`.

Install once if the command is missing:

```bash
npm i -g agent-browser && agent-browser install   # add --with-deps on Linux
```

## Memory cap (Linux)

Run Chrome in its own capped scope so browser memory pressure cannot take down the agent.
One-time setup (replace `<agent-browser-skill>` with this skill’s installed path):

```bash
install -Dm755 <agent-browser-skill>/resources/capped-browser "$HOME/.local/bin/agent-browser-capped-browser"
# ~/.agent-browser/config.json — use your absolute home path, not `~`
{"executablePath":"/home/YOU/.local/bin/agent-browser-capped-browser"}
systemctl --user list-units 'agent-browser-*.scope'   # check while Chrome is open
```

## Core loop

```bash
agent-browser open https://example.com
agent-browser snapshot -i        # interactive elements only, with @eN refs
agent-browser click @e3          # act on a ref from the snapshot
agent-browser snapshot -i        # re-snapshot after any page change
agent-browser close
```

Refs (`@e1`, `@e2`, …) are reassigned on every snapshot and go **stale the
moment the page changes**: after navigation, submits, dynamic re-renders.
Always re-snapshot before the next ref interaction.

## Commands you reach for

```bash
# interact
agent-browser fill @e1 "user@example.com"
agent-browser type "query"; agent-browser press Enter
agent-browser select @e9 "value"; agent-browser check @e12; agent-browser hover @e4

# read
agent-browser get text @e5          # also: html | value | attr <name> | url | title
agent-browser snapshot              # full tree (omit -i)
agent-browser eval "document.title"

# capture
agent-browser screenshot out.png    # --full for full-page
agent-browser pdf out.pdf

# diagnose
agent-browser console               # console messages
agent-browser errors                # runtime/page errors   (--json on either)
agent-browser network requests      # also: network har
agent-browser react tree|inspect|renders   # React component detail
agent-browser vitals                # performance

# wait
agent-browser wait --load networkidle
```

## Sessions are shared

Other agents on the machine drive their own browser sessions through the same
daemon. Name yours with your run ID (the one your caller holds): use
`--session <run-id>-<task>` on every command, or set
`AGENT_BROWSER_SESSION`. Close only that one:
`agent-browser --session <name> close`. Never `close --all`: it ends every
other agent's browser mid-run.

Add `--json` for structured output to pipe elsewhere.

## Watch a session live

The dashboard is bundled into the binary (no install) and shows a live
viewport plus a command/console activity feed:

```bash
agent-browser dashboard start       # serves on :4848
agent-browser open https://example.com
```

Open `http://localhost:4848` (or a proxied URL like
`https://dashboard.agent-browser.localhost`). To watch from another device,
expose the port over tailscale when it's available:

```bash
tailscale serve 4848
```

## Going deeper

The binary serves docs matched to its installed version: load them when the
core surface isn't enough or a command behaves unexpectedly:

```bash
agent-browser skills get core --full    # full command reference + templates
agent-browser skills get dogfood        # exploratory testing / QA / bug hunts
agent-browser skills get electron       # desktop apps (VS Code, Slack, ...)
agent-browser skills get slack          # Slack workspace automation
agent-browser skills list               # everything on the installed version
```
