---
name: cl-debug
description: Debug failures systematically. Use for bugs, failing tests, stack traces, regressions, broken Agent behavior, or when previous fixes failed. Reproduce first, trace root cause, then apply a minimal local fix with tests.
---

# cl-debug

Find the root cause before fixing.

## Core rules

- Reproduce or characterize the bug before changing code.
- Trace the causal chain from trigger to symptom.
- Form hypotheses and test them.
- Change one thing at a time.
- If a fix works but the hypothesis was wrong, continue investigating.
- Add or update regression tests when practical.

## Flow

1. Parse the bug report, error, failing test, or broken behavior.
2. Check environment sanity: branch, dependencies, runtime, config, services if relevant.
3. Reproduce or characterize the failure.
4. Trace the code path.
5. Write the causal chain.
6. Identify root cause and test recommendation.
7. Apply a minimal local fix only after root cause is credible.
8. Run targeted verification.
9. Recommend `cl-verify`.
10. If the lesson is durable, recommend `cl-compound`.

## Boundaries

- Do not shotgun multiple unrelated fixes.
- Do not commit, push, open PRs, deploy, or mutate external systems.
- Ask before changing security, data, or Agent tool permissions.

Read `references/root-cause-flow.md`, `references/level-1-automation.md`, and `references/agent-native-lens.md` when relevant.
