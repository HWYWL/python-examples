name = "小米"
age = 18
sex = True
weight = 100.5

# 查看类型
print(type(name))
print(type(age))
print(type(sex))
print(type(weight))

# 不同类型计算
print(age + weight)
print(age * weight)
print(weight + sex)
print(age + sex)

# 打印18个小米
print(name * age)

# 字符串和数字类型只能使用 * 计算，不能使用其他计算方式。例如(name + sex)这种就是错误的计算方式
print(name + age) # 错误的计算方式
