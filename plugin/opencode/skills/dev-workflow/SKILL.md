---
name: dev-workflow
description: 'Load for the lifecycle of a code change, from the plan to the merged PR: keep going and when to stop, verify, failing tests, review rounds, merges and rebases, early knowledge capture, commits, the PR, and branch cleanup.'
metadata:
  type: reference
---

# Dev Workflow

## Plan

Account for the earlier work on the subject first (`/meridian-dev-workflow:explore-and-engage`),
then write the plan into the work directory.

Settle the structure in the plan before any code: where the change lands,
what it adds or moves, and the refactors in the existing code that would
shrink it. Put those refactors first: found now, a simpler structure is a
refactor; after the code exists, it's a rewrite. When the plan adds a
module, contract or data format that other code will depend on, have a
`@reviewer` review it against the code it lands in.

Then run `/meridian-dev-workflow:pre-dev` before the first source edit.

## Keep Going

Keep moving until the requested outcome is implemented, verified, and ready
to ship. A spawn returning is not a stopping point: fold its findings in,
decide the next step, and continue. Where the brief leaves something
unclear, write the question in the work directory with the call you made,
keep going, and put the open questions to the user at the end. A product
decision only the user can make, or a departure from an instruction they
gave for this work (`/meridian-dev-workflow:intent-modeling`), goes to them now; meanwhile work on what doesn't
depend on it.

Worktrees, installs, commits, pushes, PRs, issues, knowledge capture, doc and
comment fixes, and work already approved need no permission: do them. Only
these go to the human: a product decision only they can make, a departure
from an instruction they gave for this work or from an invariant, and the
merges the project reserves for them. A
project can narrow or widen this in its `AGENTS.md`.

Stop early only for: (a) a scope problem, sent to your caller as a Redesign
Brief (`/meridian-dev-workflow:review` `resources/redesign-escalation.md`), (b) a blocker you
cannot clear yourself.

## Verify

Whoever writes the code exercises each way it could fail on the real system
(`/meridian-dev-workflow:testing`); read its report for what it left unverified. Check each review fix the same way, on what it changes and the screens or commands
next to it. Run the full suite on the commit you send to review and on the commit you
ship;
passing unit tests never show the change works.

When tests fail, decide whether the behavior broke, the test went stale, or
the test sits at the wrong tier (`/meridian-dev-workflow:testing`) before changing either the
code or the test.

## Review

Once per feature, when all of it is built, not per phase, move, part PR,
or edit, open `/meridian-dev-workflow:agent-staffing` `resources/reviewers.md` and staff the review
it calls for. Prepare `/meridian-dev-workflow:post-dev` while it runs, then fix its
findings as `reviewers.md` says, within its one round.

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

Commit each self-contained change after the focused checks that cover its risks.

Update the changelog according to the project's conventions, at commit time rather
than retroactively.

## Deferrals

Fix what you find. When something truly can't be fixed now, route it through
`/meridian-dev-workflow:issues`.

## Ship

Run `/meridian-dev-workflow:post-dev` before opening the PR. When the branch passes the full
gate, push it and open or update its PR without asking, and clean up what
the branch claimed the moment it merges, both per `resources/ship.md`.

## Do Not

- Land feature work on `main` or `staging` directly, by merge or by push — use a PR. Merges between other working branches need no gate.
- Create or push `v*` tags manually (CI owns tagging)
- Use `--no-verify` on push without explicit user permission
- Delete untracked files without asking (may be someone else's work)
