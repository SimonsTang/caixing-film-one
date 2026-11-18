#!/usr/bin/env python3
"""Structural validation for the caixing-film-one skill package."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = [
    "SKILL.md",
    "README.md",
    "references/chow-playbook.md",
    "references/creation-workflows.md",
    "references/evaluation-rubric.md",
    "references/network-playbook.md",
    "references/rights-and-safety.md",
    "references/source-registry.json",
    "references/three-roles.md",
    "scripts/classic_score.py",
    "scripts/evaluate_output.py",
    "scripts/quote_guard.py",
    "scripts/source_validator.py",
    "examples/sample-workflow.md",
]

SKILL_MARKERS = [
    "彩星电影一号位",
    "编剧",
    "制片",
    "导演",
    "规则冲突",
    "情感反冲",
    "道具回收",
    "网络",
    "硬失败",
]


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def main() -> int:
    failures: list[str] = []

    for rel in EXPECTED_FILES:
        if not (ROOT / rel).is_file():
            failures.append(f"missing file: {rel}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").is_file() else ""
    for marker in SKILL_MARKERS:
        if marker not in skill:
            failures.append(f"SKILL.md missing marker: {marker}")

    try:
        json.loads((ROOT / "references" / "source-registry.json").read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"source-registry.json invalid: {exc}")

    if sys.version_info < (3, 8):
        failures.append("Python 3.8+ required")

    checks = [
        [sys.executable, "scripts/source_validator.py"],
        [sys.executable, "scripts/classic_score.py", "--input", "examples/sample-workflow.md"],
        [sys.executable, "scripts/evaluate_output.py", "--input", "examples/sample-workflow.md"],
    ]
    for cmd in checks:
        code, output = run(cmd)
        print(f"$ {' '.join(cmd)}\n{output}\n")
        if code != 0:
            failures.append(f"command failed: {' '.join(cmd)}")

    if failures:
        print("FAILED")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
