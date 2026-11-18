#!/usr/bin/env python3
"""Flag near-duplicate n-grams between a candidate script and lawfully supplied references.

This is a human-review aid. It does not determine infringement.
"""
import argparse
import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[\s\u3000]+", "", text)
    text = re.sub(r'[，。！？、；：“”‘’《》()（）\[\]【】,.!?;:_\-]', '', text)
    return text


def ngrams(text: str, n: int) -> set[str]:
    return {text[i:i + n] for i in range(max(0, len(text) - n + 1))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--references", required=True)
    parser.add_argument("--n", type=int, default=12)
    parser.add_argument("--threshold", type=int, default=3,
                        help="minimum number of shared n-grams to report")
    args = parser.parse_args()

    candidate_path = Path(args.candidate)
    references_path = Path(args.references)
    for path in (candidate_path, references_path):
        if not path.is_file():
            print(f"ERROR: missing file: {path}", file=sys.stderr)
            return 2

    candidate = normalize(candidate_path.read_text(encoding="utf-8", errors="ignore"))
    references = normalize(references_path.read_text(encoding="utf-8", errors="ignore"))

    if len(candidate) < args.n or len(references) < args.n:
        print("SKIP: text shorter than n-gram size")
        return 0

    shared = ngrams(candidate, args.n) & ngrams(references, args.n)
    if len(shared) < args.threshold:
        print(f"PASS: {len(shared)} shared {args.n}-gram(s), below threshold {args.threshold}")
        return 0

    print(f"REVIEW: {len(shared)} shared {args.n}-gram(s) (threshold {args.threshold})")
    for gram in sorted(shared)[:20]:
        print(f"  - {gram}")
    print("Manual review required. This tool does not give a legal conclusion.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
