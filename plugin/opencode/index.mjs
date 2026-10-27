import { readFile } from "node:fs/promises"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"

const DATA = {
  "plugin": "meridian-dev-workflow",
  "skills": [
    {
      "directory": "agent-browser",
      "name": "agent-browser",
      "description": "Use when a task needs a live browser: scraping, extracting data or design tokens, filling forms, verifying frontend rendering and flows, capturing screenshots, or reproducing a UI bug. Accessibility-tree snapshots let you act on a page in a few hundred tokens instead of parsing HTML."
    },
    {
      "directory": "agent-staffing",
      "name": "agent-staffing",
      "description": "Load before you spawn a worker or a reviewer: which agent for which work, the review lanes a change needs, and when a model change is justified."
    },
    {
      "directory": "anti-slop",
      "name": "anti-slop",
      "description": "Load for any frontend work: catches AI-generated UI tells, the defaults that show up regardless of the brief."
    },
    {
      "directory": "architecture",
      "name": "architecture",
      "description": "Load when a decision places a boundary, a dependency direction, or a data model, or when a design needs settling: entanglement, tradeoff dimensions, structural risk."
    },
    {
      "directory": "code",
      "name": "code",
      "description": "Load when you switch from coordinating or designing to changing code yourself, so the change follows the project's patterns, deletes what it replaces, and is verified on the real system."
    },
    {
      "directory": "correct",
      "name": "correct",
      "description": "Use when the human wants the mistakes agents keep repeating fixed for good. Works the KB corrections register: fixes each recurring class at the strongest level that holds (remove the wrong way, an automated check, a tool permission, a written rule last), proves each fix on a real past mistake, and updates the register."
    },
    {
      "directory": "design-analysis",
      "name": "design-analysis",
      "description": "Load when gathered findings and requirements need turning into a design analysis, so the decision rests on challenged assumptions and compared options rather than the first idea."
    },
    {
      "directory": "design-craft",
      "name": "design-craft",
      "description": "Load when making production visual decisions (color, typography, layout, motion, interaction), so each choice is deliberate rather than a default."
    },
    {
      "directory": "dev-principles",
      "name": "dev-principles",
      "description": "Load when implementing, reviewing, refactoring, or designing code: the engineering values every code decision is judged against."
    },
    {
      "directory": "dev-workflow",
      "name": "dev-workflow",
      "description": "Load for the lifecycle of a code change, from the plan to the merged PR: keep going and when to stop, verify, failing tests, review rounds, merges and rebases, early knowledge capture, commits, the PR, and branch cleanup."
    },
    {
      "directory": "diagnose",
      "name": "diagnose",
      "description": "Load when diagnosing hard bugs or performance regressions. Structured loop from feedback loop through instrumentation to fix."
    },
    {
      "directory": "divergence",
      "name": "divergence",
      "description": "Load when the design or plan may shift during multi-phase work: a logged shift lets reviewers tell planned change from drift."
    },
    {
      "directory": "explore-and-engage",
      "name": "explore-and-engage",
      "description": "Load when you investigate with a human waiting: share your read and ask the next question while the evidence comes in, instead of going silent until it is complete."
    },
    {
      "directory": "goal-writing",
      "name": "goal-writing",
      "description": "Load when turning intent into an executable goal for an agent, delegated run, work item, experiment, or handoff. Use to define outcome, evidence, constraints, anti-goals, stop conditions, and reporting shape before work begins.\n"
    },
    {
      "directory": "grill",
      "name": "grill",
      "description": "Use in conversation to stress-test a plan or direction. Interviews the human in rounds, asking every question that is ready with a recommended answer, until no decision is left open.\n"
    },
    {
      "directory": "grill-with-docs",
      "name": "grill-with-docs",
      "description": "Use when grilling should be grounded primarily in project artifacts. Loads `/grill`, checks project vocabulary and prior decisions first, and spawns bounded explorers when the answer should come from docs.\n"
    },
    {
      "directory": "grill-with-evidence",
      "name": "grill-with-evidence",
      "description": "Use when grilling should be grounded in evidence. Loads `/grill`, then checks the plan, terms, and assumptions against project artifacts first and primary sources when needed.\n"
    },
    {
      "directory": "handoff",
      "name": "handoff",
      "description": "Use when the next phase belongs to a different interactive lead: writes a transition brief, runs applicable pre-phase checks, and hands off to a new primary session."
    },
    {
      "directory": "information-hierarchy",
      "name": "information-hierarchy",
      "description": "Load when a report, doc, or explanation runs past one screen, or will be browsed rather than read: choose the form for each beat (prose, diagram, table, mockup), put the answer first and depth behind it."
    },
    {
      "directory": "intent-modeling",
      "name": "intent-modeling",
      "description": "Use before acting on human instructions: separate what they said from what they meant."
    },
    {
      "directory": "issues",
      "name": "issues",
      "description": "Load when you defer work, so each item lands where it will be found: a colocated .context/ file or a GitHub issue."
    },
    {
      "directory": "knowledge-layers",
      "name": "knowledge-layers",
      "description": "Use when deciding where knowledge goes or reading/writing durable docs: AGENTS.md, .context/, KB, docs/, and work directories."
    },
    {
      "directory": "llm-writing",
      "name": "llm-writing",
      "description": "Load before you write a commit message, PR body, changelog entry, issue, report to the user, doc, README, AGENTS.md or .context/ page, KB page, or prompt: choose plain words, write for the reader's context, and strip default LLM phrasing."
    },
    {
      "directory": "md-validation",
      "name": "md-validation",
      "description": "Load after writing, moving, or linking markdown pages or Mermaid diagrams, before committing them: validates links, the KB link graph, and diagram syntax."
    },
    {
      "directory": "merge-prep",
      "name": "merge-prep",
      "description": "Load before merging or rebasing a branch. Build comprehension of what each side intended so conflict resolution serves the work, not the text."
    },
    {
      "directory": "parallel-execution",
      "name": "parallel-execution",
      "description": "Load when work splits into lanes that can run in parallel or phases that build on each other. DAG planning, worktrees, merging, gates."
    },
    {
      "directory": "poc",
      "name": "poc",
      "description": "Load when a feasibility question needs an answer from running code: throwaway code that answers it, then is deleted."
    },
    {
      "directory": "post-dev",
      "name": "post-dev",
      "description": "Run when implementation is done, before opening the PR: catches what would otherwise ship missing (PR body, changelog, review sign-off, deferred work, knowledge capture, cleanup)."
    },
    {
      "directory": "pre-dev",
      "name": "pre-dev",
      "description": "Run before implementation starts: before your first source edit, or before handing off to an implementation agent. It is the only point where before-state evidence still exists."
    },
    {
      "directory": "probe",
      "name": "probe",
      "description": "Load when you need to know what the system actually does: run it, exercise workflows, reproduce bugs. Reading code and passing tests don't show that."
    },
    {
      "directory": "qi-layer",
      "name": "qi-layer",
      "description": "Use when writing or maintaining AGENTS.md, .context/CONTEXT.md, or a Claude-specific CLAUDE.md: keep intent docs minimal and load-bearing."
    },
    {
      "directory": "qi-maintenance",
      "name": "qi-maintenance",
      "description": "Load on agents that make durable changes to a project's files, so the colocated AGENTS.md and .context/ docs stay true for the next cold agent."
    },
    {
      "directory": "react-architecture",
      "name": "react-architecture",
      "description": "Load when building or reviewing React code, where component composition, state architecture, and token discipline decide whether the UI stays easy to change."
    },
    {
      "directory": "reflect",
      "name": "reflect",
      "description": "Use when the user invokes it before you report: checks you delivered what they needed, not only what they literally asked, and routes knowledge capture."
    },
    {
      "directory": "research-web",
      "name": "research-web",
      "description": "Load when a question depends on external facts (library docs, upstream issues, changelogs, production patterns) that may postdate training data. Gathers and reports; the caller judges."
    },
    {
      "directory": "review",
      "name": "review",
      "description": "Use when reviewing code, designs, or plans: review the code as it stands, check standards and design alignment, report constructive findings with severity."
    },
    {
      "directory": "review-alignment",
      "name": "review-alignment",
      "description": "Load when one artifact must faithfully match another (plan vs design, code vs spec, output vs intent) and the check needs to be systematic, not a skim."
    },
    {
      "directory": "shared-dao",
      "name": "shared-dao",
      "description": "Load when a concept has two names, a name has two meanings, or you are about to coin a term: resolve it early, one name per concept, in the project's vocab files."
    },
    {
      "directory": "shared-workspace",
      "name": "shared-workspace",
      "description": "Use when a workspace has changes from other agents: safe orientation, preserving unfamiliar files."
    },
    {
      "directory": "solo-dev",
      "name": "solo-dev",
      "description": "Load when you implement and verify a change yourself, in one session, instead of delegating it: what you do yourself and what still goes to a spawn."
    },
    {
      "directory": "source-study",
      "name": "source-study",
      "description": "Load when you need evidence from real codebases before designing, scoping, or choosing an approach."
    },
    {
      "directory": "structured-artifact",
      "name": "structured-artifact",
      "description": "Load when the human wants something to browse rather than read: an HTML page that explains or presents information, with its delivery."
    },
    {
      "directory": "tech-docs",
      "name": "tech-docs",
      "description": "Use when writing design documents. Architecture specs, behavioral specs, component docs, feasibility reports."
    },
    {
      "directory": "test-architecture",
      "name": "test-architecture",
      "description": "Load when test code is making the codebase harder to change, to find tests that pin implementation, mock rot, and sprawl worth deleting."
    },
    {
      "directory": "testing",
      "name": "testing",
      "description": "Load when deciding whether to write a test, and at which tier: keep none the user didn't ask for, and delete tests you wrote to check your work."
    },
    {
      "directory": "thermo-nuclear-review",
      "name": "thermo-nuclear-review",
      "description": "Use for extremely strict maintainability review: find the code-judo move that makes a change or a design, and the system around it, dramatically simpler. Blocks structural regressions."
    },
    {
      "directory": "ui-implementation",
      "name": "ui-implementation",
      "description": "Load when turning a settled visual direction (mockups, a spec, screenshots) into production UI, so the result matches the design and every state renders, not only the one in the mockup."
    },
    {
      "directory": "unravel-codebase",
      "name": "unravel-codebase",
      "description": "Use when the human wants to understand how a codebase works today by walking through it together. Human-paced; source stays read-only unless asked; fixes the docs it reads along the way."
    },
    {
      "directory": "uxdev",
      "name": "uxdev",
      "description": "Load when the work needs visual thinking about what the user sees, so design choices come from the brief and the existing design language, not defaults."
    },
    {
      "directory": "visualize-codebase",
      "name": "visualize-codebase",
      "description": "Load when the human wants a browsable visual map of a codebase: structure, data flow, connections, and where something looks off."
    },
    {
      "directory": "work-artifacts",
      "name": "work-artifacts",
      "description": "Load when work must survive compaction or crashes or be shared with other agents: findings, decisions, and artifacts go in the work directory, not in context."
    },
    {
      "directory": "zoom-out",
      "name": "zoom-out",
      "description": "Use when orienting in an unfamiliar area: fans out parallel explorers across structure, knowledge, and history, then synthesizes one orientation map."
    }
  ],
  "mcp": [],
  "hooks": []
}
const ROOT = dirname(fileURLToPath(import.meta.url))
const HOOK_DIR_TOKEN = "${MARS_HOOK_DIR}"

function runtimeServer(server) {
  if (!server.environment) return server

  const environment = {}
  for (const [key, value] of Object.entries(server.environment)) {
    const match = /^\{env:(.+)\}$/.exec(value)
    if (!match) {
      environment[key] = value
      continue
    }
    const resolved = process.env[match[1]]
    if (resolved !== undefined) environment[key] = resolved
  }
  return { ...server, environment }
}

function encodeForJavaScriptString(value) {
  return value.replace(/[^A-Za-z0-9/._-]/g, (character) => {
    return `\\u${character.charCodeAt(0).toString(16).padStart(4, "0")}`
  })
}

async function renderHook(hook) {
  const hookDirectory = join(ROOT, "hooks", hook.name)
  const source = await readFile(join(hookDirectory, hook.fragment), "utf8")
  return source.replaceAll(HOOK_DIR_TOKEN, encodeForJavaScriptString(hookDirectory))
}

export default {
  id: DATA.plugin,
  async setup(ctx) {
    if (DATA.skills.length) {
      const skills = await Promise.all(
        DATA.skills.map(async (skill) => {
          const path = join(ROOT, "skills", skill.directory, "SKILL.md")
          return { ...skill, path, content: await readFile(path, "utf8") }
        }),
      )
      await ctx.skill.transform((editor) => {
        for (const skill of skills) {
          editor.add({
            id: `${DATA.plugin}:${skill.directory}`,
            name: skill.name,
            description: skill.description,
            path: skill.path,
            content: skill.content,
          })
        }
      })
    }

    if (DATA.mcp.length) {
      const servers = JSON.parse(await readFile(join(ROOT, "mcp.json"), "utf8"))
      await ctx.mcp.transform((editor) => {
        for (const name of DATA.mcp) {
          editor.set(`${DATA.plugin}:${name}`, runtimeServer(servers[name]))
        }
      })
    }

    const cleanups = []
    for (const hook of DATA.hooks) {
      try {
        const rendered = await renderHook(hook)
        const url = `data:text/typescript;base64,${Buffer.from(rendered, "utf8").toString("base64")}`
        const definition = (await import(url)).default
        if (!definition || typeof definition.id !== "string" || typeof definition.setup !== "function") {
          throw new Error(`OpenCode hook ${hook.name} must export default { id, setup }`)
        }
        const cleanup = await definition.setup(ctx)
        if (typeof cleanup === "function") cleanups.push(cleanup)
      } catch (error) {
        console.error(`[${DATA.plugin}] failed to load hook ${hook.name}`, error)
      }
    }

    if (cleanups.length) {
      return async () => {
        for (const cleanup of cleanups.reverse()) await cleanup()
      }
    }
  },
}
