"""数据库操作"""

import json
import os
import config


def load_db():
    """加载数据库"""
    if os.path.exists(config.DB_FILE):
        try:
            with open(config.DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []


def save_db(data):
    """保存数据库，保留最新的 1000 条记录"""
    data = sorted(data, key=lambda x: x.get("timestamp", 0), reverse=True)[:1000]
    with open(config.DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
