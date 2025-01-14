import pygame
import os
import sys

class Ship(pygame.sprite.Sprite):
    def __init__(self, all_sprites, path_ship, x, y):
        super().__init__(all_sprites)
        self.image = self.load_image(path_ship, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        all_sprites.add(self)
        
        self.rect.x = x
        self.rect.y = y
        
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