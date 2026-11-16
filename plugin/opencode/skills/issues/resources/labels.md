# Issue Labels

## Category Labels

| Label | Color (hex) | Description |
|-------|-------------|-------------|
| `bug` | `d73a4a` | Bug found during implementation |
| `unexpected` | `e99d42` | Surprising behavior worth investigating |
| `backlog` | `0075ca` | Work needed but out of current scope |
| `deferred` | `fbca04` | Explicitly deferred from current work |
| `review-finding` | `7057ff` | From code review, not blocking |
| `decision-needed` | `d876e3` | Needs a decision before it can be worked on |

## Work Item Labels

| Label | Color (hex) | Description |
|-------|-------------|-------------|
| `work:<slug>` | `c5def5` | Links issue to its work item when one exists |

When an active work item exists, replace `<slug>` with its actual slug (e.g.,
`work:auth-refactor`). Otherwise omit the work label and work-item references.

## Label Creation

Run these once per repository to set up the label taxonomy. Idempotent: `gh label create` will error if the label exists, which is fine.

```bash
gh label create "bug" --color "d73a4a" --description "Bug found during implementation" 2>/dev/null
gh label create "unexpected" --color "e99d42" --description "Surprising behavior worth investigating" 2>/dev/null
gh label create "backlog" --color "0075ca" --description "Work needed but out of current scope" 2>/dev/null
gh label create "deferred" --color "fbca04" --description "Explicitly deferred from current work" 2>/dev/null
gh label create "review-finding" --color "7057ff" --description "From code review, not blocking" 2>/dev/null
gh label create "decision-needed" --color "d876e3" --description "Needs a decision before it can be worked on" 2>/dev/null
gh label create "tech-debt" --color "D4C5F9" --description "Technical debt to address later" 2>/dev/null
gh label create "enhancement" --color "A2EEEF" --description "New feature or improvement to existing functionality" 2>/dev/null
gh label create "design" --color "F9D0C4" --description "Needs design discussion or decision" 2>/dev/null
gh label create "blocked" --color "B60205" --description "Cannot proceed without external resolution" 2>/dev/null
gh label create "good-first-task" --color "7057FF" --description "Good for a new agent or contributor" 2>/dev/null
```

Create work item labels as needed:

```bash
gh label create "work:auth-refactor" --color "c5def5" --description "Work item: auth-refactor" 2>/dev/null
```
