import hello

# 函数使用
hello.hello()


# 函数传参
def sum(num1, num2):
    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))

    return result


# 函数调用
result = sum(10, 20)

print("结果：%d" % result)
