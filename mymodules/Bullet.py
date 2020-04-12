from mymodules.Element import Element


class Bullet(Element):
    def __init__(self, x, y, speed, image, game, state=0):
        Element.__init__(self, x, y, speed, image, game)
        self.__state = state

    def draw(self):
        self.game.screen.blit(self.image, (self.x - 5, self.y + 16))

    def move(self):
        if self.__state == 1:
            self.x -= self.__speed
        if self.x < 0:
            self.__del__()

    def delete(self):
        try:
            self.game.bullet.remove(self)
        except:
            print('Not found')
        del self

    def __del__(self):
        pass


if __name__ == "__main__":
    b = Bullet(735, 268, 3, "assets/archer.png", 'game', state=1)
    l = [1, 2, 3, 4, b, 5]
    # for i in l:
    #     print(type(i))
    #     if type(i) == Bullet:
    #         del i
    #     else:
    #         print(i)
    print(l)
    del l[4]
    print(l, 'del')
