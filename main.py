from mymodules.Element import Element
from mymodules.Game import Game
from mymodules.Player import Player
from mymodules.Screen import Screen
from mymodules.ScreenElement import ScreenElement


def load_img(path):
    pass


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
    screen = Screen([0, -1], game)
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 0,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_111.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_127.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 128,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_143.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 192,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_111.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 256,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_127.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 5,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_143.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 6,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_111.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 7,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_127.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 8,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_143.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 9,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_111.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 10,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_127.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 11,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_143.png',
                                         game))
    game.add_background(screen)
    screen = Screen([0, 1], game)
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 0,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_154.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_170.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 128,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_186.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 192,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_154.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 256,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_170.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 5,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_186.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 6,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_154.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 7,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_170.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 8,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_186.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 9,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_154.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 10,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_170.png',
                                         game))
    for i in range(20):
        screen.add_element(ScreenElement(i * 64, 64 * 11,
                                         r'assets\2dhandpainted_towntileset\Assets\64x64\Town@64x64_crop\Town@64x64_186.png',
                                         game))
    game.add_background(screen)
    game.run()


if __name__ == '__main__':
    main()
