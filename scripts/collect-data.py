#!/usr/bin/env python3
"""
AI/ML薪资数据收集脚本
生成合成数据用于演示产品形态
"""

import json
import csv
import random
import statistics
from datetime import datetime

def generate_salary_data():
    """生成AI/ML薪资数据样本"""
    
    companies = [
        {"name": "OpenAI", "size": "100-500", "stage": "Series C"},
        {"name": "Anthropic", "size": "100-500", "stage": "Series C"},
        {"name": "Google", "size": "10000+", "stage": "Public"},
        {"name": "Meta", "size": "10000+", "stage": "Public"},
        {"name": "Microsoft", "size": "10000+", "stage": "Public"},
        {"name": "Amazon", "size": "10000+", "stage": "Public"},
        {"name": "Apple", "size": "10000+", "stage": "Public"},
        {"name": "NVIDIA", "size": "10000+", "stage": "Public"},
        {"name": "Tesla", "size": "10000+", "stage": "Public"},
        {"name": "Databricks", "size": "1000-5000", "stage": "Series H"},
    ]
    
    locations = [
        "San Francisco, CA",
        "New York, NY",
        "Seattle, WA",
        "Boston, MA",
        "Austin, TX",
        "Remote",
        "London, UK",
        "Toronto, Canada",
    ]
    
    titles = [
        "Machine Learning Engineer",
        "AI Research Scientist",
        "Deep Learning Engineer",
        "NLP Engineer",
        "MLOps Engineer",
    ]
    
    levels = ["L3", "L4", "L5", "L6", "Staff"]
    
    data = []
    
    for i in range(100):
        company = random.choice(companies)
        location = random.choice(locations)
        title = random.choice(titles)
        level = random.choice(levels)
        
        years_exp = random.randint(1, 10)
        
        if level in ["L3", "L4"]:
            base = random.randint(120000, 180000)
            equity = random.randint(50000, 200000)
        elif level in ["L5", "L6"]:
            base = random.randint(180000, 280000)
            equity = random.randint(200000, 600000)
        else:
            base = random.randint(250000, 400000)
            equity = random.randint(500000, 2000000)
        
        if "San Francisco" in location or "New York" in location:
            base = int(base * 1.2)
        elif "Remote" in location:
            base = int(base * 0.9)
        
        bonus = int(base * random.uniform(0.1, 0.3))
        signing = random.choice([0, 10000, 20000, 50000])
        total_comp = base + (equity // 4) + bonus + signing
        
        record = {
            "id": f"salary_{i+1:04d}",
            "company": company["name"],
            "company_size": company["size"],
            "company_stage": company["stage"],
            "location": location,
            "country": "USA" if "CA" in location or "NY" in location or "WA" in location or "TX" in location else "Other",
            "region": "North America",
            "remote_policy": random.choice(["On-site", "Hybrid", "Remote"]),
            "title": title,
            "level": level,
            "years_experience": years_exp,
            "years_at_company": random.randint(0, min(years_exp, 5)),
            "base_salary": base,
            "currency": "USD",
            "equity": equity,
            "equity_vesting": "4 years",
            "bonus": bonus,
            "signing_bonus": signing,
            "total_comp": total_comp,
            "benefits": random.sample(["Health", "Dental", "Vision", "401k", "Unlimited PTO"], k=random.randint(3, 5)),
            "skills": random.sample(["Python", "PyTorch", "TensorFlow", "LLM", "NLP", "Computer Vision"], k=random.randint(3, 4)),
            "education": random.choice(["BS Computer Science", "MS Computer Science", "PhD Machine Learning"]),
            "date_reported": f"2024-{random.randint(1, 3):02d}",
            "source": random.choice(["Levels.fyi", "LinkedIn", "Indeed"]),
            "verified": random.choice([True, False])
        }
        
        data.append(record)
    
    return data

def export_to_csv(data, filename="data/salary_data.csv"):
    """导出到CSV"""
    if not data:
        return
    
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ 导出CSV: {filename} ({len(data)}条记录)")

def export_to_json(data, filename="data/salary_data.json"):
    """导出到JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 导出JSON: {filename} ({len(data)}条记录)")

def generate_statistics(data):
    """生成统计数据"""
    base_salaries = [d["base_salary"] for d in data]
    total_comps = [d["total_comp"] for d in data]
    
    stats = {
        "total_records": len(data),
        "base_salary": {
            "mean": statistics.mean(base_salaries),
            "median": statistics.median(base_salaries),
            "min": min(base_salaries),
            "max": max(base_salaries),
        },
        "total_comp": {
            "mean": statistics.mean(total_comps),
            "median": statistics.median(total_comps),
            "min": min(total_comps),
            "max": max(total_comps),
        }
    }
    
    return stats

def main():
    print("🚀 开始生成AI/ML薪资数据...")
    print()
    
    # 生成数据
    data = generate_salary_data()
    
    # 导出
    export_to_csv(data)
    export_to_json(data)
    
    # 统计
    stats = generate_statistics(data)
    
    print()
    print("📊 数据统计:")
    print(f"  总记录数: {stats['total_records']}")
    print()
    print("  Base Salary:")
    print(f"    平均: ${stats['base_salary']['mean']:,.0f}")
    print(f"    中位数: ${stats['base_salary']['median']:,.0f}")
    print(f"    范围: ${stats['base_salary']['min']:,.0f} - ${stats['base_salary']['max']:,.0f}")
    print()
    print("  Total Compensation:")
    print(f"    平均: ${stats['total_comp']['mean']:,.0f}")
    print(f"    中位数: ${stats['total_comp']['median']:,.0f}")
    print(f"    范围: ${stats['total_comp']['min']:,.0f} - ${stats['total_comp']['max']:,.0f}")
    
    # 保存统计
    with open("output/statistics.json", 'w') as f:
        json.dump(stats, f, indent=2)
    print()
    print("✅ 统计数据已保存: output/statistics.json")
    print()
    print("🎉 数据收集完成!")

if __name__ == "__main__":
    main()
