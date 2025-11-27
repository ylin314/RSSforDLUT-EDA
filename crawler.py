"""爬虫逻辑"""

import requests
from bs4 import BeautifulSoup
import config
import time
from urllib.parse import urljoin


def fetch_url(source):
    """抓取指定数据源的内容"""
    new_items = []
    try:
        resp = requests.get(source["url"], headers=config.HEADERS, timeout=10)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        tags = soup.select(source["selector"])

        for tag in tags:
            try:
                href = tag.get("href")
                if not href:
                    continue

                full_url = urljoin(str(source["url"]), str(href))
                title = source["parser"](tag)

                if title and full_url:
                    new_items.append(
                        {
                            "title": title,
                            "link": full_url,
                            "source": source["name"],
                            "category": source.get("category", "unknown"),
                            "timestamp": time.time(),
                        }
                    )
            except:
                pass

    except Exception as e:
        print(f"Failed to fetch {source['name']}: {e}")
    return new_items
