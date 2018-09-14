# 函数嵌套执行
def test1(num):
    print("+" * num)


def test2(num):
    test1(num)
    print("-" * num)


test2(10)
