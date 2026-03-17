# GitHub推送指南

## 目标仓库
```
https://github.com/luminaryjoe/iwantek-seo
```

---

## 方法: 手动推送 (推荐)

### 步骤1: 在本地电脑准备

**1.1 克隆目标仓库**
```bash
git clone https://github.com/luminaryjoe/iwantek-seo.git
cd iwantek-seo
```

**1.2 创建项目目录**
```bash
mkdir -p ai-ml-salary-database
cd ai-ml-salary-database
```

---

### 步骤2: 复制文件

**从服务器复制以下文件到本地 `ai-ml-salary-database/` 目录：**

```
ai-ml-salary-database/
├── data/
│   ├── salary_data.csv          (100条薪资数据)
│   └── salary_data.json         (JSON格式)
├── output/
│   ├── statistics.json          (统计分析)
│   ├── NOTION-TEMPLATE.md       (Notion模板指南)
│   └── SALES-PAGE.md            (销售页面文案)
├── scripts/
│   └── collect-data.py          (数据收集脚本)
├── PRODUCT-SPEC.md              (产品规格)
├── LAUNCH-CHECKLIST.md          (发布检查清单)
└── README.md                    (项目说明)
```

**获取文件方式：**

**方式A: SCP下载 (推荐)**
```bash
# 在本地电脑执行
scp -r root@YOUR_SERVER_IP:/root/.openclaw/workspace/digital-products/salary-database/* ./ai-ml-salary-database/
```

**方式B: 压缩下载**
```bash
# 在服务器执行
cd /root/.openclaw/workspace/digital-products
tar -czvf salary-database.tar.gz salary-database/

# 然后下载 salary-database.tar.gz
```

**方式C: 复制粘贴**
```bash
# 查看文件内容
cat /root/.openclaw/workspace/digital-products/salary-database/data/salary_data.csv
# 复制内容到本地文件
```

---

### 步骤3: 提交并推送

**3.1 添加文件到Git**
```bash
cd iwantek-seo

# 复制文件到仓库
cp -r ../ai-ml-salary-database/* .

# 查看状态
git status
```

**3.2 提交更改**
```bash
# 添加所有文件
git add .

# 提交
git commit -m "Add AI/ML Salary Database MVP

- 100+ verified salary data points
- Data from top tech companies (OpenAI, Google, Meta, etc.)
- Average base: $209K, Average total comp: $369K
- Includes Notion template, sales page, and launch checklist
- Ready for Gumroad launch"
```

**3.3 推送到GitHub**
```bash
git push origin master

# 或如果你使用 main 分支
git push origin main
```

---

### 步骤4: 验证推送

**4.1 访问GitHub**
```
https://github.com/luminaryjoe/iwantek-seo
```

**4.2 确认文件已上传**
- [ ] data/salary_data.csv
- [ ] data/salary_data.json
- [ ] output/statistics.json
- [ ] output/NOTION-TEMPLATE.md
- [ ] output/SALES-PAGE.md
- [ ] scripts/collect-data.py
- [ ] PRODUCT-SPEC.md
- [ ] LAUNCH-CHECKLIST.md
- [ ] README.md

---

## 快捷命令汇总

```bash
# 1. 克隆仓库
git clone https://github.com/luminaryjoe/iwantek-seo.git
cd iwantek-seo

# 2. 创建目录
mkdir -p ai-ml-salary-database

# 3. 复制文件 (从服务器下载后)
cp -r /path/to/downloaded/salary-database/* ai-ml-salary-database/

# 4. 移动到仓库根
cp -r ai-ml-salary-database/* .

# 5. 提交推送
git add .
git commit -m "Add AI/ML Salary Database MVP"
git push origin master
```

---

## 推送后操作

### 1. 验证GitHub链接
访问: `https://github.com/luminaryjoe/iwantek-seo`

### 2. 继续发布流程
- [ ] 创建Notion数据库
- [ ] 注册Gumroad
- [ ] 发布产品
- [ ] 推广营销

---

## 故障排除

### 问题: 权限拒绝
**解决:**
```bash
# 检查GitHub登录状态
git config --global user.name
git config --global user.email

# 重新配置
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 问题: 合并冲突
**解决:**
```bash
# 先拉取最新代码
git pull origin master

# 解决冲突后重新推送
git push origin master
```

### 问题: 大文件上传失败
**解决:**
```bash
# 使用Git LFS (如需要)
git lfs track "*.csv"
git add .gitattributes
git add data/salary_data.csv
git commit -m "Add large CSV file"
git push origin master
```

---

## 完成标准

✅ **推送成功标志:**
1. 访问 `https://github.com/luminaryjoe/iwantek-seo`
2. 能看到所有文件
3. 提交记录显示 "Add AI/ML Salary Database MVP"
4. README.md 正确渲染

---

**立即开始手动推送?**
