import random

player = int(input("请输入石头(1)剪刀(2)布(3)："))

# 随机生成1~3之间的整数，包含1和3
computer = random.randint(1, 3)

if player == computer:
    print("平局，电脑%d -- 你%d" % (computer, player))
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("你赢了，电脑%d -- 你%d" % (computer, player))
else:
    print("电脑获胜，电脑%d -- 你%d" % (computer, player))
