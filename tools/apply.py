#!/usr/bin/env python3
"""Apply the Compound Lite template to a target repository.

The script is conservative:
- It creates missing files and directories.
- It does not overwrite existing files unless --overwrite is passed.
- Conflicting files are copied into .compound-lite-incoming/ for manual merge.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template"


def should_skip_template_file(src: Path) -> bool:
    rel = src.relative_to(TEMPLATE)
    return (
        "__pycache__" in rel.parts
        or src.suffix == ".pyc"
        or src.name == ".DS_Store"
    )


def copy_file(src: Path, dest: Path, overwrite: bool, incoming_root: Path) -> tuple[str, Path]:
    rel = src.relative_to(TEMPLATE)
    if dest.exists() and not overwrite:
        incoming = incoming_root / rel
        incoming.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, incoming)
        return "conflict", incoming
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return "copied" if not dest.exists() else "overwritten", dest


def apply(target: Path, mode: str, overwrite: bool) -> None:
    if mode == "new":
        target.mkdir(parents=True, exist_ok=True)
    elif not target.exists():
        raise SystemExit(f"Target does not exist for --mode existing: {target}")

    incoming_root = target / ".compound-lite-incoming"
    copied = []
    conflicts = []

    for src in TEMPLATE.rglob("*"):
        if src.is_dir():
            continue
        if should_skip_template_file(src):
            continue
        rel = src.relative_to(TEMPLATE)
        dest = target / rel
        status, out = copy_file(src, dest, overwrite, incoming_root)
        if status == "conflict":
            conflicts.append((rel, out))
        else:
            copied.append((rel, out))

    print("Compound Lite applied.")
    print(f"Target: {target}")
    print(f"Mode: {mode}")
    print(f"Files copied/overwritten: {len(copied)}")
    print(f"Conflicts staged for manual merge: {len(conflicts)}")

    if conflicts:
        print("\nConflicts:")
        for rel, out in conflicts:
            print(f"- {rel} -> {out.relative_to(target)}")
        print("\nMerge these files manually, then remove .compound-lite-incoming/ when done.")

    print("\nNext steps:")
    print("1. Open the target repo in Codex.")
    if mode == "existing":
        print("2. Run: $cl-onboard")
    else:
        print("2. Run: $cl-strategy")
    print("3. Keep automation at Level 1: no automatic commit/push/PR/deploy.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply Compound Lite to a repository.")
    parser.add_argument("target", help="Target repository or project directory")
    parser.add_argument("--mode", choices=["new", "existing"], default="existing")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files instead of staging conflicts")
    args = parser.parse_args()
    apply(Path(args.target).resolve(), args.mode, args.overwrite)


if __name__ == "__main__":
    main()
