---
name: cl-work
description: Execute a Compound Lite plan locally. Use when a docs/plans implementation plan is ready. May edit local code and tests and run local verification. Must not commit, push, open PRs, deploy, or mutate external systems.
---

# cl-work

Implement an existing plan locally using Level 1 automation.

## Flow

1. Read `AGENTS.md`.
2. Read the relevant plan completely.
3. Read the referenced requirements document and `STRATEGY.md` when relevant.
4. Confirm scope, non-goals, files, and verification.
5. Implement the smallest safe diff.
6. Update or add tests when behavior changes.
7. Run local verification from the plan.
8. Stop and report if implementation discovery invalidates the plan.
9. Finish with a summary and recommend `cl-verify`.

## Boundaries

- Do not commit.
- Do not push.
- Do not open PRs.
- Do not deploy.
- Do not mutate external systems.
- Ask before adding dependencies, changing security-sensitive behavior, changing Agent tool permissions, or running migrations.

## Completion summary

```text
Changed:
Verified:
Risks:
Artifacts:
Next: Run cl-verify.
```

Read `references/level-1-automation.md`, `references/verification-resolver.md`, and `references/agent-native-lens.md` when relevant.
