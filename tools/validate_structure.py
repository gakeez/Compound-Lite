#!/usr/bin/env python3
"""Validate that a repository contains the expected Compound Lite structure."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "STRATEGY.md",
    ".agents/skills/cl-onboard/SKILL.md",
    ".agents/skills/cl-strategy/SKILL.md",
    ".agents/skills/cl-ideate/SKILL.md",
    ".agents/skills/cl-brainstorm/SKILL.md",
    ".agents/skills/cl-design/SKILL.md",
    ".agents/skills/cl-review/SKILL.md",
    ".agents/skills/cl-plan/SKILL.md",
    ".agents/skills/cl-work/SKILL.md",
    ".agents/skills/cl-verify/SKILL.md",
    ".agents/skills/cl-debug/SKILL.md",
    ".agents/skills/cl-compound/SKILL.md",
    ".agents/skills/cl-product-pulse/SKILL.md",
    ".agents/skills/cl-render/SKILL.md",
    ".agents/skills/cl-strategy/references/html-decision-mode.md",
    ".agents/skills/cl-ideate/references/html-decision-mode.md",
    ".agents/skills/cl-brainstorm/references/html-decision-mode.md",
    ".agents/skills/cl-plan/references/html-decision-mode.md",
    ".agents/skills/cl-verify/references/html-decision-mode.md",
    "tools/render_compound_html.py",
    "docs/ideation/README.md",
    "docs/brainstorms/README.md",
    "docs/designs/README.md",
    "docs/plans/README.md",
    "docs/solutions/README.md",
    "docs/pulse-reports/README.md",
    "docs/evals/README.md",
    "docs/.compound-lite/README.md",
    "docs/.compound-lite/drafts/README.md",
    "docs/.compound-lite/views/README.md",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.target).resolve()
    missing = [p for p in REQUIRED if not (root / p).exists()]
    if missing:
        print("Missing Compound Lite files:")
        for p in missing:
            print(f"- {p}")
        raise SystemExit(1)
    print("Compound Lite structure looks complete.")


if __name__ == "__main__":
    main()
