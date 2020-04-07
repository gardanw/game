import pygame


class Element:
    def __init__(self, x, y, speed, image, game):
        self.__x = x
        self.__y = y
        self.__speed = speed
        img = pygame.image.load(image)
        self.__image = img
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
