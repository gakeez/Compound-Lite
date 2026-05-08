---
name: cl-design
description: Create a UX/UI design artifact for user-facing Compound Lite work. Use after confirmed requirements and before cl-review/cl-plan when screens, flows, interaction states, visual direction, or image-based UI exploration matter. Does not write code.
---

# cl-design

Define the user experience before implementation planning.

## Flow

1. Read `AGENTS.md`.
2. Read the local design authority when present, such as `design.md`, product design docs, or existing UI guidelines.
3. Read `STRATEGY.md` when product direction or Agent behavior matters.
4. Read the confirmed `docs/brainstorms/` requirements document.
5. Inspect existing UI components, screens, copy, and states that the design may affect.
6. Detect the design context: existing system, partial system, greenfield, or ambiguous.
7. Write a dated UX/UI artifact under `docs/designs/`.
8. Stop for `cl-review`; after review and user confirmation, hand the confirmed design artifact to `cl-plan`.

## Output artifact

Use `docs/designs/YYYY-MM-DD-topic-ux.md`.

Required sections:

```md
# UX/UI Design: Topic

## Origin
## Design context
## UX goal
## Visual thesis
## User flows
## Screen and state design
## Interaction rules
## Copy rules
## Accessibility and responsive notes
## Image concept direction
## Handoff to cl-plan
## Risks
## Open questions
```

## Boundaries

- Do not write code.
- Do not add dependencies, component libraries, or design systems.
- Do not expand product scope beyond confirmed requirements.
- Do not override `AGENTS.md`, local design guidance, or explicit user instructions.
- Do not treat generated images as final UI specs. Images are for visual direction only.
- Do not proceed to `cl-plan` until the design artifact has passed `cl-review` and the user confirms the design direction when the design changes user-facing flow.

## Defaults

- Prefer existing product patterns over new visual systems.
- Keep workflows ergonomic for repeated use, not just first impressions.
- Define empty, loading, error, permission, and mobile states when the UI can enter them.
- Keep copy rules concrete enough that implementation does not invent tone or instructions.
- Use image generation only to explore atmosphere and composition; translate accepted directions back into concrete states, components, and verification checks.
