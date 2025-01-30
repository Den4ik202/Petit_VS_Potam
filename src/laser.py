import pygame
import os
from src.settings import *


class Laser(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, angl: tuple, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(f'data/weapon/laser/laser_weapon.png'))
        rotate = {(-1, -1): 270+45+22, (1, -1): 270-45-22, (1, 1): 90+45+22, (-1, 1): 45-22}
        self.image = pygame.transform.rotate(self.image, rotate[angl])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites
        
        self.rect.x = x
        self.rect.y = y
        self.STATUS = 'WEAPON'
        self.mode = False
        self.angl = angl
        self.laser = None
        self.last_time = 0
        
    def update(self):
        if self.mode:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time >= COOLDOWN_LASER:
                self.last_time = pygame.time.get_ticks()
                self.laser.damage()
        
        
    def set_mode(self, state_mode: bool) -> None:
        self.mode = state_mode
        if self.mode:
            self.laser = Ray(self.rect.x, self.rect.y, self.angl, self.all_sprites)
            self.all_sprites.add(self.laser)
        else:
            self.laser.kill()
            
    def get_status(self) -> str:
        return self.STATUS
    
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



class Ray(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, angl: tuple, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(f'data/weapon/laser/ray_laser_weapon.png'))
        rotate = {(-1, -1): 270+45+22, (1, -1): 270-45-22, (1, 1): 90+45+22, (-1, 1): 45-22}
        self.image = pygame.transform.rotate(self.image, rotate[angl])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites
        
        self.rect.x = x
        self.rect.y = y
        if angl == (1, -1):
            self.rect.y = y - self.rect.h + 100
        if angl == (-1, 1):
            self.rect.x = x - self.rect.w + 100
        if angl == (-1, -1):
            self.rect.y = y - self.rect.h + 100
            self.rect.x = x - self.rect.w + 100
            
        self.STATUS = 'SUPPORT_WEAPON'
        
    def damage(self) -> None:
        robots = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s.get_status() == 'PLAYER'], False, pygame.sprite.collide_mask)
        
        if not robots:
            return
        
        for robot in robots:
            robot.damage(DAMAGE_LASER)
    
    def get_status(self) -> str:
        return self.STATUS
    
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