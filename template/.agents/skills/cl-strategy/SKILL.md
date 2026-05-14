---
name: cl-strategy
description: Create or update STRATEGY.md. Use when setting product direction, revising roadmap, clarifying Agent product thesis, or when downstream work lacks a strategy anchor. Does not write feature requirements or implementation plans.
---

# cl-strategy

Create or maintain `STRATEGY.md` as the product and Agent strategy anchor.

## Core idea

Strategy is not a feature list. It is the durable answer to:

- What problem matters?
- Who is it for?
- What approach are we taking?
- How will we know it works?
- What work tracks are active?
- What are we intentionally not doing?

## Flow

1. Read existing `STRATEGY.md` if present.
2. If creating it for the first time, interview the user section by section.
3. If updating, summarize the existing strategy and ask which section to revisit.
4. Push back on weak answers:
   - vague user segments
   - metrics that are vanity or not measurable
   - approach statements that are just feature lists
   - tracks that are too many or too granular
5. For Agent products, always capture Agent-native assumptions.
6. Write or update `STRATEGY.md`.
7. End by naming which downstream skill should run next.

If arguments include `~html`, enter HTML decision mode instead of writing
`STRATEGY.md`. Use this only for major strategy revisions that benefit from
browser-based comparison and editing. Read `references/html-decision-mode.md`,
generate a compact decision model under `docs/.compound-lite/drafts/strategy/`,
run `tools/render_compound_html.py`, and stop after telling the user where to
open the editor. The exported Markdown from that editor is the strategy artifact
the user can apply to `STRATEGY.md`.

## STRATEGY.md structure

```md
# Strategy

last_updated:

## Target problem
## Approach
## Primary users
## Key metrics
## Tracks
## Not working on
## Agent-native assumptions
## Current state snapshot
```

## Non-goals

- Do not write requirements documents.
- Do not write implementation plans.
- Do not update issue trackers.
- Do not change code.
- Do not create `cl-finalize`, `~import`, or `~html-only` flows.

Read `references/strategy-interview.md` and `references/agent-native-lens.md` before interviewing. When using `~html`, also read `references/html-decision-mode.md`.
