# -*- coding:utf-8 -*-

import pymysql
from DrissionPage import WebPage

# 建立数据库连接
conn = pymysql.connect(host='127.0.0.1', port=50379, database='crawler', user='root', password='123456')

# 创建游标对象
cursor = conn.cursor()
# 创建页面对象
page = WebPage()


def next_page(title, page_link, image_url):
    page.get(page_link)

    try:
        video_url = page.ele('#myPlayer').ele('tag:source').attr('src')

        if video_url.strip():
            # 执行INSERT语句
            sql = "INSERT INTO tkbbo (title, video_url, image_url) VALUES (%s, %s, %s)"
            values = (title, video_url, image_url)
            cursor.execute(sql, values)
            conn.commit()
            print(title, video_url, image_url)
        else:
            print("URL not found in the code.")
    except Exception as e:
        print("获取视频详情错误.")


if __name__ == "__main__":
    # 下载文件路径
    for i in range(2, 59):
        # 访问某一页的网页
        page.get(f'https://www.tkbbo8.life/videos.html?type=NEW&page={i}')
        # 获取所有开源库<a>元素列表
        links = page.eles('.video-item')

        lists = []
        # 遍历所有<a>元素
        for link in links:
            try:
                # https://static.tkbbo8.life/21ca1774d543b735318875cdb06fda0a/480p_38501/thumbnail.jpg
                pre_img = link.ele('.pre-img')
                link_img = pre_img.ele('tag:img').attr('data-src')

                title = link.ele('.video-desc').ele('.video-desc-content').text

                # https://www.tkbbo8.life/view_video.html?batch=21ca1774d543b735318875cdb06fda0a&u=480p_38501
                url_parts = link_img.split("/")
                href = 'https://www.tkbbo8.life/view_video.html?batch=' + url_parts[3] + '&u=' + url_parts[4]
                # 拉取下一层级明细

                array = [title, href, link_img]
                lists.append(array)
            except Exception as e:
                print("获取视频列表错误.")

        for arr in lists:
            next_page(arr[0], arr[1], arr[2])

        print("当前页：%d" % i)

    # 关闭游标对象和数据库连接
    cursor.close()
    conn.close()
