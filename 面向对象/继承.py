class Dog:

    def eat(self):
        print("吃骨头")

    def cry(self):
        print("汪汪叫")


# 继承Dog 类
class XiaoTiandog(Dog):

    def trait(self):
        print("我会飞")


# 继承Dog 类
class WangCaiDog(Dog):
    # 重写父类方法
    def eat(self):
        print("吃狗粮")

    def trait(self):
        print("我打不死")


xiao_tian_dog = XiaoTiandog()
xiao_tian_dog.eat()
xiao_tian_dog.trait()

print("*" * 50 + "华丽分隔符" + "*" * 50)

wang_cai_dog = WangCaiDog()
wang_cai_dog.eat()
wang_cai_dog.trait()
