from mymodules.Element import Element


class ScreenElement(Element):
    def __init__(self, x, y, image, game):
        super().__init__(x, y, image, game)

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))


if __name__ == '__main__':
    pass
