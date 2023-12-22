# -*- coding:utf-8 -*-

from DrissionPage import SessionPage
import pymysql
import datetime
from urllib.parse import urlparse

# 建立数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, database='crawler', user='root', password='123456')

# 创建游标对象
cursor = conn.cursor()
# 创建页面对象
page = SessionPage()


def next_page(title, page_link, logo):
    global name, dec, url_without_params
    try:
        page.get(page_link)
        name = page.ele('.site-name h3 my-3').text
        dec = page.ele('.panel-body single my-4 ').text
        go_url = page.ele('.site-go-url').ele('tag:a').attr('href')

        # 跳转到源站
        page.get(go_url)
        source_station = page.ele('.loading-url').text
        parsed_url = urlparse(source_station)
        scheme = parsed_url.scheme
        netloc = parsed_url.netloc
        path = parsed_url.path
        url_without_params = f"{scheme}://{netloc}{path}"

        print(name, title, logo, dec, url_without_params)
    except Exception as e:
        print("title error.")
        return

    # 执行INSERT语句
    sql = "INSERT INTO ai (name,intro, logo_url, summarize,source_url,create_time) VALUES (%s, %s, %s, %s, %s, %s)"
    current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values = (name, title, logo, dec, url_without_params, current_timestamp)
    cursor.execute(sql, values)
    conn.commit()


if __name__ == "__main__":
    # 下载文件路径
    # 访问某一页的网页
    page.get(f'https://www.ainav.cn/')
    # 获取所有开源库<class>元素列表
    links = page.eles('.url-body default ')
    # 遍历所有<a>元素
    for link in links:
        a_info = link.ele('tag:a')
        href = a_info.attr('href')
        title = a_info.attr('title')
        logo = link.ele('tag:img').attr('data-src')
        # 拉取下一层级明细
        next_page(title, href, logo)

    # 关闭游标对象和数据库连接
    cursor.close()
    conn.close()
