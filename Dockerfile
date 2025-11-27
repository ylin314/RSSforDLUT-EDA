# 使用官方 Python 运行时作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目文件
COPY . .

# 创建 RSS 目录
RUN mkdir -p rss

# 暴露端口
EXPOSE 5634

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 运行应用
CMD ["python", "main.py"]
