---
name: cl-onboard
description: Adopt Compound Lite in an existing or new repository. Use for first setup, mid-project adoption, project scan, creating AGENTS.md/STRATEGY.md drafts, and bootstrapping docs folders. Never modify application code.
---

# cl-onboard

Adopt Compound Lite in the current repository without rewriting history or changing application code.

## Purpose

Use this skill when a project wants to start using Compound Lite. It supports both existing projects and new projects.

## Rules

- Start with a read-only scan.
- Do not modify application code.
- Do not commit, push, open PRs, deploy, or mutate external systems.
- Do not invent historical plans. If this is a mid-project adoption, label strategy and active plans as current snapshots.
- Prefer creating missing artifacts over overwriting existing files.

## Flow

1. Read `AGENTS.md` if present.
2. Scan README, docs, manifests, CI config, key source directories, tests, current branch, and git status.
3. Summarize the project shape, likely verification commands, existing conventions, and current risks.
4. Check for `STRATEGY.md`; if missing, draft one from existing evidence and user-provided context.
5. Ensure artifact directories exist:
   - `docs/ideation/`
   - `docs/brainstorms/`
   - `docs/plans/`
   - `docs/solutions/`
   - `docs/pulse-reports/`
   - `docs/evals/`
6. If there is active in-progress work, offer to write one current active-work plan under `docs/plans/`.
7. Identify up to three high-value existing learnings that might deserve `docs/solutions/` entries, but do not backfill everything.
8. Finish with a setup summary.

## Output

```text
Project snapshot:
Artifacts created or found:
Suggested verification commands:
Strategy status:
Current active work:
Recommended next skill:
```

Read `references/project-discovery.md`, `references/artifact-policy.md`, and `references/level-1-automation.md` before doing the scan.
