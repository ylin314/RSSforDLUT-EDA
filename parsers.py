"""HTML 解析器"""


def parse_title_attr(tag):
    """解析 title 属性"""
    return tag.get('title', '').strip()


def parse_h2_child(tag):
    """解析 h2 子标签内容"""
    h2 = tag.find('h2')
    return h2.get_text().strip() if h2 else tag.get_text().strip()


def parse_text_content(tag):
    """解析文本内容"""
    return tag.get_text().strip()
