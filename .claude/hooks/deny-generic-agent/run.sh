#!/bin/bash
# Deny generic Agent(subagent_type: "claude") spawns.
# Named agents (design-lead, tech-lead, etc.) are allowed.
# Captures the prompt, writes it to a temp file, and returns a
# ready-to-run meridian spawn command.

input=$(cat)

tool_name=$(echo "$input" | jq -r '.tool_name // ""')

if [ "$tool_name" != "Agent" ]; then
  exit 0
fi

subagent_type=$(echo "$input" | jq -r '.tool_input.subagent_type // ""')

if [ "$subagent_type" != "claude" ] && [ -n "$subagent_type" ]; then
  exit 0
fi

# Extract the prompt and description from the blocked Agent call
prompt=$(echo "$input" | jq -r '.tool_input.prompt // ""')
description=$(echo "$input" | jq -r '.tool_input.description // ""')

# Build the error message
msg="Blocked: generic Agent() spawn. This project uses meridian subagents."

# Write prompt to temp file if we have content
prompt_file=""
if [ -n "$prompt" ]; then
  prompt_dir="/tmp/meridian-$$"
  mkdir -p "$prompt_dir"

  # Generate a unique filename from the description or timestamp
  if [ -n "$description" ]; then
    slug=$(echo "$description" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//' | cut -c1-60)
  else
    slug="agent-prompt"
  fi
  prompt_file="$prompt_dir/${slug}.md"

  echo "$prompt" > "$prompt_file"
fi

# List available agents via meridian (dynamic mars inventory)
agents=""
if command -v meridian >/dev/null 2>&1; then
  agents=$(meridian spawn subagents 2>/dev/null | tr '\n' ', ' | sed 's/,$//')
fi

{
  echo "$msg"
  echo ""
  if [ -n "$prompt_file" ]; then
    echo "Prompt saved to: $prompt_file"
    echo ""
    echo "Run:"
    echo "  meridian spawn -a <agent> --prompt-file \"$prompt_file\" --bg"
    echo "  meridian spawn wait"
  else
    echo "Run:"
    echo "  meridian spawn -a <agent> \"<task>\" --bg"
    echo "  meridian spawn wait"
  fi
  if [ -n "$agents" ]; then
    echo ""
    echo "Available agents: $agents"
  fi
} >&2

exit 2
