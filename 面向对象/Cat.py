class Cat:
    def __init__(self, cat_name):
        print("创建对象,数据初始化。。。")
        self.name = cat_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)


# 对象创建
cat = Cat("Tomcat")

# 对象方法调用
cat.eat()
cat.drink()

# 对象创建
lazy_cat = Cat("大懒猫")

# 对象方法调用
lazy_cat.eat()
lazy_cat.drink()
