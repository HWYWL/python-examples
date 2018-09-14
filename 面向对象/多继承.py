class Erlang:
    def figure(self):
        print("二郎神")

    def weapon(self):
        print("三叉戟")


class SkyBarkingHound:
    def fly(self):
        print("飞天神犬")


# 多继承
class SupernaturalBeing(Erlang, SkyBarkingHound):
    def combat(self):
        print("全军出击")


# 神仙打架
being = SupernaturalBeing()
being.figure()
being.weapon()
being.fly()
