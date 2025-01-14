import pygame
import os
import sys


class Racket(pygame.sprite.Sprite):
    def __init__(self, all_sprites, WIDTH, path_racket, x, y):
        super().__init__(all_sprites)
        self.WIDTH = WIDTH
        self.image = self.load_image(path_racket)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        all_sprites.add(self)

        self.rect.x = x   # начальное положение
        self.rect.y = y
        
    def move(self, pix):
        self.rect.x += pix     # двигаем влево/вправо
        if self.rect.x + self.rect.width > self.WIDTH or self.rect.x < 0:
            self.rect.x -= pix

    def load_image(self, name, colorkey=None):
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