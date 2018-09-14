def test():
    try:
        num = int(input("请输入一个整数："))
        i = 1 / num
    except ZeroDivisionError:
        print("除以0错误")

        # as 关键字是用于重命名
    except Exception as result:
        print("未知异常: %s" % result)
    else:
        print("没有异常时，执行此行代码")
    finally:
        print("不管是否出现异常，此行代码都会执行")


test()
