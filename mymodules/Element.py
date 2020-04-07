import pygame


class Element:
    def __init__(self, x, y, speed, image, game):
        self.__x = x
        self.__y = y
        self.__speed = speed
        side_left = []
        side_right = []
        side_up = []
        side_down = []
        for i in range(len(image[0])):
            side_left.append(pygame.image.load(image[0][i]))
            side_right.append(pygame.transform.flip(side_left[-1], True, False))
            side_up.append(pygame.image.load(image[1][i]))
            side_down.append(pygame.image.load(image[2][i]))
        self.__image = {'Left': side_left, 'Right': side_right, 'Up': side_up, 'Down': side_down}
        self.__game = game

    def draw(self):
        pass

    def move(self):
        pass

    def tick(self):
        pass

    def shot(self):
        pass

    def __str__(self):
        return str(self.__x) + ' ' + str(self.__y) + ' ' + str(self.__speed)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def speed(self):
        return self.__speed

    @property
    def game(self):
        return self.__game

    @property
    def image(self):
        return self.__image

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @speed.setter
    def speed(self, speed):
        self.__speed = speed


if __name__ == "__main__":
    pass
