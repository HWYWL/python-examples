class YoungerSister:
    def __init__(self, name):
        self.name = name
        # 外部不能访问私有属性
        self.__age = 18

    # 外部不能访问私有方法
    def __secret(self):
        print("我的年龄是%s 岁" % self.__age)


imoko = YoungerSister("校花")
print(imoko.name)

print("*" * 50 + "华丽分隔符" + "*" * 50)

# 强制调用私有属性和私有方法，不建议使用
print(imoko._YoungerSister__age)
imoko._YoungerSister__secret()

