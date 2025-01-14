# ----------- импортирование библиотек ----------------
import pygame
import os
import sys
from random import randint

# --------------- импорт кода ------------------------
sys.path.append(os.path.join('code'))
from bullet import Bullet
from racket import Racket
from ship import Ship

    

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    PIX = 20  # на сколько двигаем ракетку
    FPS = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()  # все спрайты на экране
    button_left = pygame.K_a
    button_right = pygame.K_d
    
    ship1 = Ship(all_sprites, os.path.join('data', 'ship1.png'), 0, 635)         # начальное инцилизация обьектов
    ship2 = Ship(all_sprites, os.path.join('data', 'ship2.png'), 0, 0)
    racket1 = Racket(all_sprites, WIDTH, os.path.join('data', 'racket1.png'), 0, 485)
    racket2 = Racket(all_sprites, WIDTH, os.path.join('data', 'racket2.png'), 0, 150)
    
    while running:  # главный игровой цикл
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == button_left:              # при нажатии на кнопку 
                racket1.move(-PIX)
                
            elif event.type == pygame.KEYDOWN and event.key == button_right:
                racket1.move(PIX)
            
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()  # смена кадра

        clock.tick(FPS)