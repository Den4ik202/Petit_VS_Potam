import pygame
import os
from src.settings import *


class Robot(pygame.sprite.Sprite):
    def __init__(self, iamgeName: str) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(f'data/{iamgeName}'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect.x = WIDTH
        self.rect.y = HEIGHT
        self.hp = HP
        
    def update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # наноситься урон
        
    def move(self, coef_x: int, coef_y: int) -> None:
        self.rect.x += SPEED * coef_x
        self.rect.y += SPEED * coef_y
        
        if self.rect.x < 100 or self.rect.x + self.rect.w > 1100:
            self.rect.x -= SPEED * coef_x
        
        if self.rect.y < 100 or self.rect.y + self.rect.h > 700:
            self.rect.y -= SPEED * coef_y
        
    
    def set_damage(self, damage: int) -> bool:
        self.hp -= damage
        if self.hp <= 0:
            return True
        return False
    
    def set_position(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y
    
    def load_image(self, name, colorkey=None) -> pygame.image:
        image = pygame.image.load(name)

        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image