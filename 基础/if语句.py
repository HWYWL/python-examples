age = 22
is_employee = False

"""
and 与
or  或
not 非
"""

if age < 18:
    print("骚年你还未满18，不要想着搞事情")
elif 18 <= age < 60:
    print("我们去happy，手动滑稽")
else:
    print("嗨不动了")

if not is_employee:
    print("你是本公司员工")

holiday = "情人节"
happy = "开心"

if holiday == "情人节":
    print("送纪梵希口红")
    if happy == "开心":
        print("嘿嘿嘿")
    else:
        print("看电影")
elif holiday == "生日":
    print("买蛋糕")
    print("送玫瑰")
else:
    print("天天都是小甜甜的节日")
