#!/bin/bash
# push-to-github.sh — 上传 agent-sovereignty-rules 到 GitHub
set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

REPO_NAME="agent-sovereignty-rules"
GITHUB_USER="${GITHUB_USER:-billgaohub}"

echo "=== 上传 $REPO_NAME 到 GitHub ==="

if ! git remote -v | grep -q origin; then
    gh repo create "$REPO_NAME" --public --source=. --push || true
else
    echo "✓ Git remote 已配置: $(git remote get-url origin)"
    echo "请手动 push 或修改 remote 后执行: git push -u origin main"
fi

echo "=== 完成 ==="
