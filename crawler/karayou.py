import os
import re

from DrissionPage import SessionPage

# 创建页面对象
page = SessionPage()


def next_page(title, page_link, path):
    page.get(page_link)
    sr_eles = page.eles('.mbn savephotop')

    # 创建文件夹
    special_chars = r'[\\/:*?"<>|]'
    new_folder_name = re.sub(special_chars, '', title)
    folder_path = path + new_folder_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 遍历列表
    for ele in sr_eles:
        e = ele.ele('tag:img')
        # 获取并打印标签名、文本、href 属性
        img_url = e.attr('src').split('static')[0] + e.attr('zoomfile')

        # 返回一个任务对象，通过任务对象查看状态，多线程下载
        # mission = page.download.add(img_url, folder_path, new_folder_name, 'rename')
        # print(mission.rate, mission.info)

        # 单线程下载，显示下载进度
        res = page.download(img_url, folder_path, new_folder_name, 'rename', show_msg=True)
        print(res)


if __name__ == "__main__":
    # 下载文件路径
    path = 'D:/small/'
    for i in range(2, 3):
        # 访问某一页的网页
        page.get(f'https://www.karayou.com/forum-92-{i}.html')
        # 获取所有开源库<a>元素列表
        links = page.eles('.s xst')
        # 遍历所有<a>元素
        for link in links:
            # 拉取下一层级明细
            print(link.text, link.link)
            next_page(link.text, link.link, path)
