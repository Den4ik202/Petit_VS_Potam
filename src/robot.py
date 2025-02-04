import pygame
import os
import src.settings


class Robot(pygame.sprite.Sprite):
    def __init__(self, iamgeName: str, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(f'data/{iamgeName}'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites
        
        self.rect.x = src.settings.WIDTH
        self.rect.y = src.settings.HEIGHT
        self.hp = src.settings.HP
        self.STATUS = 'PLAYER'
            
    def move(self, coef_x: int, coef_y: int, coef_slow: int) -> None:
        collision = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s != self and s.get_status() not in ['SUPPORT_WEAPON', 'SUPPORT']], False, pygame.sprite.collide_mask)
        if collision:
            self.rect.x += src.settings.SPEED * coef_x * coef_slow
            self.rect.y += src.settings.SPEED * coef_y * coef_slow
            return
        
        self.rect.x += src.settings.SPEED * coef_x * coef_slow
        self.rect.y += src.settings.SPEED * coef_y * coef_slow
        collision = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s != self and s.get_status() not in ['SUPPORT_WEAPON', 'SUPPORT']], False, pygame.sprite.collide_mask)
        if self.rect.x < 100 or self.rect.x + self.rect.w > 1100 or collision:
            self.rect.x -= src.settings.SPEED * coef_x * coef_slow
        
        if self.rect.y < 100 or self.rect.y + self.rect.h > 700 or collision:
            self.rect.y -= src.settings.SPEED * coef_y * coef_slow
        
    def get_hp(self) -> int:
        return self.hp
    
    def damage(self, damage: int) -> None:
        self.hp -= damage
    
    def set_position(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y
        self.hp = src.settings.HP
    
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