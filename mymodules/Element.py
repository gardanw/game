import pygame


class Element:
    def __init__(self, x, y, image, game):
        self.__x = x
        self.__y = y
        self.__image, self.__size = self.__set_image(image)
        self.__game = game

    def draw(self):
        pass

    def move(self):
        pass

    def tick(self):
        pass

    @staticmethod
    def __set_image(image):
        if type(image) == dict:
            side_left = []
            side_right = []
            side_up = []
            side_down = []
            size = None
            for side in image:
                for img in image[side]:
                    if side == 'back':
                        side_up.append(pygame.image.load(img))
                        if not size:
                            size = side_up[-1].get_size()
                    elif side == 'side':
                        side_left.append(pygame.image.load(img))
                        side_right.append(pygame.transform.flip(side_left[-1], True, False))
                        if not size:
                            size = side_left[-1].get_size()
                    elif side == 'front':
                        side_down.append(pygame.image.load(img))
                        if not size:
                            size = side_down[-1].get_size()
            return {'Left': side_left, 'Right': side_right, 'Up': side_up, 'Down': side_down}, size
        elif type(image) == str:
            img = pygame.image.load(image)
            size = img.get_size()
            return img, size

    def __str__(self):
        return str(self.__x) + ' ' + str(self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def size(self):
        return self.__size

    @property
    def pos(self):
        return self.__x + self.__size[0] / 2, self.__y + self.__size[1] / 2

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


if __name__ == "__main__":
    pass
