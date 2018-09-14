# 这是列表，[]
name_list = ["校花", "美女", "小萝莉"]
print(name_list)

name_list.append("御姐")
print(name_list)

# 直接遍历
for name in name_list:
    print(name)

# 通过索引遍历
for index in range(len(name_list)):
    print(name_list[index])


count = name_list.count("美女")
print("美女关键字出现的次数 %d" % count)

# 逆序反转
name_list.reverse()
print(name_list)

num_list = [3, 101, 6, 8, 62, 25]
print(num_list)

# 升序排序
num_list.sort()
print(num_list)

# 降序排序
num_list.sort(reverse=True)
print(num_list)