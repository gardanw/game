from mymodules.Game import Game
from mymodules.Player import Player


def load_img(path):
    pass


def main():
    game = Game("arrow", 'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png')
    side = []
    back = []
    front = []
    for i in range(1, 5):
        side.append(f'assets/7soulsrpggraphics_sprites/Assets/Human (Side)/Full/player_0{i}_64.png')
        back.append(f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_0{i}_64.png')
        front.append(f'assets/7soulsrpggraphics_sprites/Assets/Human (Front)/Full/player_0{i}_64.png')
    player = Player(735, 268, 1, [side, back, front], game)
    game.add_element(player)
    game.run()


if __name__ == '__main__':
    main()
