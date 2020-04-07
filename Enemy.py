from Element import Element


class Enemy(Element):
    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y <= 1:
            self.speed *= -1
            self.x += 32
        elif self.y >= 535:
            self.speed *= -1
            self.x += 32

    def shot(self):
        print('arg')
