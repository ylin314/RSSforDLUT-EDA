# RSS for DLUT-EDA

大连理工大学开发区校区 RSS 订阅服务，自动抓取并聚合校内各类通知公告

## 快速使用

**订阅地址**: [http://rss.ylin314.cn](http://rss.ylin314.cn)

访问该地址即可查看所有可用的 RSS 订阅源，复制对应链接添加到你的 RSS 阅读器即可

## 订阅源列表

### 教务信息
- 教务处部院信息

### 软件学院
- 本科生通知
- 研究生通知
- 研究生招生
- 学术报告
- 创新实践
- 国际交流
- 国际通知
- 学工通知
- 学生活动

### 校区行政
- 开发区校区教学运行保障中心
- 开发区校区管委会


## 项目结构

```
├── config.py           # 配置文件
├── main.py             # 主程序入口
├── crawler_service.py  # 后台爬虫服务
├── crawler.py          # 网页抓取逻辑
├── parsers.py          # HTML 解析器
├── sources.py          # 数据源配置
├── database.py         # 数据持久化
├── rss_generator.py    # RSS 生成器
├── web_server.py       # Flask Web 服务
├── rss_data.json       # 持久化抓取数据
└── rss/                # RSS 文件输出目录
```

## 添加新的订阅源

编辑 `sources.py`，在 `SOURCES` 列表中添加新的配置项：

```python
{
    "name": "订阅源名称",
    "url": "目标网页 URL",
    "selector": "CSS 选择器",
    "parser": parse_title_attr,  # 解析函数
    "category": "分类标识"
}
```