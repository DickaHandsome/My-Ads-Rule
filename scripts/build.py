#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
规则合并构建脚本
- 读取 rule/ 目录下所有 .txt 分类规则
- 去重后合并生成主规则文件
- 自动生成头部元信息与版本号（基于日期）
用法: python scripts/build.py
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# ============== 配置区（按需修改） ==============
REPO_TITLE = "My Ads Rule"                      # 规则集名称
OUTPUT_FILE = "MyRule.txt"                      # 输出主规则文件名
HOMEPAGE = "https://github.com/DickaHandsome/My-Ads-Rule"  # 仓库主页
LICENSE_URL = f"{HOMEPAGE}/blob/main/LICENSE"   # 协议链接
RULE_DIR = "rule"                               # 分类规则目录
# ==============================================

ROOT = Path(__file__).resolve().parent.parent
RULE_PATH = ROOT / RULE_DIR
OUTPUT_PATH = ROOT / OUTPUT_FILE


def load_rules(path: Path):
    """读取单个规则文件，返回 (分类标题, 规则行列表)"""
    title = path.stem
    rules = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("!"):
                continue
            rules.append(line)
    return title, rules


def build():
    if not RULE_PATH.exists():
        print(f"[错误] 规则目录不存在: {RULE_PATH}")
        sys.exit(1)

    files = sorted(RULE_PATH.glob("*.txt"))
    if not files:
        print(f"[错误] 规则目录下没有 .txt 文件: {RULE_PATH}")
        sys.exit(1)

    seen = set()
    merged = []          # 去重后的规则
    category_stats = []  # 各分类统计

    for fp in files:
        title, rules = load_rules(fp)
        category_stats.append((title, len(rules)))
        for r in rules:
            if r not in seen:
                seen.add(r)
                merged.append(r)

    version = datetime.now().strftime("v%Y.%m.%d")
    total = len(merged)

    header = [
        f"!Title: {REPO_TITLE}",
        "!======================================",
        f"!Total lines: {total}",
        f"!Version: {version}",
        "",
        f"!Homepage: {HOMEPAGE}",
        f"!License: {LICENSE_URL}",
        "",
        "! 分类统计:",
    ]
    for title, count in category_stats:
        header.append(f"!   - {title}: {count} 条")
    header.append("!======================================")
    header.append("")

    content = "\n".join(header) + "\n".join(merged) + "\n"

    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"[完成] 已生成 {OUTPUT_FILE}")
    print(f"  规则总数: {total}")
    for title, count in category_stats:
        print(f"  - {title}: {count}")
    print(f"  版本号: {version}")


if __name__ == "__main__":
    build()
