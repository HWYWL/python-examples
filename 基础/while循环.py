num_1 = 100
num_2 = 100
num_3 = 100

while num_1 > 0:
    num_1 -= 1
    print(num_1)

while num_2 > 0:
    num_2 -= 1
    print(num_2)
    # 跳出本次循环开始下一次循环
    continue
    print("此行代码不会执行")

while num_3 > 0:
    num_3 -= 1
    print(num_3)
    if num_3 == 96:
        print("程序停止，不在往下执行")
        # 程序将讲跳出整个while循环，不会继续执行
        break
        print("此行代码不会执行")
print("程序执行完毕")
