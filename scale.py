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


def pil_crop(path, box):
    im = Image.open(path)
    width, height = im.size
    count = 1
    for i in range(0, width, box[0]):
        for j in range(0, height, box[1]):
            new_im = im.crop((j, i, j + box[0], i + box[1]))
            new_path = path.split('.')
            new_path[-1] = f'_{count}.' + new_path[-1]
            new_im.save(''.join(new_path))
            count += 1


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


# filename = r'assets/guiicons/Assets/GUI_Icons/GUI_Icons_png/transparent/arrow_s_t.png'
# img = Image.open(filename)
# img.save('assets/arrow_s_t.ico')


# n = 32
# for i in range(1, 10):
#     pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/Monster/Monsters/monster_0{i}.png', (n, n))
#
# n = 64
# for i in range(1, 10):
#     pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/Monster/Monsters/monster_0{i}.png', (n, n))

# n = 32
# for i in range(10, 229):
#     try:
#         pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/Monster/Monsters/monster_{i}.png', (n, n))
#     except:
#         print(f'nie ma {i}')
#
# n = 64
# for i in range(10, 229):
#     try:
#         pygame_img_scale(f'assets/7soulsrpggraphics_sprites/Assets/Monster/Monsters/monster_{i}.png', (n, n))
#     except:
#         print(f'nie ma {i}')

pil_crop('assets/2dhandpainted_towntileset/Assets/64x64/Town@64x64.png', (64, 64))
