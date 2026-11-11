#!/usr/bin/env python3
"""
RSS 讀取小工具

用法：
    pip install feedparser
    python tools/rss_reader.py
"""

import feedparser

FEEDS = {
    "Guardian": "https://www.theguardian.com/world/rss",
    "Ars Technica": "https://arstechnica.com/feed",
    "Rest of World": "https://restofworld.org/feed/latest",
}


def print_feed(name: str, url: str, limit: int = 5) -> None:
    feed = feedparser.parse(url)

    if feed.bozo:
        print(f"[{name}] 讀取失敗：{feed.bozo_exception}")
        return

    print(f"\n=== {name} ===")
    print(f"網站標題：{feed.feed.get('title', '(無)')}")
    print(f"網站連結：{feed.feed.get('link', '(無)')}")
    print(f"共 {len(feed.entries)} 篇文章，顯示前 {limit} 篇：\n")

    for entry in feed.entries[:limit]:
        print(f"- {entry.get('title', '(無標題)')}")
        print(f"  連結：{entry.get('link', '(無)')}")
        print(f"  時間：{entry.get('published', '(無)')}")


def main() -> None:
    for name, url in FEEDS.items():
        print_feed(name, url)


if __name__ == "__main__":
    main()
