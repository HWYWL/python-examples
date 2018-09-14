def test(num):
    a = 10

    print("num的值为：%d,其内存地址为：%d" % (num, id(num)))
    print("a的值为：%d,其内存地址为：%d" % (a, id(a)))


test(11)