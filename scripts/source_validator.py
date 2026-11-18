#!/usr/bin/env python3
"""Validate references/source-registry.json structure and field sanity."""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {"id", "title", "publisher", "url", "source_type", "confidence", "topics"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read/parse {path}: {exc}"]

    if not isinstance(data, dict):
        return ["registry root must be an object"]

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return ["registry must contain a non-empty 'sources' array"]

    seen: set[str] = set()
    for index, item in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        missing = REQUIRED - item.keys()
        if missing:
            errors.append(f"{prefix}: missing {sorted(missing)}")
            continue
        sid = item["id"]
        if sid in seen:
            errors.append(f"{prefix}: duplicate id '{sid}'")
        seen.add(sid)
        parsed = urlparse(str(item["url"]))
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{prefix}: invalid url '{item['url']}'")
        confidence = item["confidence"]
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"{prefix}: confidence must be between 0 and 1")
        if not isinstance(item["topics"], list) or not item["topics"]:
            errors.append(f"{prefix}: topics must be a non-empty array")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "references" / "source-registry.json"
    errors = validate(path)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"  - {error}")
        return 1
    count = len(json.loads(path.read_text(encoding="utf-8"))["sources"])
    print(f"VALID: {count} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
