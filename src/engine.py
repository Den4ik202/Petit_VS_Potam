"""

"""


import pygame
import os
from src.setting import *
from src.button import Button

class Engine:
    """
    ...
    
    Args:
        __init__(self, width, height, fps)
            ...
            Args: ...
            Returns: ...

        __del__(self)
            ...
            Args: ...
            Returns: ...

        __check_events(self):
            ...
            Args: ...
            Returns: ...

        __check_logic(self):
            ...
            Args: ...
            Returns: ...
        
        __draw(self):
            ...
            Args: ...
            Returns: ...

        run(self):
            ...
            Args: ...
            Returns: ...
    """

    def __init__(self) -> None:

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.title = "PetitPotam"
        self.game_end = False

        self.play_button = Button('play_button.png', 0, HEIGHT // 4)
        self.rule_button = Button('play_button.png', WIDTH, HEIGHT // 2)
        self.setting_button = Button('play_button.png', 0,3 * HEIGHT // 4)
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.play_button)
        self.all_sprites.add(self.rule_button)
        self.all_sprites.add(self.setting_button)
        
    def __del__(self) -> None:
        """"""
        pygame.quit()

    def __check_events(self) -> None:
        """"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True
            
            if self.play_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.play_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
            
            if self.rule_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.play_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
            
            if self.setting_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.play_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]

    
    def __check_logic(self) -> None:
        """"""
        ...

    def __draw(self) -> None:
        """"""
        self.screen.fill(BLACK)

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        pygame.display.flip()

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption(self.title)

        while not self.game_end:
            self.__check_events()
            self.__check_logic()
            self.__draw()
            self.clock.tick(FPS)
