---
name: cl-plan
description: Create an implementation plan for non-trivial work. Use after requirements/design review, for multi-step implementation, Agent behavior changes, integrations, refactors, data/security/reliability changes, or when the user asks for a plan. Does not write code.
---

# cl-plan

Define HOW to build before local implementation.

## Flow

1. Read `AGENTS.md`.
2. Read `STRATEGY.md` when product/Agent behavior matters.
3. Read the relevant `docs/brainstorms/` requirements document if present.
4. Perform project discovery.
5. Identify affected files and existing patterns.
6. Select risk lenses.
7. Determine verification commands using the resolver.
8. For Agent behavior changes, load the Agent-native lens and include eval requirements.
9. Write a dated plan under `docs/plans/`.
10. Stop for `cl-review` before `cl-work`.

## Output artifact

Use `docs/plans/YYYY-MM-DD-topic-plan.md`.

Required sections:

```md
# Plan: Topic

## Origin
## Goal
## Scope
## Non-goals
## Project discovery
## Implementation plan
## Files likely to change
## Verification
## Risks
## Agent-native considerations
## Rollback / recovery
## Open questions
```

## Boundaries

- Do not write code.
- Do not over-specify exact implementation code.
- Do not silently expand scope beyond requirements.
- Do not proceed to `cl-work` until the plan artifact has passed `cl-review` and the user confirms implementation should start.

Read `references/project-discovery.md`, `references/verification-resolver.md`, `references/risk-lenses.md`, `references/agent-native-lens.md`, and `references/artifact-policy.md` before writing the plan.
