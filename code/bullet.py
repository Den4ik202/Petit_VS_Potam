import pygame
import os
import sys
from random import randint


class Bullet(pygame.sprite.Sprite):
    def __init__(self, all_sprites, path_bullet, x, y):
        super().__init__(all_sprites)
        self.image = self.load_image(path_bullet, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = x
        self.rect.y = y
        
    def update(self, coor):          # обновление координат
        x, y = coor
        coor_x_in_rect = self.rect.x < x < self.rect.x + 100
        coor_y_in_rect = self.rect.y < y < self.rect.y + 101

    
    def load_image(self, name, colorkey=None):    # загрузка изображения
            if not os.path.isfile(name):
                print(f"Файл с изображением '{name}' не найден")
                sys.exit()
            image = pygame.image.load(name)

            if colorkey is not None:
                image = image.convert()
                if colorkey == -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey)
            else:
                image = image.convert_alpha()
            return image