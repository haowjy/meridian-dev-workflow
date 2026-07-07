---
name: branch-sync
type: checkpoint
description: "Sync a feature branch with its moved base: rebase-vs-merge choice, intent-aware conflict resolution, sibling-PR reconciliation. Run when the base moved or a PR shows CONFLICTING."
model-invocable: true
---

# Branch Sync

Run when the base branch has moved under your feature branch, a PR reports
CONFLICTING, or overlapping PRs exist against the same base.

## Choose merge vs rebase

- **Pushed or shared branch → merge the base in.** Never rewrite published
  history; repo convention is `git merge origin/<base>` into the feature
  branch.
- **Local-only, short-lived branch → rebase** onto the base for linear
  history.

## Understand before resolving

Conflicts are resolved between *intents*, not hunks. Before touching a
conflict marker:

1. `git merge-base origin/<base> HEAD`, then
   `git log --oneline --first-parent <mb>..origin/<base>` — identify which
   PRs landed on the base since you branched.
2. Read each landed PR (`gh pr view <n>`) for what it was trying to do.
3. Test-merge to enumerate: `git merge --no-commit --no-ff origin/<base>`,
   then `git diff --name-only --diff-filter=U`.
4. For each conflict file, diff **both** sides against the merge base
   (`git diff <mb> HEAD -- <file>` / `git diff <mb> origin/<base> -- <file>`)
   so you know what each side's change *means* before combining them.

## Resolution rules

- **Take the newer structure, carry the other side's semantics through it.**
  When one side restructured (extracted helpers, converted a union to a
  const array) and the other made a semantic change (a rename, a contract
  change), resolve to the new structure expressing the semantic change.
- **One concept, one module.** If the incoming side introduced a canonical
  helper for logic your side edited in duplicated copies, delegate to the
  canonical helper instead of resolving each copy — the semantic change then
  lives in one place.
- Never resolve a conflict by discarding a side you don't understand; go
  back to the PR intent first.

## Sweep semantic-but-not-textual conflicts

Textual conflicts are the minority. After resolving, sweep files the base
side added or changed for identifiers, string literals, URIs, and labels
your branch renamed or deleted (`git diff <mb> origin/<base> --name-only |
xargs rg <renamed-terms>`). Typecheck catches type-level drift; only a grep
catches literals.

## Verify

Full gate (`pnpm check`) on the merge result before committing it. Push,
then confirm the PR's mergeability recomputed (it updates async).

## Sibling open PRs

For other open PRs against the same base that overlap your branch:

1. Probe-merge each into a **throwaway worktree** of your branch
   (`git worktree add … --detach`) to size the conflict set; abort and
   remove the worktree after.
2. If its conflicts sit in modules your branch **rewrote or deleted**, it is
   an **intent-port, not a merge**. Map each of its intents against your
   actual code: *structurally satisfied* (cite the mechanism), *still a real
   gap* (port it, freshly designed), or *obsolete*. Delegate the mapping to
   an explorer per PR.
3. Close superseded PRs with the verdict table in the closing comment so the
   intent trail survives; port the named gaps as scoped work. Never
   force-merge a superseded diff — it resurrects deleted architecture.
