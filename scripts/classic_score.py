#!/usr/bin/env python3
"""Score the presence of classic-making elements in a draft.

Heuristic checklist derived from the distilled Chow playbook. Not a substitute
for human judgment; designed to catch missing structure, not measure talent.
"""
import argparse
import sys
from pathlib import Path

CHECKS = {
    "底层欲望": ["想", "要", "保住", "渴望", "希望"],
    "世界规则": ["规则", "制度", "规定", "系统", "大家都"],
    "地位图": ["地位", "低", "被看", "底层", "临时", "被低估"],
    "升级链": ["升级", "第一次", "第二次", "第三次", "变本加厉"],
    "角色选择": ["选择", "决定", "偷偷", "他以为", "因为"],
    "反转": ["反转", "没想到", "原来", "以为", "误解"],
    "道具回收": ["回收", "又出现", "重新出现", "还在", "回到"],
    "情感反冲": ["沉默", "眼泪", "纸条", "拥抱", "眼眶", "说不出"],
    "记忆点": ["截图", "评论", "模仿", "争议", "金句"],
    "锋利度": ["不舒服", "代价", "没有结局", "仍然", "照常", "不圆满"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    path = Path(args.input)
    if not path.is_file():
        print(f"ERROR: missing file: {path}", file=sys.stderr)
        return 2
    text = path.read_text(encoding="utf-8", errors="ignore")

    results = {name: any(word in text for word in words) for name, words in CHECKS.items()}
    score = sum(results.values())
    total = len(CHECKS)
    print(f"Classic-element coverage: {score}/{total}")
    for name, ok in results.items():
        print(f"  [{'x' if ok else ' '}] {name}")
    if score < 7:
        print("WARN: too few classic elements. Add the missing ones before release.")
        return 1
    print("PASS: core classic structure present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
