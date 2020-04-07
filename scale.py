import pygame
from PIL import Image

# for i in range(1, 10):
#     img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/full_0{i}.png')
#     pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_0{i}.png')
# for i in range(10, 241):
#     img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/full_{i}.png')
#     pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/Human (Back)/Full/player_{i}.png')

# side_list = ['Front', 'Back', 'Side']
# for side in side_list:
#     path_list = [f'Human ({side})/Bodies/body_', f'Human ({side})/Heads/head_', f'Human ({side})/Full/player_']
#     for path in path_list:
#
#         n = 32
#         for i in range(1, 10):
#             img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}.png')
#             img = pygame.transform.scale(img, (n, n))
#             pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}_{n}.png')
#
#         n = 64
#         for i in range(1, 10):
#             img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}.png')
#             img = pygame.transform.scale(img, (n, n))
#             pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}0{i}_{n}.png')
#
#         n = 32
#         for i in range(10, 241):
#             img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png')
#             img = pygame.transform.scale(img, (n, n))
#             pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}_{n}.png')
#
#         n = 64
#         for i in range(10, 241):
#             img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png')
#             img = pygame.transform.scale(img, (n, n))
#             pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}_{n}.png')
#
#         if 'Heads' in path:
#             n = 32
#             for i in range(241, 321):
#                 img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png')
#                 img = pygame.transform.scale(img, (n, n))
#                 pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}_{n}.png')
#
#             n = 64
#             for i in range(241, 321):
#                 img = pygame.image.load(f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}.png')
#                 img = pygame.transform.scale(img, (n, n))
#                 pygame.image.save(img, f'assets/7soulsrpggraphics_sprites/Assets/{path}{i}_{n}.png')

filename = r'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png'
img = Image.open(filename)
img.save('assets/arrow_s_t.ico')
