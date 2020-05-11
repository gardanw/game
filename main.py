from mymodules.Element import Element
from mymodules.Game import Game
from mymodules.Player import Player
from mymodules.Screen import Screen
from mymodules.ScreenElement import ScreenElement


def load_img(path):
    pass


def create_screen(location, path_to_image, game):
    screen = Screen(location, game)
    screen.add_element(ScreenElement(0, 0, path_to_image, game))
    return screen


def main():
    game = Game("arrow", 'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png', width=1280,
                height=720, color=(0, 0, 0))
    # player
    side = []
    back = []
    front = []
    for i in range(1, 5):
        side.append('assets/7soulsrpggraphics_sprites/Assets/Human (Side)/Full/player_{:02d}_64.png'.format(i))
        back.append('assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_{:02d}_64.png'.format(i))
        front.append('assets/7soulsrpggraphics_sprites/Assets/Human (Front)/Full/player_{:02d}_64.png'.format(i))
    player = Player(0, 0, 1, {'side': side, 'back': back, 'front': front}, game)
    game.add_element(player)

    # background
    s1 = create_screen([0, 0], r'assets\2dhandpainted_towntileset\Assets\64x64\grass.png', game)
    s2 = create_screen([0, 0], r'assets\2dhandpainted_towntileset\Assets\64x64\bar.png', game)
    game.add_background(s1)
    game.add_background(s2)
    game.run()


if __name__ == '__main__':
    main()
