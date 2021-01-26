from game_oop import Game


class HouYi(Game):

    # 构造方法会被重写，所以需要继承父类的构造方法+
    def __init__(self, my_hp, enemy_hp):
        self.defence = 100
        # 继承父类的构造方法
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        # 改造一下 my_hp的计算方式
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defence - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power

            print(f"我的血量:{self.my_hp} VS 敌人血量：{self.enemy_hp}")
            super().rest(3)
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


if __name__ == '__main__':
    houyi = HouYi(1000, 1100)
    # 子类对象可以直接调用父类的属性和方法
    print(houyi.my_power)
    houyi.fight()
    houyi.rest(3)

    #效果等同于在方法中用super().方法名
    # houyi.rest(3)
