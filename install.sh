#!/usr/bin/env bash
# 彩星电影一号位 - 一键安装 (macOS / Linux)
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main"
SKILL_DIR="${HOME}/.workbuddy/skills/caixing-film-one"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "==> 彩星电影一号位 安装程序"
echo "    目标目录: $SKILL_DIR"

mkdir -p "$TMP/caixing-film-one"
for f in \
  SKILL.md README.md README.en.md LICENSE \
  references/chow-playbook.md \
  references/three-roles.md \
  references/creation-workflows.md \
  references/network-playbook.md \
  references/evaluation-rubric.md \
  references/rights-and-safety.md \
  references/source-registry.json \
  scripts/source_validator.py \
  scripts/quote_guard.py \
  scripts/evaluate_output.py \
  scripts/classic_score.py \
  examples/sample-workflow.md \
  tests/validate_skill.py; do
  mkdir -p "$TMP/caixing-film-one/$(dirname "$f")"
  curl -fsSL "$REPO_RAW/$f" -o "$TMP/caixing-film-one/$f"
done

mkdir -p "$(dirname "$SKILL_DIR")"
if [ -d "$SKILL_DIR" ]; then
  echo "==> 检测到已安装，先备份旧版本"
  mv "$SKILL_DIR" "${SKILL_DIR}.bak.$(date +%Y%m%d%H%M%S)"
fi
cp -R "$TMP/caixing-film-one" "$SKILL_DIR"

echo "==> 安装完成: $SKILL_DIR"
echo "==> 请重启 WorkBuddy 会话后使用。"
