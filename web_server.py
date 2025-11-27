"""Web 服务器"""

import os
from flask import Flask, send_from_directory, render_template_string
import config

app = Flask(__name__)


@app.route("/")
def index():
    files = [f for f in os.listdir(config.RSS_DIR) if f.endswith(".xml")]

    links_html = ""
    for f in files:
        links_html += f'<li><a href="/rss/{f}">{f}</a> (Copy Link: <code>http://{get_request_url()}/rss/{f}</code>)</li>'

    return render_template_string(
        """
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DLUT-EDA RSS Server</title>
        <style>
            body {
                font-family: sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 0 20px;
                line-height: 1.6;
            }

            h1 {
                color: #333;
            }

            li {
                margin-bottom: 10px;
            }

            code {
                background: #f4f4f4;
                padding: 2px 5px;
                border-radius: 3px;
            }
        </style>
        </head>
        <body>
            <h1>DLUT-EDA RSS Feeds</h1>
            <p>Current Status: Running</p>
            <p>Available Feeds:</p>
            <ul>"""
        + links_html
        + """</ul>
        </body>
        </html>
    """
    )

@app.route("/rss/<path:filename>")
def serve_rss(filename):
    """提供 RSS 文件下载"""
    return send_from_directory(config.RSS_DIR, filename)


def get_request_url():
    return "rss.linyang.ink"
