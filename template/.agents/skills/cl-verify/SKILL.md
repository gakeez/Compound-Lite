---
name: cl-verify
description: Independently verify implemented work. Use after cl-work or any substantial code change to review the diff, tests, plan compliance, Agent behavior, and risks. Prefer read-only review unless explicitly asked to add tests.
---

# cl-verify

Verify work from an independent perspective. Do not rely on the builder's explanation as evidence.

## Flow

1. Read `AGENTS.md`.
2. Read `STRATEGY.md` if product/Agent direction matters.
3. Read the relevant requirements and plan artifacts.
4. Inspect the current diff.
5. Compare implementation against requirements and plan.
6. Run relevant local verification commands when safe.
7. Review tests and eval cases.
8. For Agent behavior changes, load the Agent-native lens and check `docs/evals/`.
9. Report findings and residual risks.

## Default posture

- Review first.
- Prefer read-only behavior.
- Do not rewrite implementation unless the user explicitly asks.
- If tests are missing, recommend focused tests or ask before adding them.
- Do not commit, push, open PRs, deploy, or mutate external systems.

## Output

```text
Verdict:
Requirements coverage:
Verification run:
Findings:
Agent behavior / eval status:
Risks:
Recommended next step:
```

Read `references/risk-lenses.md`, `references/verification-resolver.md`, and `references/agent-native-lens.md` before reviewing.
