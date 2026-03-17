# 行业薪资数据库 - 产品规格

## 产品概述

| 属性 | 详情 |
|------|------|
| **产品名称** | Tech Salary Database 2024 |
| **目标市场** | 科技行业从业者、HR、猎头、求职者 |
| **售价** | $99 (基础版) / $299 (专业版) |
| **形态** | Notion数据库 + Airtable + PDF报告 |
| **制作周期** | 1周 |
| **预期收入** | $500-2000/月 (3个月内) |

---

## 为什么这个产品

### 第一性原理
```
问题: 科技行业薪资不透明，谈判困难

现有方案:
- Levels.fyi: 程序员为主，$29/月订阅
- Glassdoor: 免费但数据旧、不准确
- 猎头: 贵，信息不全面

缺口:
- 细分领域薪资数据缺失
- 实时更新需求
- 个性化查询

解决方案:
- 细分行业薪资数据库
- 一次性购买，终身更新
- 多维度查询筛选
```

### 商业判断
| 因素 | 分析 |
|------|------|
| **市场规模** | 全球科技从业者3000万+ |
| **付费意愿** | 高 (薪资谈判ROI明显) |
| **竞争** | 低 (细分领域空白) |
| **制作成本** | 低 (公开数据+AI整理) |
| **利润率** | 95%+ (数字产品) |

---

## 产品规格

### 基础版 ($99)

**包含内容**:
- 10,000+ 薪资数据点
- 5个主要科技城市
- 3个经验级别 (初级/中级/高级)
- 50+ 职位类别
- Notion数据库格式
- 基础筛选功能
- PDF摘要报告

**数据来源**:
- Levels.fyi (公开数据)
- LinkedIn Salary Insights
- Indeed Salary Estimates
- AngelList (创业公司)
- 公司招聘网站

### 专业版 ($299)

**额外内容**:
- 50,000+ 薪资数据点
- 全球20+ 科技中心
- 股权/期权估值
- 福利对比 (保险/假期/远程)
- 谈判脚本模板
- 薪资计算器 (Excel)
- 季度更新
- 1对1咨询 (30分钟)

---

## 细分行业选择

### 推荐细分领域 (按优先级)

| 优先级 | 领域 | 为什么 | 数据来源 |
|--------|------|--------|----------|
| **P0** | AI/ML工程师 |  hottest, 薪资高 | Levels.fyi, LinkedIn |
| **P0** | 远程工作薪资 | 趋势, 数据稀缺 | RemoteOK, FlexJobs |
| **P0** | 数据工程师 | 需求大, 细分少 | LinkedIn, Indeed |
| **P1** | 产品经理 | 决策需要 | Product School, LinkedIn |
| **P1** | UX设计师 | 创意行业 | Dribbble, Behance |
| **P1** | 安全工程师 | 紧缺, 薪资高 | CyberSec jobs |
| **P2** | DevOps | 基础设施 | StackOverflow Jobs |
| **P2** | 区块链开发 | 新兴, 波动大 | Crypto jobs |

### MVP选择

**推荐: AI/ML工程师薪资数据库**

原因:
- 最热门领域
- 薪资最高
- 数据相对丰富
- 付费意愿最强

---

## 数据结构

### 数据库字段

```json
{
  "id": "uuid",
  "company": "OpenAI",
  "company_size": "100-500",
  "company_stage": "Series C",
  "location": "San Francisco, CA",
  "country": "USA",
  "region": "North America",
  "remote_policy": "Hybrid",
  "title": "Senior ML Engineer",
  "level": "L5",
  "years_experience": 5,
  "years_at_company": 2,
  "base_salary": 250000,
  "currency": "USD",
  "equity": 500000,
  "equity_vesting": "4 years",
  "bonus": 50000,
  "signing_bonus": 50000,
  "total_comp": 350000,
  "benefits": ["Health", "Dental", "Vision", "401k", "Unlimited PTO"],
  "skills": ["Python", "PyTorch", "LLM", "MLOps"],
  "education": "MS Computer Science",
  "date_reported": "2024-03",
  "source": "Levels.fyi",
  "verified": true
}
```

### 筛选维度

**基础筛选**:
- 公司 (搜索/多选)
- 地点 (城市/国家/区域)
- 职位 (搜索/分类)
- 经验年限 (范围)
- 薪资范围 (滑动条)

**高级筛选** (专业版):
- 公司规模
- 融资阶段
- 远程政策
- 技能要求
- 教育背景
- 报告时间范围

---

## 制作流程

### Day 1: 数据收集 (4小时)

**任务**:
1. 爬取 Levels.fyi AI/ML数据
2. 收集LinkedIn Salary Insights
3. 整理Indeed/AngelList数据
4. 去重和清洗

**工具**:
- firecrawl-skills (网页抓取)
- Python pandas (数据清洗)
- OpenAI API (数据标准化)

### Day 2: 数据分析 (3小时)

**任务**:
1. 统计分析 (均值/中位数/分位数)
2. 可视化 (图表生成)
3. 趋势分析 (同比/环比)
4. 洞察提取

**输出**:
- 统计摘要
- 可视化图表
- 趋势报告

### Day 3: 产品制作 (3小时)

**任务**:
1. Notion数据库搭建
2. Airtable导入
3. 筛选视图设置
4. PDF报告制作

**工具**:
- Notion
- Airtable
- Canva (PDF设计)

### Day 4: 销售页面 (2小时)

**任务**:
1. Gumroad产品页
2. 产品介绍文案
3. 定价设置
4. 预览图制作

### Day 5: 发布推广 (2小时)

**任务**:
1. Product Hunt发布
2. Reddit社区分享
3. LinkedIn推广
4. Twitter宣传

---

## 技术实现

### 数据收集脚本

```python
# data_collector.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def scrape_levels_fyi():
    """爬取Levels.fyi数据"""
    url = "https://www.levels.fyi/t/software-engineer/focus/ai-machine-learning"
    # 使用firecrawl或requests
    pass

def scrape_linkedin():
    """LinkedIn Salary Insights"""
    pass

def clean_data(raw_data):
    """数据清洗"""
    df = pd.DataFrame(raw_data)
    # 去重
    # 标准化
    # 验证
    return df

def export_to_notion(df):
    """导出到Notion"""
    pass

def export_to_airtable(df):
    """导出到Airtable"""
    pass

if __name__ == "__main__":
    raw_data = scrape_levels_fyi()
    clean_df = clean_data(raw_data)
    export_to_notion(clean_df)
    export_to_airtable(clean_df)
```

### Notion模板

```
Database: AI/ML Salary Database 2024

Views:
- All Data (默认)
- By Company (按公司分组)
- By Location (按地点筛选)
- By Level (按级别分组)
- High Paying (薪资>300k)
- Remote Friendly (远程友好)
- Recently Reported (最近报告)

Properties:
- Company (Title)
- Title (Select)
- Location (Select)
- Base Salary (Number)
- Total Comp (Number)
- Experience (Number)
- Skills (Multi-select)
- Date (Date)
- Source (URL)
```

---

## 销售策略

### 定价策略

| 版本 | 价格 | 内容 | 目标 |
|------|------|------|------|
| **基础版** | $99 | 10k数据, 基础筛选 | 个人用户 |
| **专业版** | $299 | 50k数据, 高级功能 | 企业/HR |
| **企业版** | $999 | 定制数据, API访问 | 猎头公司 |

### 促销策略

**早鸟价**:
- 前100名: 50% off ($49)
- 101-500名: 30% off ($69)
- 之后: 原价 $99

**捆绑销售**:
- 薪资数据库 + 谈判指南: $129
- 薪资数据库 + 简历模板: $119

### 销售渠道

1. **Gumroad** (主要)
2. **Product Hunt** (曝光)
3. **个人网站**
4. **社交媒体** (Twitter/LinkedIn)
5. **Reddit社区** (r/cscareerquestions, r/datascience)

---

## 风险与缓解

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| **数据准确性** | 中 | 高 | 多源验证, 用户反馈 |
| **法律合规** | 低 | 高 | 免责声明, 公开数据 |
| **竞争加剧** | 中 | 中 | 持续更新, 深度细分 |
| **数据过时** | 高 | 中 | 季度更新, 订阅模式 |

---

## 成功指标

### 短期 (1个月)
- [ ] 产品上线
- [ ] 100个付费用户
- [ ] $5000收入

### 中期 (3个月)
- [ ] 1000个用户
- [ ] $20000收入
- [ ] 扩展到3个细分领域

### 长期 (12个月)
- [ ] 10000个用户
- [ ] $100000收入
- [ ] 建立薪资数据平台

---

## 立即执行

### 今天 (4小时)
- [ ] 爬取Levels.fyi数据
- [ ] 收集LinkedIn数据
- [ ] 数据清洗

### 明天 (3小时)
- [ ] 数据分析
- [ ] 可视化制作
- [ ] Notion数据库搭建

### 后天 (3小时)
- [ ] PDF报告制作
- [ ] Gumroad产品页
- [ ] 定价设置

### 第4天 (2小时)
- [ ] Product Hunt准备
- [ ] 社媒文案
- [ ] 发布推广

**总投入: 12小时**
**预期产出: MVP产品**

---

**准备好开始制作AI/ML薪资数据库MVP吗?**
