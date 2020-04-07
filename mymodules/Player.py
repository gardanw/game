import pygame

from mymodules.Element import Element


class Player(Element):
    def __init__(self, x, y, speed, image, game, move_side=True):
        Element.__init__(self, x, y, speed, image, game)
        self.__move_side = move_side
        self.__orientation = "Left"
        self.bullet = []
        self.left, self.right, self.up, self.down = False, False, False, False
        self.cooldown = 0
        self.__time_start = 0
        self.__animation_stage = 0

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
            self.x += -self.speed

        if self.right:
            self.x += self.speed

        if self.up:
            self.y += -self.speed

        if self.down:
            self.y += self.speed


        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
        if self.y <= 0:
            self.y = 0
        elif self.y >= 536:
            self.y = 536

    def tick(self):
        keys = pygame.key.get_pressed()

        # movment

        if self.__move_side and keys[pygame.K_LEFT]:
            self.__orientation = "Left"
            self.left = True
        else:
            self.left = False

        if self.__move_side and keys[pygame.K_RIGHT]:
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

        if self.left or self.right or self.up or self.down:
            if self.__animation_stage < 3:
                self.__animation_stage += 1
            else:
                self.__animation_stage = 0
        else:
            self.__animation_stage = 0
