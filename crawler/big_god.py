# -*- coding:utf-8 -*-

from DrissionPage import SessionPage
import pymysql
import re

# 建立数据库连接
conn = pymysql.connect(host='172.16.10.90', port=3306, database='crawler', user='root', password='123456')

# 创建游标对象
cursor = conn.cursor()
# 创建页面对象
page = SessionPage()


def next_page(title, page_link):
    page.get(page_link)
    div = page.ele('#content')
    script = div.ele('tag:script').text
    # 使用正则表达式提取URL
    url_pattern = r"url: '([^']*)'"
    pic_pattern = r"pic: '([^']*)'"
    url_matches = re.findall(url_pattern, script)
    pic_matches = re.findall(pic_pattern, script)

    if url_matches:
        url = url_matches[0]
        pic = pic_matches[0]

        # 执行INSERT语句
        sql = "INSERT INTO big_god (title, video_url, image_url) VALUES (%s, %s, %s)"
        values = (title, url, pic)
        cursor.execute(sql, values)
        conn.commit()
        try:
            print(title, url, pic)
        except Exception as e:
            print("title error.")
    else:
        print("URL not found in the code.")


if __name__ == "__main__":
    # 下载文件路径
    for i in range(1, 54):
        # 访问某一页的网页
        page.get(f'https://xn---91dsvodcom-uu0ty71c3m3evyue1b8a.91dsvod-com.com/index-0-{i}.html')
        # 获取所有开源库<a>元素列表
        links = page.eles('.item')
        # 遍历所有<a>元素
        for link in links:
            a_info = link.ele('tag:a')
            href = a_info.attr('href')
            title = a_info.attr('title')
            # 拉取下一层级明细
            next_page(title, href)

        print("当前页：%d" % i)

    # 关闭游标对象和数据库连接
    cursor.close()
    conn.close()
