---
name: dev-workflow
description: 'Load for the lifecycle of a code change, from the plan to the merged PR: keep going and when to stop, verify, failing tests, review rounds, merges and rebases, early knowledge capture, commits, the PR, and branch cleanup.'
metadata:
  type: reference
alwaysApply: false
---

# Dev Workflow

## Plan

Account for the earlier work on the subject first (`/meridian-dev-workflow:explore-and-engage`),
then write the plan into the work directory.

When the change adds something the project doesn't have yet (a module,
contract, seam, data format, or UI pattern), moves responsibility between
modules, or grows existing code beyond a local edit, settle its
architecture in the plan with `/meridian-dev-workflow:architecture` loaded: how others have built
it, where it lands, the boundaries it adds or moves, how it reorganizes the
code, and which later changes it makes easier or harder.

Have a `@reviewer` with `/meridian-dev-workflow:thermo-nuclear-review` and `/meridian-dev-workflow:architecture`
review that plan against the code it lands in, and put the enabling refactors it finds first: found
now, a simpler structure is a refactor; after the code exists, a rewrite.
When several structures would work and none is clearly better, have
`@design-lead` lay out the options with a recommendation, then decide from
its report; a tradeoff that is the user's goes to them.

Then run `/meridian-dev-workflow:pre-dev` before the first source edit.

## Keep Going

Keep moving until the requested outcome is implemented, verified, and ready
to ship. A spawn returning is not a stopping point: fold its findings in,
decide the next step, and continue. Where the brief leaves something
unclear, write the question in the work directory with the call you made,
keep going, and put the open questions to the user at the end. A product
decision only the user can make, or a departure from one they made
(`/meridian-dev-workflow:intent-modeling`), goes to them now; meanwhile work on what doesn't
depend on it.

Stop early only for: (a) a scope problem, sent to your caller as a Redesign
Brief (`/meridian-dev-workflow:review` `resources/redesign-escalation.md`), (b) a blocker you
cannot clear yourself.

## Verify

Exercise each way the change could fail on the real system (`/meridian-dev-workflow:probe`). Run
the full suite once, on the commit you send to review; passing unit tests
never show the change works.

When tests fail, decide whether the behavior broke, the test went stale, or
the test sits at the wrong tier (`/meridian-dev-workflow:testing`) before changing either the
code or the test.

## Review

Once per coherent change, not per edit, open `/meridian-dev-workflow:agent-staffing`
`resources/reviewers.md` and staff the lanes it calls for; a change whose
plan needed the architecture step gets the structure lane, not only
correctness. Prepare `/meridian-dev-workflow:post-dev` while the lanes run, then fix their
findings as `reviewers.md` says, up to its round limits.

## Merges and Rebases

Hand every merge and rebase to `@coder` with `/meridian-dev-workflow:merge-prep` attached. Skim
the PRs being merged in and tell the coder what matters from each side and
where they could overlap: `/meridian-dev-workflow:merge-prep` has it read the sources, and your
brief tells it what to look for.

## Knowledge Capture

`/meridian-dev-workflow:post-dev` captures knowledge when the change settles. Spawn `@kb-lead`
earlier when a decision has settled and the work will pause across
sessions.

## Commit Discipline

Commit each self-contained change after the focused checks that cover its risks. Run the full project gate at ship readiness, not after every implementation step, unless the project's policy or a specific risk requires it earlier.

Update the changelog according to the project's conventions, at commit time rather
than retroactively.

## Deferrals

When you skip something during implementation — a cleanup, an edge case, a
better approach — route it immediately through `/meridian-dev-workflow:issues`.

## Ship

Run `/meridian-dev-workflow:post-dev` before opening the PR. When the branch passes the full
gate, push it and open or update its PR without asking, and clean up what
the branch claimed the moment it merges, both per `resources/ship.md`.

## Do Not

- Land feature work on `main` or `staging` directly, by merge or by push — use a PR. Merges between other working branches need no gate.
- Create or push `v*` tags manually (CI owns tagging)
- Use `--no-verify` on push without explicit user permission
- Delete untracked files without asking (may be someone else's work)
- Edit `__version__` or `Cargo.toml` version for stable releases (CI-owned)
