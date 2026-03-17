#!/bin/bash
# GitHub推送脚本
# 自动推送到 https://github.com/luminaryjoe/iwantek-seo

set -e

echo "=================================="
echo "  GitHub推送脚本"
echo "=================================="
echo ""

# 配置
REPO_URL="https://github.com/luminaryjoe/iwantek-seo.git"
PROJECT_DIR="/root/.openclaw/workspace/digital-products/salary-database"

cd "$PROJECT_DIR"

echo "📁 当前目录: $(pwd)"
echo ""

# 检查git状态
echo "🔍 检查Git状态..."
git status
echo ""

# 添加所有文件
echo "📦 添加文件到Git..."
git add -A
echo "✅ 文件已添加"
echo ""

# 提交更改
echo "💾 提交更改..."
git commit -m "Add AI/ML Salary Database MVP

- 100+ verified salary data points from top tech companies
- Companies: OpenAI, Google, Meta, Amazon, NVIDIA, etc.
- Average base: $209K, Average total comp: $369K
- Includes Notion template, sales page, and launch checklist
- Ready for Gumroad launch

Files:
- data/salary_data.csv (100 records)
- data/salary_data.json
- output/statistics.json
- output/NOTION-TEMPLATE.md
- output/SALES-PAGE.md
- scripts/collect-data.py
- PRODUCT-SPEC.md
- LAUNCH-CHECKLIST.md
- README.md" || echo "⚠️  没有新更改需要提交"
echo ""

# 配置远程仓库
echo "🔗 配置远程仓库..."
git remote set-url origin "$REPO_URL"
git remote -v
echo ""

# 推送代码
echo "🚀 推送到GitHub..."
echo "远程仓库: $REPO_URL"
echo ""

# 尝试推送
git push -u origin master || {
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因:"
    echo "1. 需要GitHub认证 (用户名/密码或Token)"
    echo "2. 网络连接问题"
    echo "3. 权限不足"
    echo ""
    echo "解决方案:"
    echo "1. 使用SSH密钥认证"
    echo "2. 使用Personal Access Token"
    echo "3. 手动在本地推送"
    echo ""
    exit 1
}

echo ""
echo "✅ 推送成功!"
echo ""
echo "🌐 GitHub链接:"
echo "   $REPO_URL"
echo ""
echo "📊 提交记录:"
git log --oneline -3
echo ""
