# eval函数可以将字符当成表达式计算,例如输入：6*9+64+4+595+6
while True:
    input_str = input("请输入计算表达式：")
    print(eval(input_str))
