#!/usr/bin/env bash
# 彩星电影一号位 - 一键安装 (macOS / Linux)
# 走 git clone，规避国内 raw.githubusercontent.com 不可达的问题
set -euo pipefail

REPO="https://github.com/SimonsTang/caixing-film-one.git"
SKILL_DIR="${HOME}/.workbuddy/skills/caixing-film-one"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "==> 彩星电影一号位 安装程序"
echo "    目标目录: $SKILL_DIR"

if ! command -v git >/dev/null 2>&1; then
  echo "错误: 需要 git，请先安装。" >&2
  exit 1
fi

git clone --depth 1 "$REPO" "$TMP/caixing-film-one"

mkdir -p "$(dirname "$SKILL_DIR")"
if [ -d "$SKILL_DIR" ]; then
  echo "==> 检测到已安装，先备份旧版本"
  mv "$SKILL_DIR" "${SKILL_DIR}.bak.$(date +%Y%m%d%H%M%S)"
fi
cp -R "$TMP/caixing-film-one" "$SKILL_DIR"
rm -rf "$SKILL_DIR/.git"   # 安装为技能，不需要仓库历史

echo "==> 安装完成: $SKILL_DIR"
echo "==> 请重启 WorkBuddy 会话后使用。"
