#!/usr/bin/env python3
"""Deny tmux commands that kill or reconfigure a server unless they name a private one.

The owner's live sessions, including most agents, run on the default tmux server.
`$TMUX` overrides `TMUX_TMPDIR`, so only `-L`/`-S` reliably avoids it. Read-only
tmux commands pass.

Sees through `VAR=` prefixes, wrappers (`env`, `sudo`, `timeout`, `xargs`, ...),
`$(...)`, backticks, tmux's own command chaining, and the command string of `sh|bash|zsh|dash -c`
and `eval`, recursively. Does not see commands built at runtime (`$T kill-server`,
`python3 -c "os.system(...)"`, scripts that call tmux): those need a different
control than a command-string check.

Input is the Claude Code hook JSON on stdin; Mars renders the same shape for the
other harnesses. To block it prints the reason to stderr and exits 2; otherwise it
exits 0 silently. Codex ignores the hook's `if`, so this script must decide.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import sys

DESTRUCTIVE = {
    "kill-server", "kill-session", "kill-window", "killw", "kill-pane", "killp",
    "source-file", "source",
    "respawn-pane", "respawnp", "respawn-window", "respawnw",
}
SET_COMMANDS = {"set-option", "set", "set-window-option", "setw", "set-environment", "setenv"}
WRAPPERS = {"env", "sudo", "command", "exec", "nohup", "time", "timeout", "nice", "stdbuf", "setsid", "xargs"}
WRAPPER_OPTS_WITH_ARG = {
    "-u", "-C", "-n", "-s", "-k", "--unset", "--chdir",  # env, sudo, timeout, nice
    "-I", "-P", "-L", "-E", "-d", "-a", "-J",  # xargs
}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "ash"}
# tmux global options that take a value
TMUX_VALUE_OPTS = set("cfLST")
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
SHELL_TOOLS = {"", "Bash", "Shell", "bash", "shell", "exec_command", "unified_exec", "commandExecution"}

REASON = (
    "Blocked: `tmux {name}` without -L/-S would act on the owner's default tmux server, "
    "which holds all their live sessions (likely including yours). $TMUX overrides "
    "TMUX_TMPDIR, so that does not isolate you. Run it on a private server instead: "
    "`tmux -L <your-spawn-id> ...`. Read-only commands (ls, list-panes, has-session) "
    "are fine on the default server."
)


def deny(reason: str) -> int:
    # Exit 2 with the reason on stderr is the blocking answer in every harness.
    print(reason, file=sys.stderr)
    return 2


def payload_command(payload: object) -> tuple[str, str]:
    if not isinstance(payload, dict):
        return "", ""
    tool_name = str(payload.get("tool_name") or payload.get("toolName") or "")
    for input_key in ("tool_input", "toolInput"):
        tool_input = payload.get(input_key)
        if isinstance(tool_input, dict):
            command = tool_input.get("command") or tool_input.get("cmd")
            if isinstance(command, str):
                return tool_name, command
    for command_key in ("command", "cmd"):
        command = payload.get(command_key)
        if isinstance(command, str):
            return tool_name, command
    return tool_name, ""


SEPARATORS = ("||", "&&", ";", "|", "&", "\n", "(", ")")


def split_unquoted(part: str):
    """Split on shell separators outside quotes, so `bash -c "a; tmux kill-server"` stays whole."""
    buf: list[str] = []
    quote = ""
    i = 0
    while i < len(part):
        ch = part[i]
        if ch == "\\" and quote != "'" and i + 1 < len(part):
            buf.append(part[i : i + 2])  # `\;` is tmux's own separator, not the shell's
            i += 2
            continue
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "'\"":
            quote = ch
        else:
            sep = next((s for s in SEPARATORS if part.startswith(s, i)), None)
            if sep:
                yield "".join(buf)
                buf = []
                i += len(sep)
                continue
        buf.append(ch)
        i += 1
    yield "".join(buf)


def segments(command: str):
    """Split a shell command into simple commands, including $(...) and `...` bodies."""
    inner = re.findall(r"\$\(([^()]*)\)|`([^`]*)`", command)
    for part in [command] + [a or b for a, b in inner]:
        for seg in split_unquoted(part):
            if seg.strip():
                yield seg


def argv_of(seg: str) -> list[str]:
    try:
        words = shlex.split(seg, comments=True)
    except ValueError:
        # Unbalanced quotes: check the raw words rather than skip the segment.
        words = seg.split()
    while words:
        w = words[0]
        if ASSIGN.match(w):
            words.pop(0)
        elif os.path.basename(w) in WRAPPERS:
            words.pop(0)
            # wrapper flags, their values, and bare timeout durations / nice levels
            while words and (
                words[0].startswith("-") or re.fullmatch(r"\d+[smhd]?", words[0]) or ASSIGN.match(words[0])
            ):
                flag = words.pop(0)
                if flag in WRAPPER_OPTS_WITH_ARG and words:
                    words.pop(0)
        else:
            break
    return words


def names_default_server(flag: str, value: str) -> bool:
    if flag == "L":
        return value in ("", "default")
    if not value:
        return True
    resolved = os.path.realpath(os.path.expanduser(value))
    defaults = {os.path.join(os.environ.get("TMUX_TMPDIR") or "/tmp", f"tmux-{os.getuid()}", "default")}
    tmux_env = os.environ.get("TMUX", "")
    if tmux_env:
        defaults.add(tmux_env.split(",", 1)[0])
    return resolved in {os.path.realpath(d) for d in defaults} or os.path.basename(resolved) == "default"


def violation(words: list[str]) -> str | None:
    if not words or os.path.basename(words[0]) != "tmux":
        return None
    private = False
    i = 1
    while i < len(words) and words[i].startswith("-") and words[i] != "--":
        letters = words[i][1:]
        for j, ch in enumerate(letters):
            if ch in TMUX_VALUE_OPTS:
                if j < len(letters) - 1:
                    value = letters[j + 1 :]
                else:
                    i += 1  # value is the next word
                    value = words[i] if i < len(words) else ""
                if ch in "LS":
                    # `-L default` and the default socket path name the shared server too
                    private = not names_default_server(ch, value)
                break
        i += 1
    if private:
        return None
    # tmux chains commands with ';' or '\;'; check every subcommand
    sub: list[str] = []
    subs = [sub]
    for w in words[i:]:
        if w in (";", "\\;"):
            sub = []
            subs.append(sub)
        else:
            sub.append(w)
    for sub in subs:
        if not sub:
            continue
        name = sub[0]
        if name in DESTRUCTIVE or (
            name in SET_COMMANDS and any(a.startswith("-") and "g" in a[1:] for a in sub[1:])
        ):
            return name
    return None


def inner_command(words: list[str]) -> str | None:
    """The command string a shell `-c` or `eval` will run, if `words` is one."""
    if not words:
        return None
    prog = os.path.basename(words[0])
    if prog == "eval":
        return " ".join(words[1:])
    if prog not in SHELLS:
        return None
    i = 1
    while i < len(words):
        w = words[i]
        if w in ("-o", "-O", "+o", "+O"):
            i += 2
        elif w.startswith("-") and not w.startswith("--") and "c" in w:
            return words[i + 1] if i + 1 < len(words) else None  # -c, -lc, -ec, ...
        elif w.startswith(("-", "+")):
            i += 1
        else:
            return None  # a script file: out of scope
    return None


def check(command: str) -> str | None:
    """Name of the first destructive tmux subcommand `command` would run, or None."""
    for seg in segments(command):
        words = argv_of(seg)
        name = violation(words)
        if name:
            return name
        inner = inner_command(words)
        name = check(inner) if inner else None  # inner is shorter than command, so this ends
        if name:
            return name
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool_name, command = payload_command(payload)
    if "tmux" not in command or tool_name not in SHELL_TOOLS:
        return 0
    name = check(command)
    if name:
        return deny(REASON.format(name=name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
