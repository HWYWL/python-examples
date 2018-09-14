# 元组可以存放不同的数据,当元组只有一个数据时需要在后面加上逗号 info_tuple = ("美女",)
info_tuple = ("美女", 18, 165.5)

for info in info_tuple:
    print(info)

print("美女关键字所在的索引为：%d" % info_tuple.index("美女"))
print("元组长度为：%d" % len(info_tuple))

print("%s 的年龄为 %d 身高是%.2f" % info_tuple)

# 把元组转换为列表
asalk_list = list(info_tuple)
print(asalk_list)

# 把列表转换为元组
asalk_tuple = tuple(asalk_list)
print(asalk_tuple)