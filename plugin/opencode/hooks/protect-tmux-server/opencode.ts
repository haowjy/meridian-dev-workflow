import { spawnSync } from "node:child_process"

// Runs the shared rule set (run.sh -> run.py) on a shell command. Returns the
// denial reason, or null to allow. If the script cannot run, fail closed only
// for commands that mention tmux, as the Claude and Codex hooks do.
const SCRIPT = "${MARS_HOOK_DIR}/run.sh"

function denial(command: string): string | null {
  const run = spawnSync("bash", [SCRIPT], {
    input: JSON.stringify({ tool_name: "Bash", tool_input: { command } }),
    encoding: "utf8",
    timeout: 5000,
  })
  if (run.error || run.status !== 0) {
    return command.includes("tmux")
      ? "Blocked: the tmux guard could not run. Name a private server with `tmux -L <name> ...`, or ask the user."
      : null
  }
  try {
    const out = JSON.parse(run.stdout.trim() || "{}").hookSpecificOutput
    return out?.permissionDecision === "deny" ? String(out.permissionDecisionReason) : null
  } catch {
    return null
  }
}

export default {
  id: "protect-tmux-server",
  async setup(ctx: any) {
    await ctx.tool.hook("execute.before", (e: any) => {
      const command = e?.input?.command
      // OpenCode 2.x names the shell tool "shell"; 1.x called it "bash".
      if (!["shell", "bash"].includes(String(e?.tool).toLowerCase()) || typeof command !== "string") return
      if (!command.includes("tmux")) return // run.py allows these too; skip spawning it per shell call
      const reason = denial(command)
      if (reason) throw new Error(reason)
    })
  },
}
