from DrissionPage import WebPage

# pip 安装 DrissionPage：pip install DrissionPage
# 创建页面对象
page = WebPage()
# 访问网址
page.get('https://www.boxmp4.com')
# 查找文本框元素并输入关键词
page('#wd').input('情癫大圣')
# 点击搜索按钮
page('t:button@tx():搜索').click()
# 等待页面加载
page.wait.load_start()
# 切换到收发数据包模式
# page.change_mode()
# 获取所有行元素
items = page('#list_all').ele("tag:ul").eles("tag:li")
# 遍历获取到的元素
for item in items:
    ele = item.ele("tag:a")
    ele_info = ele.ele("tag:img")
    name = ele_info.attr("alt")
    # 打印元素文本
    print('电影名称：', ele_info.attr("alt"), '\t\t\t详情链接：', ele.link, '\t\t\t封面链接：', ele_info.link)
