import math
import random

import pygame

from mymodules.Enemy import Enemy
from mymodules.Player import Player


def is_collision(enemy, bullet):
    distance = math.sqrt((enemy.x - bullet.x) ** 2 + (enemy.y - bullet.y) ** 2)
    if distance <= 25:
        return True
    else:
        return False


def draw_text(text, font, x, y, screen, color=(255, 255, 255)):
    text_object = font.render(text, True, color)
    screen.blit(text_object, (x, y))


class Game:
    def __init__(self, caption, icon, width=800, height=600):
        self.__tps_max = 100.0

        pygame.init()
        self.__main_clock = pygame.time.Clock()
        self.__tps_delta = 0.0

        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.__icon = pygame.image.load(icon)
        pygame.display.set_icon(self.__icon)
        self.__entity = []
        self.__score = 0

    def run(self, color=(167, 184, 86)):
        running = True
        while running:
            self.__screen.fill(color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.__tps_delta += self.__main_clock.tick() / 1000.0
            while self.__tps_delta > 1 / self.__tps_max:
                for element in self.__entity:
                    element.move()
                    element.tick()

                self.__tps_delta -= 1 / self.__tps_max

            for element in self.__entity:
                element.draw()

            draw_text('score = %s' % self.__score, pygame.font.SysFont(None, 48), 0, 0, self.__screen)

            pygame.display.update()

    @property
    def screen(self):
        return self.__screen

    @property
    def elements(self):
        return self.__entity

    def add_element(self, element):
        if type(element) == list:
            self.__entity += element
        else:
            self.__entity.append(element)


if __name__ == "__main__":
    game = Game("arrow", 'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png')
    player = Player(735, 268, 3, ['assets/7soulsrpggraphics_sprites/Assets/Human (Side)/Full/player_01_64.png',
                                  'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_01_64.png',
                                  'assets/7soulsrpggraphics_sprites/Assets/Human (Front)/Full/player_01_64.png'], game)
    game.add_element(player)
    game.run()
