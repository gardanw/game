from mymodules.Game import Game
from mymodules.Player import Player


def main():
    game = Game("arrow", 'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png')
    player = Player(735, 268, 3, ['assets/7soulsrpggraphics_sprites/Assets/Human (Side)/Full/player_01_64.png',
                                  'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_01_64.png',
                                  'assets/7soulsrpggraphics_sprites/Assets/Human (Front)/Full/player_01_64.png'], game)
    game.add_element(player)
    game.run()


if __name__ == '__main__':
    main()
