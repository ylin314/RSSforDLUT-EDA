"""RSS 生成器"""

import os
import datetime
import time
import config
from rfeed import Feed, Item, Guid

def generate_rss_files(all_items):
    """根据所有条目生成 RSS 文件"""
    categories = set(item["category"] for item in all_items if item.get("category"))

    for cat in categories:
        filename = f"{cat}.xml"
        filepath = os.path.join(config.RSS_DIR, filename)

        # 筛选当前分类的条目
        cat_items = [i for i in all_items if i.get("category") == cat]
        cat_items.sort(key=lambda x: x.get("timestamp", 0), reverse=True)

        if not cat_items:
            continue

        # 构建 RSS 条目
        rss_items = []
        for i in cat_items:
            display_title = f"[{i['source']}] {i['title']}"
            rss_items.append(
                Item(
                    title=display_title,
                    link=i["link"],
                    description=display_title,
                    author="Monitor Script",
                    guid=Guid(i["link"]),
                    pubDate=datetime.datetime.fromtimestamp(
                        i.get("timestamp", time.time())
                    ),
                )
            )

        # 生成 RSS Feed
        feed = Feed(
            title=f"DUT Notification - {cat.upper()}",
            link=f"http://rss.ylin314.cn/rss/{filename}",
            description=f"Aggregated notifications for {cat}",
            language="zh-CN",
            lastBuildDate=datetime.datetime.now(),
            items=rss_items,
        )

        # 写入文件
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(feed.rss())

        print(f"Updated RSS file: {filepath}")
