def test(num, *ags, **kwargs):
    """
    python 中有 两种 多值参数：

    - 参数名前增加 一个 * 可以接收 元组
    - 参数名前增加 两个 * 可以接收 字典

    :param num: 不同数据
    :param ags: 元组数据
    :param kwargs: 字典数据
    """
    print(num)
    print(ags)
    print(kwargs)


test(1, 2, 3, 4, 5, 6, 7, name="美女", age=18)

print("*" * 100)


def test1(ags):
    """
    类型按照传参决定
    :param ags: 类型按照传参决定
    """
    print(ags)


# 参数为元组
test1((1, 2, 3, 4, 5, 6, 7))

print("*" * 100)

# 拆包
gl_nums_tuple = (1, 2, 3, 4, 5)
gl_student_dict = {"name": "美女", "age": 18}


def test2(*args, **kwargs):
    print(args)
    print(kwargs)


test2(*gl_nums_tuple, **gl_student_dict)
