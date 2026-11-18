#!/usr/bin/env python3
"""Structural scoring for a generated script. Heuristic, not a quality oracle."""
import argparse
import re
import sys
from pathlib import Path

SECTIONS = {
    "premise": [r"前提", r"一句话", r"premise"],
    "mechanism": [r"机制", r"mechanism"],
    "beats": [r"节拍", r"建立", r"规则", r"升级", r"反转", r"回收", r"beat"],
    "dialogue": [r"对白", r"台词", r"dialogue"],
    "directing": [r"镜头", r"表演", r"景别", r"shot", r"direct"],
    "producer": [r"可行", r"预算", r"场景", r"制片", r"budget"],
    "network": [r"钩子", r"传播", r"平台", r"记忆点", r"short video"],
    "originality": [r"原创", r"权利", r"独立表达", r"original"],
}

MECHANISMS = [
    "地位反转", "规则冲突", "类型错置", "重复", "延迟后果", "道具回收",
    "情感反冲", "字面执行", "错位的尊严", "冒牌专家", "藏起来的温柔", "公开",
]


def present(text: str, patterns: list[str]) -> bool:
    lowered = text.lower()
    return any(re.search(p, lowered) for p in patterns)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--mode", default="script", choices=["script", "research"])
    args = parser.parse_args()

    path = Path(args.input)
    if not path.is_file():
        print(f"ERROR: missing file: {path}", file=sys.stderr)
        return 2
    text = path.read_text(encoding="utf-8", errors="ignore")

    if args.mode == "research":
        needed = {
            "结论": [r"结论", r"conclusion"],
            "已核事实": [r"事实", r"fact"],
            "解读": [r"解读", r"interpretation"],
            "不确定": [r"不确定", r"uncertain"],
            "来源": [r"来源", r"source", r"http"],
        }
        score = sum(present(text, patterns) for patterns in needed.values())
        print(f"Research sections: {score}/{len(needed)}")
        return 0 if score >= 4 else 1

    hits = {name: present(text, patterns) for name, patterns in SECTIONS.items()}
    score = sum(hits.values())
    mech_hits = [m for m in MECHANISMS if m in text]
    print(f"Script sections: {score}/{len(SECTIONS)}")
    for name, ok in hits.items():
        print(f"  [{'x' if ok else ' '}] {name}")
    print(f"Mechanisms referenced: {len(mech_hits)} ({', '.join(mech_hits) or 'none'})")
    if score < 6:
        print("WARN: below delivery bar. Add missing sections before release.")
        return 1
    print("PASS: structural minimum met. Manual rubric scoring still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
