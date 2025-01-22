"""

"""


import pygame
import os


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

    def __init__(self, width=800, height=800, fps=60) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps

        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.title = "PetitPotam"
        self.game_end = False

        self.all_sprites = pygame.sprite.Group()
        
        
    def __del__(self) -> None:
        """"""
        pygame.quit()

    def __check_events(self) -> None:
        """"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True

    
    def __check_logic(self) -> None:
        """"""
        ...

    def __draw(self) -> None:
        """"""
        self.screen.fill(self.BLACK)

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

            self.clock.tick(self.FPS)
