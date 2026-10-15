# meridian-dev-workflow

A multi-agent development team for [Meridian](https://github.com/meridian-flow/meridian-cli):
leads you work with in a session, the specialists they spawn, and the skills
that carry a change from first edit to merged PR.

Built on [meridian-base](https://github.com/meridian-flow/meridian-base),
which supplies the shared workers (`explorer`, `session-miner`, `subagent`,
`kb-lead`, `kb-maintainer`) and the coordination skills. Both must be
installed.

## Install

```bash
meridian mars add meridian-flow/meridian-base
meridian mars add meridian-flow/meridian-dev-workflow
meridian config set primary.agent tech-lead
```

## How It Works

### Leads

Each session runs one lead, and each lead owns a different kind of decision.

**tech-lead** (the default) leads technical work. It makes the technical
decisions (approach, structure, tradeoffs, what to cut) and records them in a
decision file per work item. It runs a team of agents through long-running or
multi-part work, keeps several loosely related tasks moving as separate work
items, and makes small fixes and glue changes itself.

**product-lead** settles what to build and why: the problem statement,
requirements, and product decisions. It spawns only research, then proposes
which lead comes next and writes the handoff. You launch that lead as its own
session so you can steer it directly.

**design-lead** settles structure when it is open: interfaces, boundaries,
the data model. It also takes a Redesign Brief from an implementation lead.
It investigates in parallel, converges, runs one challenge (prober, reviewer,
or an alignment review), and returns design docs with a recommendation. Run
it as a session or spawn it.

**gpt-dev** implements and verifies one coherent objective in a single
session (`/solo-dev`).

**ux-lead** works the same way for UI, with you steering visual direction.
It makes small tweaks directly for you to check. For a large change it
explores first, running mockups in parallel when you want to compare
directions, then builds the UI itself. It spawns coders only for a big
frontend refactor.

```text
Default: tech-lead.
When direction is open:  product-lead ─handoff→ design-lead | ux-lead | gpt-dev | tech-lead
When structure is open:  design-lead ─handoff→ tech-lead | gpt-dev
```

### A Change, End to End

Every implementation lead runs the same lifecycle:

1. **`/pre-dev`** runs before the first source edit. It sets up a worktree
   for the work item, drafts the PR body from the repo template, and captures
   before-state evidence while it still exists.
2. **Implement.** tech-lead plans any task that needs more than one spawn as a
   DAG with `/parallel-execution`, using a worktree per parallel lane and one
   owner for each change to shared code. It delegates to `coder` and
   `frontend-coder`. gpt-dev and ux-lead implement the change themselves.
   Each commit carries a `CHANGELOG.md` entry.
3. **Verify.** Leads run focused checks and `/probe` against the real system
   while working, and the full suite once on the finished change.
4. **Review.** `reviewer` and `prober` run on a committed state. Parallel
   work gets one review per phase, and the last phase's review covers the
   whole change with `thermo-nuclear-review`. A single-session lead runs both
   once at the end, on the same dev stack, each with its own test data.
   Review runs again only when fixes restructured code or changed behavior.
5. **`/post-dev`** runs before the PR. It checks the PR body, the changelog,
   the review sign-off, and deferred work (routed to `.context/` or issues).
   It also runs `kb-lead` once for the whole change.
6. **Ship** with `/dev-workflow`. The lead pushes the feature branch and
   opens the PR with the drafted body and a `release:*` label. Merging to
   `main` waits for a human.

### When Fixes Don't Converge

On a second finding of the same failure class in the same code, the lead
stops patching and looks for the shared cause, often two places owning one
invariant. A worker that ran out of depth gets one retry on Opus with its
report. When the structure itself is wrong, the lead writes a Redesign Brief:
design problems go to design-lead, scope problems go back to you and
product-lead.

### Review

`reviewer` judges the code as it stands, not only the diff. Every review
covers:

- correctness and regressions
- maintainability: entanglement, and what the change could delete
- efficiency on hot paths
- security

It settles behavioral findings by running the system. Attach skills to focus
it; `skills/agent-staffing/resources/reviewers.md` maps change risks to
review skills.

## Agents

Use the tables below to compare roles. Each agent's description is its
launch guidance: when to use it, what to pass, and what comes back.

Models are profile defaults. Fallbacks and explicit-only options live in each
agent's `model-policies`. `skills/agent-staffing/` covers model choice by
task.

**Leads**

| Agent | Model | Role |
|---|---|---|
| `tech-lead` | fable | Technical decisions, an agent team, several concurrent tasks, hands-on fixes |
| `product-lead` | opus | Product direction: intent, requirements, decisions, handoff |
| `design-lead` | opus | Technical design: structural options, interfaces, boundaries, tradeoffs |
| `gpt-dev` | astra | Implements and verifies one objective in a single session |
| `ux-lead` | opus | Visual direction and UI implementation in one session |

**Implementation**

| Agent | Model | Role |
|---|---|---|
| `coder` | luna | Implements a scoped objective, commits with a changelog entry |
| `frontend-coder` | sonnet | Production UI with visual self-checks in a browser |
| `mockup-dev` | luna | Throwaway frontend mockups for comparing directions |
| `imagegen` | sol | Generated images: concepts, icons, reference imagery |

**Verification**

| Agent | Model | Role |
|---|---|---|
| `reviewer` | opus | Finds risks in a commit: correctness, maintainability, efficiency, security. Read-only |
| `prober` | luna | Runtime evidence: exercises workflows, reproduces bugs, runs feasibility spikes |
| `investigator` | luna | Root cause of broken behavior; fixes only when the brief assigns it |

**Design and research**

| Agent | Model | Role |
|---|---|---|
| `architect` | opus | Compares structural options and writes design docs |
| `design-researcher` | sol | Structured analysis of design alternatives |
| `web-researcher` | luna | External facts: library docs, upstream issues, changelogs |
| `source-researcher` | luna | How real open-source projects solve a similar problem |
| `browser` | luna | Live websites: design references, scraping, screenshots |

From meridian-base: `explorer` (codebase facts), `session-miner` (past
decisions), `kb-lead` (knowledge capture), `kb-maintainer` (doc structure),
`subagent` (general tasks).

## Skills

**Workflow**

| Skill | What it covers |
|---|---|
| `pre-dev` | Before the first edit: worktree, PR body draft, before-state evidence |
| `solo-dev` | Single-session implementation: when to review and probe, verification, when to stop patching |
| `parallel-execution` | DAG planning, worktree lanes, merge and verify, review per phase |
| `dev-workflow` | Commits, changelog, pushing and opening PRs, branch cleanup |
| `post-dev` | Before the PR: PR body, changelog, review sign-off, deferred work, knowledge capture |
| `divergence` | Logging plan shifts during multi-phase work in `DIVERGENCE/` |
| `merge-prep` | Understanding both sides' intent before merging or rebasing |
| `issues` | Routing deferred work to `.context/` or GitHub issues |
| `agent-staffing` | Which agents and models to use, review and test coverage by risk |

**Engineering**

| Skill | What it covers |
|---|---|
| `dev-principles` | The engineering values code decisions are judged against |
| `code` | Changing code yourself: follow project patterns, delete what you replace, verify for real |
| `architecture` | Boundaries, dependencies, structural risk |
| `testing` | Whether and how to test: tests earn their place by protecting a durable risk |
| `probe` | Runtime verification against the real system |
| `poc` | Throwaway code that answers a feasibility question |
| `diagnose` | Diagnosis loop for hard bugs and performance regressions |

**Review**

| Skill | What it covers |
|---|---|
| `review` | Base review method: code as it stands, standards and design, maintainability, efficiency, redesign escalation |
| `thermo-nuclear-review` | Strict maintainability: the code-judo move that makes the system dramatically simpler |
| `test-architecture` | Tests that pin implementation, mock rot, sprawl worth deleting |
| `review-alignment` | Systematic check that one artifact matches another |
| `react-architecture` | React composition, state architecture, token discipline |

**UI and visual**

| Skill | What it covers |
|---|---|
| `uxdev` | Visual thinking grounded in the brief and the existing design language |
| `ui-implementation` | Turning a settled direction into production UI |
| `design-craft` | Deliberate color, typography, layout, motion, interaction |
| `anti-slop` | AI-generated UI tells to avoid |
| `agent-browser` | Driving a live browser: snapshots, interaction, screenshots |

**Research and docs**

| Skill | What it covers |
|---|---|
| `research-web` | Gathering external facts that may postdate training data |
| `source-study` | Evidence from real codebases before designing |
| `design-analysis` | Turning findings into a design analysis with compared options |
| `tech-docs` | Writing design documents |
| `unravel-codebase` | Human-paced walkthrough of how a codebase works (human-invoked) |
| `visualize-codebase` | Browsable visual map of a codebase (human-invoked) |

Agents here also load meridian-base skills, including `work-artifacts`,
`shared-dao`, `llm-writing`, `information-hierarchy`, `intent-modeling`,
`explore-and-engage`, `handoff`, `grill-with-docs`, `zoom-out`,
`qi-maintenance`, `qi-layer`, `knowledge-layers`, and `session-mining`.

## Layout

```
agents/*.md              # Agent profiles (YAML frontmatter + markdown)
skills/*/SKILL.md        # Skills (with optional resources/ subdirectory)
```

## See Also

- [meridian-cli](https://github.com/meridian-flow/meridian-cli): the Meridian coordination engine
- [meridian-base](https://github.com/meridian-flow/meridian-base): the coordination layer this builds on
