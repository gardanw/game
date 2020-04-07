import pygame
from PIL import Image


def pygame_img_save(path):
    img = pygame.image.load(path)
    pygame.image.save(img, path)


def pygame_img_scale(path, scale=(64, 64)):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, scale)
    new_path = path.split('.')
    new_path[-1] = f'_{scale[0]}x{scale[1]}.' + new_path[-1]
    pygame.image.save(img, ''.join(new_path))


# for i in range(1, 10):
#     pygame_img_save(f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/full_0{i}.png')
# for i in range(10, 241):
#     pygame_img_save(img, f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_{i}.png')

# side_list = ['Front', 'Back', 'Side']
# for side in side_list:
#     path_list = [f'Human ({side})/Bodies/body_', f'Human ({side})/Heads/head_', f'Human ({side})/Full/player_']
#     for path in path_list:
#         n = 32
#         for i in range(1, 10):
#             pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}.png', (n, n))
#         n = 64
#         for i in range(1, 10):
#             pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}.png', (n, n))
#         n = 32
#         for i in range(10, 241):
#             pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png', (n, n))
#         n = 64
#         for i in range(10, 241):
#             pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png', (n, n))
#         if 'Heads' in path:
#             n = 32
#             for i in range(241, 321):
#                 pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png', (n, n))
#             n = 64
#             for i in range(241, 321):
#                 pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png', (n, n))


filename = r'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png'
img = Image.open(filename)
img.save('assets/arrow_s_t.ico')
