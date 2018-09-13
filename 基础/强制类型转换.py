name = "苹果"

# 从键盘输入数据
price_str = input("请输入" + name + "的价格：")
weight_str = input("请输入" + name + "的重量：")

# 类型转换
price = float(price_str)
weight = float(weight_str)

"""
%d 整数占位符
%s 字符串占位符
%f 小数占位符
%%  输出%号
"""
print("%s 的单价为 %.2f，重量为 %f，总价格为 %f" % (name, price, weight, price * weight))


# 立方体计算

# 输入转换一步完成
length = float(input("请输入立方体的长度："))
width = float(input("请输入立方体的宽度："))
height = float(input("请输入立方体的高度："))

print("立方体的长度 %.2f，立方体的宽度 %.2f，立方体的高度 %.2f，立方体的体积为：%.2f" % (length, width, height, length * width * height))


