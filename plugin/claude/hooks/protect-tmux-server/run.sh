#!/bin/bash
# Shell wrapper because Mars executes hook scripts with bash.
set -euo pipefail

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

if ! command -v python3 >/dev/null 2>&1; then
  # Fail closed only for commands that mention tmux; blocking every shell call
  # on a machine without python3 would make the agent unusable.
  payload=$(cat)
  case "$payload" in
    *tmux*)
      echo 'Blocked: python3 is required to check this tmux command. Name a private server with `tmux -L <name> ...` and install python3, or ask the user.' >&2
      exit 2
      ;;
  esac
  exit 0
fi

exec python3 -I "$script_dir/run.py"
