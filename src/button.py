import pygame
import os
<<<<<<< HEAD

=======
>>>>>>> d0ee9c37f4c9fc6382b66477e8335952b077f2eb
from src.settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, iamgeName: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.original_image = self.load_image(
            os.path.abspath(f'data/button/{iamgeName}'))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = x
        self.rect.y = y
        self.original_size = self.image.get_size()
        self.target_coor = WIDTH // 2            # цель, куда двигаться кнопке
        self.STATUS = 'BUTTON'

    def update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if abs(self.target_coor - self.rect.centerx) <= 10:    # кнопка находиться на своем месте
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.image = pygame.transform.scale(
                    self.original_image, (self.original_size[0] * 1.5, self.original_size[1] * 1.5))
            else:
                self.image = pygame.transform.scale(
                    self.original_image, (self.original_size[0], self.original_size[1]))

            self.rect = self.image.get_rect(center=self.rect.center)
            return

        self.rect.x += (self.target_coor - self.rect.centerx) * \
            0.05               # двигаем

    def set_target(self, coor: int) -> None:
        self.target_coor = coor

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

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
<<<<<<< HEAD
    
    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
=======
>>>>>>> d0ee9c37f4c9fc6382b66477e8335952b077f2eb
