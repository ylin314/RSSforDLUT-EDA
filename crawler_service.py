"""爬虫服务"""

import time
import datetime
import os
from config import RSS_DIR, INTERVAL
from sources import SOURCES
from database import load_db, save_db
from crawler import fetch_url
from rss_generator import generate_rss_files


def crawler_thread():
    """后台爬虫线程"""
    print("Background crawler started.")

    while True:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Scanning sources...")

        current_db = load_db()
        existing_links = {item["link"] for item in current_db}
        updates_found = False

        for source in SOURCES:
            fetched_items = fetch_url(source)
            for item in fetched_items:
                if item["link"] not in existing_links:
                    print(f"NEW [{source['category']}]: {item['title']}")
                    current_db.append(item)
                    existing_links.add(item["link"])
                    updates_found = True

        # 如果有更新或目录为空,则生成 RSS
        if updates_found or not os.listdir(RSS_DIR):
            save_db(current_db)
            generate_rss_files(current_db)

        time.sleep(INTERVAL)
