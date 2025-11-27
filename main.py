"""主程序入口"""

import os
import threading
from crawler_service import crawler_thread
from web_server import app
from config import RSS_DIR, PORT


def main():
    """主函数"""
    # 确保 RSS 目录存在
    if not os.path.exists(RSS_DIR):
        os.makedirs(RSS_DIR)

    # 启动后台爬虫线程
    t = threading.Thread(target=crawler_thread, daemon=True)
    t.start()

    # 启动 Flask Web 服务器
    app.run(debug=False, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
