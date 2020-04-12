from typing import Any, Union


class Screen:
    def __init__(self, pos, game):
        self.__game = game
        self.elements = []
        self.pos = pos

    def draw(self):
        if self.pos == [0, 0]:
            for element in self.elements:
                element.draw()

    def move(self, side):
        if side == 'up':
            self.pos[1] += 1
            for element in self.elements:
                element.y += self.__game.screen.get_size()[1]
        elif side == 'down':
            self.pos[1] -= 1
            for element in self.elements:
                element.y -= self.__game.screen.get_size()[1]
        elif side == 'right':
            self.pos[0] += 1
            for element in self.elements:
                element.x += self.__game.screen.get_size()[0]
        elif side == 'left':
            self.pos[0] -= 1
            for element in self.elements:
                element.x -= self.__game.screen.get_size()[0]

    def add_element(self, element):
        element.x += self.__game.screen.get_size()[0] * self.pos[0]
        element.y += self.__game.screen.get_size()[1] * self.pos[1]
        self.elements.append(element)


if __name__ == '__main__':
    pass
