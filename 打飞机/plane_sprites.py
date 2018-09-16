import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 敌方飞机创建时间(ms)
AIRCRAFT_CREATION_TIME = 1200
# 英雄初始化距离屏幕的距离
DISTANCE_FROM_BOTTOM = 50
# 我方飞机操作移动速度
DISTANCE_MOVEMENT_SPEED = 2
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 飞机产生子弹的速度
RATE_OF_FIR = 500
# 子弹飞行速度
RATE_MOVEMENT_SPEED = 2


class GameSprite(pygame.sprite.Sprite):
    """脚本精灵"""

    # 初始化
    def __init__(self, image_name, speed=1):
        super().__init__()

        # 游戏属性图像
        self.image = pygame.image.load(image_name)
        # 位置
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()

        # 判断是否移出屏幕，如果移出屏幕，将背景图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始随机速度 1 ~ 3
        self.speed = random.randint(1, 3)

        # 指定敌机的初始随机位置
        self.rect.bottom = 0

        # 敌机水平方向出现的最大值
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向的飞行
        super().update()

        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    # 对象销毁之前调用次方法
    def __del__(self):
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1. 调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)

        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - DISTANCE_FROM_BOTTOM

        # 3. 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -RATE_MOVEMENT_SPEED)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
