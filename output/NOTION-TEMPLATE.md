# Notion数据库模板

## AI/ML Salary Database 2024

### 数据库设置

**标题**: AI/ML Salary Database 2024

**属性**:
1. **Company** (Title) - 公司名称
2. **Title** (Select) - 职位
   - Machine Learning Engineer
   - AI Research Scientist
   - Deep Learning Engineer
   - NLP Engineer
   - MLOps Engineer
3. **Location** (Select) - 地点
   - San Francisco, CA
   - New York, NY
   - Seattle, WA
   - Boston, MA
   - Austin, TX
   - Remote
   - London, UK
   - Toronto, Canada
4. **Level** (Select) - 级别
   - L3
   - L4
   - L5
   - L6
   - Staff
5. **Base Salary** (Number) - 基本工资
6. **Total Comp** (Number) - 总包
7. **Years Experience** (Number) - 经验年限
8. **Company Size** (Select) - 公司规模
   - 100-500
   - 1000-5000
   - 10000+
9. **Remote Policy** (Select) - 远程政策
   - On-site
   - Hybrid
   - Remote
10. **Skills** (Multi-select) - 技能
    - Python
    - PyTorch
    - TensorFlow
    - LLM
    - NLP
    - Computer Vision
11. **Date Reported** (Date) - 报告日期
12. **Source** (URL) - 数据来源
13. **Verified** (Checkbox) - 已验证

### 视图设置

**1. All Data (默认视图)**
- 表格视图
- 显示所有属性

**2. By Company (按公司分组)**
- 分组: Company
- 排序: Total Comp (降序)

**3. By Location (按地点筛选)**
- 筛选: Location
- 排序: Total Comp (降序)

**4. High Paying (高薪职位)**
- 筛选: Total Comp > 300000
- 排序: Total Comp (降序)

**5. Remote Friendly (远程友好)**
- 筛选: Remote Policy = Remote
- 排序: Total Comp (降序)

**6. Recently Reported (最近报告)**
- 筛选: Date Reported > 2024-01-01
- 排序: Date Reported (降序)

**7. By Level (按级别分组)**
- 分组: Level
- 排序: Total Comp (降序)

### 导入数据步骤

1. 打开Notion，创建新页面
2. 添加Database (Table)
3. 设置上述属性
4. 点击 "..." → Import → CSV
5. 选择 `salary_data.csv`
6. 映射字段
7. 完成导入

### 使用技巧

**筛选**:
- 点击筛选图标
- 选择属性
- 设置条件

**排序**:
- 点击列标题
- 选择升序/降序

**分组**:
- 点击 "Group by"
- 选择分组属性

**公式** (可选):
```
Total Comp / 1000  # 显示为K
```

---

## 产品交付物

### 基础版 ($99)
- Notion数据库模板
- 100条数据记录
- CSV文件
- PDF摘要报告

### 专业版 ($299)
- Notion数据库
- Airtable数据库
- 1000+条数据记录
- Excel薪资计算器
- 谈判脚本模板
- 季度更新

---

## 下一步

1. 创建Notion数据库
2. 导入CSV数据
3. 设置视图
4. 生成PDF报告
5. 搭建销售页面
