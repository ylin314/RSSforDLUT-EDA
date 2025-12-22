"""数据源配置"""

from parsers import parse_title_attr, parse_h2_child, parse_text_content

SOURCES = [
    # 1. 校区行政
    {
        "name": "开发区校区综合办公室",
        "url": "https://eda.dlut.edu.cn/n/tzgg.htm",
        "selector": ".list li a",
        "parser": parse_title_attr,
        "category": "campus",
    },
    {
        "name": "开发区校区教学运行保障中心",
        "url": "https://jxyxbzzx.dlut.edu.cn/tzgg/kfqxq.htm",
        "selector": ".l_section_4 .subnav",
        "parser": parse_text_content,
        "category": "campus",
    },
    # 2. 教务
    {
        "name": "教务处部院信息",
        "url": "https://teach.dlut.edu.cn/byxx/byxx.htm",
        "selector": ".list ul li a",
        "parser": parse_title_attr,
        "category": "teaching",
    },
    # 3. 软件学院
    {
        "name": "软院-学生活动",
        "url": "https://ss.dlut.edu.cn/xsgz/xshd.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-学工通知",
        "url": "https://ss.dlut.edu.cn/xsgz/tzgg.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-国际通知",
        "url": "https://ss.dlut.edu.cn/gjhzjl/tzgg.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-国际交流",
        "url": "https://ss.dlut.edu.cn/gjhzjl/gjjl.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-学术报告",
        "url": "https://ss.dlut.edu.cn/kxyj/xsbg.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-创新实践",
        "url": "https://ss.dlut.edu.cn/rcpy/cxsj/hdtz.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-研究生招生",
        "url": "https://ss.dlut.edu.cn/rcpy/yjspy/yjszs.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-研究生通知",
        "url": "https://ss.dlut.edu.cn/rcpy/yjspy/yjstz.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
    {
        "name": "软院-本科生通知",
        "url": "https://ss.dlut.edu.cn/rcpy/bkspy/bkstz.htm",
        "selector": ".list04 .item a",
        "parser": parse_h2_child,
        "category": "ssdut",
    },
]
