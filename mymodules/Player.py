import time

import pygame

from mymodules.Element import Element


def timer(start, second):
    if time.time() - start >= second:
        return True
    return False


class Player(Element):
    def __init__(self, x, y, speed, image, game):
        super().__init__(x, y, image, game)
        self.__base_speed = speed
        self.__speed = speed
        self.__orientation = "Down"
        self.left, self.right, self.up, self.down = False, False, False, False
        self.__time_animation = time.time()
        self.__animation_stage = 2

    def draw(self):
        if self.__orientation == "Left":
            self.game.screen.blit(self.image['Left'][self.__animation_stage], (self.x, self.y))
        elif self.__orientation == "Right":
            self.game.screen.blit(self.image['Right'][self.__animation_stage], (self.x, self.y))
        elif self.__orientation == "Up":
            self.game.screen.blit(self.image['Up'][self.__animation_stage], (self.x, self.y))
        elif self.__orientation == "Down":
            self.game.screen.blit(self.image['Down'][self.__animation_stage], (self.x, self.y))

    def move(self):
        if self.left:
            self.x += -self.__speed

        if self.right:
            self.x += self.__speed

        if self.up:
            self.y += -self.__speed

        if self.down:
            self.y += self.__speed

        if self.x < 0:
            self.x = self.game.screen.get_width() - self.size[0] - 1
            for bg in self.game.background:
                bg.move('right')
        elif self.x > self.game.screen.get_width() - self.size[0]:
            self.x = 1
            for bg in self.game.background:
                bg.move('left')
        if self.y < 0:
            self.y = self.game.screen.get_height() - self.size[1] - 1
            for bg in self.game.background:
                bg.move('down')
        elif self.y > self.game.screen.get_height() - self.size[1]:
            self.y = 1
            for bg in self.game.background:
                bg.move('up')

    def tick(self):
        keys = pygame.key.get_pressed()

        # movment

        if keys[pygame.K_LEFT]:
            self.__orientation = "Left"
            self.left = True
        else:
            self.left = False

        if keys[pygame.K_RIGHT]:
            self.__orientation = "Right"
            self.right = True
        else:
            self.right = False

        if keys[pygame.K_UP]:
            self.__orientation = "Up"
            self.up = True
        else:
            self.up = False

        if keys[pygame.K_DOWN]:
            self.__orientation = "Down"
            self.down = True
        else:
            self.down = False

        if keys[pygame.K_LSHIFT]:
            self.__speed = 2.5 * self.__base_speed
        else:
            self.__speed = self.__base_speed

        if (self.left or self.right or self.up or self.down) and timer(self.__time_animation, 0.3 / self.__speed):
            if self.__animation_stage < 3:
                self.__animation_stage += 1
                self.__time_animation = time.time()
            else:
                self.__animation_stage = 0
                self.__time_animation = time.time()
        else:
            if timer(self.__time_animation, 0.4 / self.__speed):
                self.__animation_stage = 2
