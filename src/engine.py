"""

"""


from random import randint
import pygame
import os

from src.settings import *
from src.button import Button
from src.robot import Robot
from src.saw import Saw
from src.gun import Gun
from src.disk import Disk
from src.laser import Laser
from src.dirt import Dirt


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
        """"""
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.title = "PetitPotam"
        self.game_end = False
        self.main_game = False  # старт главной игры
        self.pause_game = False
        # 0 - игроки на пустом поле, 1 - появилась анархия, 2 - анархия, 3 - анархия останавливается
        self.state_timer = 0

        self.background = pygame.image.load(
            os.path.abspath('data/background.png'))
        self.field_game = pygame.image.load(
            os.path.abspath('data/field_game.png'))
        self.all_sprites = pygame.sprite.Group()
        # настройка шрифта
        pygame.font.init()
        self.font_text = pygame.font.SysFont('Comic Sans MS', 30)

        # инцилизация всех кнопок
        self.play_button = Button('play_button.png', 0, HEIGHT // 6)
        self.rule_button = Button('rule_button.png', WIDTH, HEIGHT // 3)
        self.setting_button = Button('setting_button.png', 0,  HEIGHT // 2)
        self.credit_button = Button(
            'credits_button.png', WIDTH, 2 * HEIGHT // 3)
        self.out_button = Button('out_button.png', 0, 5 * HEIGHT // 6)
        self.back_button = Button(
            'back_button.png', -self.play_button.original_size[0], 5 * HEIGHT // 6)
        self.back_button.set_target(-self.play_button.original_size[0])

        self.play_in_one_PC_button = Button(
            'play_in_one_PC_button.png', -self.play_button.original_size[0], HEIGHT // 3)
        self.play_local_inter_burron = Button(
            'play_local_inter_burron.png', WIDTH, 2 * HEIGHT // 3)
        
        self.play_in_one_PC_button.set_target(
            -self.play_button.original_size[0])
        self.play_local_inter_burron.set_target(
            WIDTH + self.play_button.original_size[0])
        
        self.pause_button = Button('pause_button.png', WIDTH, 0)
        self.pause_button.set_target(
            WIDTH + self.pause_button.original_size[0])
        
        self.pause_play_button = Button('pause_play_button.png', -100, HEIGHT // 3)
        self.pause_play_button.set_target(
            -self.pause_play_button.original_size[0])
        
        self.pause_home_button = Button('pause_home_button.png', WIDTH, 2 * HEIGHT // 3)
        self.pause_home_button.set_target(
            WIDTH + self.pause_home_button.original_size[0])

        self.robot_1_player = Robot('robot_player_1.png', self.all_sprites)
        self.robot_2_player = Robot('robot_player_2.png', self.all_sprites)

        # главыне кнопки
        self.all_sprites.add(self.play_button)
        self.all_sprites.add(self.rule_button)
        self.all_sprites.add(self.setting_button)
        self.all_sprites.add(self.credit_button)
        self.all_sprites.add(self.out_button)

        # второстепенные
        self.all_sprites.add(self.play_in_one_PC_button)
        self.all_sprites.add(self.play_local_inter_burron)
        self.all_sprites.add(self.back_button)
        self.all_sprites.add(self.pause_button)
        self.all_sprites.add(self.pause_play_button)
        self.all_sprites.add(self.pause_home_button)

        # игровые объекты
        self.all_sprites.add(self.robot_1_player)
        self.all_sprites.add(self.robot_2_player)

        self.move_robot_1_player = {(1, 0, 0, 0): lambda coef_slow = 1: self.robot_1_player.move(0, -1, coef_slow),
                                    (0, 1, 0, 0): lambda coef_slow = 1: self.robot_1_player.move(-1, 0, coef_slow),
                                    (0, 0, 1, 0): lambda coef_slow = 1: self.robot_1_player.move(0, 1, coef_slow),
                                    (0, 0, 0, 1): lambda coef_slow = 1: self.robot_1_player.move(1, 0, coef_slow),
                                    (1, 1, 0, 0): lambda coef_slow = 1: self.robot_1_player.move(-1, -1, coef_slow),
                                    (1, 0, 0, 1): lambda coef_slow = 1: self.robot_1_player.move(1, -1, coef_slow),
                                    (0, 1, 1, 0): lambda coef_slow = 1: self.robot_1_player.move(-1, 1, coef_slow),
                                    (0, 0, 1, 1): lambda coef_slow = 1: self.robot_1_player.move(1, 1, coef_slow)}  # WASD

        self.move_robot_2_player = {(1, 0, 0, 0): lambda coef_slow = 1: self.robot_2_player.move(0, -1, coef_slow),
                                    (0, 1, 0, 0): lambda coef_slow = 1: self.robot_2_player.move(-1, 0, coef_slow),
                                    (0, 0, 1, 0): lambda coef_slow = 1: self.robot_2_player.move(0, 1, coef_slow),
                                    (0, 0, 0, 1): lambda coef_slow = 1: self.robot_2_player.move(1, 0, coef_slow),
                                    (1, 1, 0, 0): lambda coef_slow = 1: self.robot_2_player.move(-1, -1, coef_slow),
                                    (1, 0, 0, 1): lambda coef_slow = 1: self.robot_2_player.move(1, -1, coef_slow),
                                    (0, 1, 1, 0): lambda coef_slow = 1: self.robot_2_player.move(-1, 1, coef_slow),
                                    (0, 0, 1, 1): lambda coef_slow = 1: self.robot_2_player.move(1, 1, coef_slow)}  # WASD

    def __del__(self) -> None:
        """"""
        pygame.quit()

    def __check_events(self) -> None:
        """"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True

            # =========== начало обработок кнопок ============
            if self.play_button.handle_event(event):
                self.play_button.set_target(-self.play_button.original_size[0])
                self.rule_button.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.setting_button.set_target(
                    -self.setting_button.original_size[0])
                self.credit_button.set_target(
                    WIDTH + self.credit_button.original_size[0])
                self.out_button.set_target(-self.out_button.original_size[0])

                self.back_button.set_target(WIDTH // 2)
                self.play_in_one_PC_button.set_target(WIDTH // 2)
                self.play_local_inter_burron.set_target(WIDTH // 2)

            if self.rule_button.handle_event(event):
                self.play_button.set_target(-self.play_button.original_size[0])
                self.rule_button.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.setting_button.set_target(
                    -self.setting_button.original_size[0])
                self.credit_button.set_target(
                    WIDTH + self.credit_button.original_size[0])
                self.out_button.set_target(-self.out_button.original_size[0])

                self.back_button.set_target(WIDTH // 2)

            if self.setting_button.handle_event(event):
                self.play_button.set_target(-self.play_button.original_size[0])
                self.rule_button.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.setting_button.set_target(
                    -self.setting_button.original_size[0])
                self.credit_button.set_target(
                    WIDTH + self.credit_button.original_size[0])
                self.out_button.set_target(-self.out_button.original_size[0])

                self.back_button.set_target(WIDTH // 2)

            if self.credit_button.handle_event(event):
                self.play_button.set_target(-self.play_button.original_size[0])
                self.rule_button.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.setting_button.set_target(
                    -self.setting_button.original_size[0])
                self.credit_button.set_target(
                    WIDTH + self.credit_button.original_size[0])
                self.out_button.set_target(-self.out_button.original_size[0])

                self.back_button.set_target(WIDTH // 2)

            if self.out_button.handle_event(event):
                self.game_end = True

            if self.back_button.handle_event(event):
                self.play_in_one_PC_button.set_target(
                    -self.play_button.original_size[0])
                self.play_local_inter_burron.set_target(
                    WIDTH + self.play_button.original_size[0])
                self.back_button.set_target(-self.play_button.original_size[0])

                self.play_button.set_target(WIDTH // 2)
                self.rule_button.set_target(WIDTH // 2)
                self.setting_button.set_target(WIDTH // 2)
                self.credit_button.set_target(WIDTH // 2)
                self.out_button.set_target(WIDTH // 2)

            if self.play_in_one_PC_button.handle_event(event):
                self.main_game = True
                self.pause_button.set_target(
                    WIDTH-self.pause_button.original_size[0])
                self.play_in_one_PC_button.set_target(
                    -self.play_button.original_size[0])
                self.play_local_inter_burron.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.back_button.set_target(-self.play_button.original_size[0])
                self.robot_1_player.set_position(200, 200)
                self.robot_2_player.set_position(100, 100)

                self.last_timer_time = pygame.time.get_ticks()

            if self.pause_button.handle_event(event):
                self.pause_game = True
                self.set_pause_sprits(True)
                self.pause_play_button.set_target(WIDTH // 2)
                self.pause_home_button.set_target(WIDTH // 2)
            
            if self.pause_play_button.handle_event(event):
                self.pause_game = False
                self.set_pause_sprits(False)
                self.pause_play_button.set_target(-self.pause_play_button.original_size[0])
                self.pause_home_button.set_target(WIDTH + self.pause_home_button.original_size[0])
            
            if self.pause_home_button.handle_event(event):
                self.pause_game = False
                self.set_pause_sprits(False)
                self.kill_sprite(('WEAPON', 'SUPPORT_WEAPON', 'SUPPORT'))
                self.main_game = False
                self.play_button.set_target(WIDTH // 2)
                self.rule_button.set_target(WIDTH // 2)
                self.setting_button.set_target(WIDTH // 2)
                self.credit_button.set_target(WIDTH // 2)
                self.out_button.set_target(WIDTH // 2)
                
                self.robot_1_player.set_position(WIDTH, HEIGHT)
                self.robot_2_player.set_position(WIDTH, HEIGHT)
                self.pause_button.set_target(WIDTH + self.pause_home_button.original_size[0])
                self.pause_play_button.set_target(-self.pause_play_button.original_size[0])
                self.pause_home_button.set_target(WIDTH + self.pause_home_button.original_size[0])
            # ====================== клавиатура ==================================

        if self.main_game and not self.pause_game:   # движение
            keys = pygame.key.get_pressed()
            keys = ((keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d]),
                    (keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_DOWN], keys[pygame.K_RIGHT]))

            colision_robot_1 = pygame.sprite.spritecollide(self.robot_1_player, [s for s in self.all_sprites if s.get_status() in [
                                                           'SUPPORT_WEAPON', 'SUPPORT']], False, pygame.sprite.collide_mask)
            colision_robot_2 = pygame.sprite.spritecollide(self.robot_2_player, [s for s in self.all_sprites if s.get_status() in [
                                                           'SUPPORT_WEAPON', 'SUPPORT']], False, pygame.sprite.collide_mask)

            if keys[0] in self.move_robot_1_player.keys():
                self.move_robot_1_player[keys[0]](
                    SLOWING_SPEED if colision_robot_1 else 1)

            if keys[1] in self.move_robot_2_player.keys():
                self.move_robot_2_player[keys[1]](
                    SLOWING_SPEED if colision_robot_2 else 1)

    def __check_logic(self) -> None:
        """"""
        if not self.main_game or self.pause_game:
            return

        current_time = pygame.time.get_ticks()

        if self.state_timer in [0, 2]:
            if current_time - self.last_timer_time >= TIMER_INTERVAL:   # прошел интервал времени
                self.last_timer_time = pygame.time.get_ticks()

                if self.state_timer == 0:  # создание анархии
                    self.create_weapon()
                else:   # остановить анархию
                    self.stop_anarxiya()

                self.state_timer = (self.state_timer + 1) % 4
        else:
            if current_time - self.last_timer_time >= TIMER_SEE:   # прошел интервал для просмотра
                self.last_timer_time = pygame.time.get_ticks()

                if self.state_timer == 1:
                    self.start_anarxiya()
                else:
                    self.kill_sprite(('WEAPON', 'SUPPORT'))
                # если 1 - запускаем анархию, 3 - удалить орудия
                # заспавнить анархию (начальный момент)

                self.state_timer = (self.state_timer + 1) % 4

        # ==================== ПРОВЕРКА НА ПРОИГРЫШ =====================
        if self.robot_1_player.get_hp() <= 0 or self.robot_2_player.get_hp() <= 0:
                self.pause_game = True
                self.set_pause_sprits(True)
                self.pause_button.set_target(WIDTH + self.pause_home_button.original_size[0])
                self.pause_home_button.set_target(WIDTH // 2)
        
    def start_anarxiya(self) -> None:
        for s in self.all_sprites:
            if s.get_status() == 'WEAPON':
                s.set_mode(True)

    def stop_anarxiya(self) -> None:
        for s in self.all_sprites:
            if s.get_status() == 'WEAPON':
                s.set_mode(False)

    def create_weapon(self) -> None:
        count_weapon = randint(1, MAX_COUNT_WEAPON)
        position = randint(1, 5)
        
        for x, y in COORDINATE_DISK[position]:
            if randint(0, 100) <= CHANCE_APPEARANCE_DISK:
                self.all_sprites.add(Disk(x, y, self.all_sprites))
        count_weapon -= 1

        if not count_weapon:  # больше нельзя ставить
            return self.create_dirt()

        for x, y, angl in COORDINATE_GUN:
            if randint(0, 100) <= CHANCE_APPEARANCE_GUN:
                self.all_sprites.add(Gun(x, y, angl, self.all_sprites))
        count_weapon -= 1

        if not count_weapon:  # больше нельзя ставить
            return self.create_dirt()

        for x, y, angl in COORDINATE_LASER:
            if randint(0, 100) <= CHANCE_APPEARANCE_LASER:
                self.all_sprites.add(Laser(x, y, angl, self.all_sprites))
        count_weapon -= 1

        self.create_dirt()

    def create_dirt(self) -> None:
        count_dirt = randint(0, MAX_COUNT_DIRT)
        for _ in range(count_dirt):
            self.all_sprites.add(Dirt(randint(200, 800), randint(200, 500)))

    def kill_sprite(self, sprite_kill: tuple) -> None:
        for s in self.all_sprites:
            if s.get_status() in sprite_kill:
                pass
                s.kill()

    def set_pause_sprits(self, state_pause: bool) -> None:
        for sprite in self.all_sprites:
            if sprite.get_status() in ['WEAPON', 'SUPPORT_WEAPON']:
                sprite.pause(state_pause)

    def __draw(self) -> None:
        """"""
        if self.main_game:
            self.screen.blit(self.field_game, (0, 0))
            text_surface = self.font_text.render(
                f'{self.robot_1_player.get_hp()} {self.robot_2_player.get_hp()}', False, (0, 0, 0))
            self.screen.blit(text_surface, (WIDTH // 3, 0))
        else:
            self.screen.blit(self.background, (0, 0))

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
