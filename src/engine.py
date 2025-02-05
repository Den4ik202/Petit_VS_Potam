"""

"""


from random import randint
import pygame
import os

import src.settings
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
        WIDTH = src.settings.WIDTH
        HEIGHT = src.settings.HEIGHT

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
            'play_in_one_PC_button.png', -self.play_button.original_size[0], HEIGHT // 6)
        self.play_local_inter_burron = Button(
            'play_local_inter_burron.png', WIDTH, HEIGHT // 2)

        self.play_in_one_PC_button.set_target(
            -self.play_button.original_size[0])
        self.play_local_inter_burron.set_target(
            WIDTH + self.play_button.original_size[0])

        self.pause_button = Button('pause_button.png', WIDTH, 0)
        self.pause_button.set_target(
            WIDTH + self.pause_button.original_size[0])

        self.pause_play_button = Button(
            'pause_play_button.png', -270, HEIGHT // 3)
        self.pause_play_button.set_target(
            -self.pause_play_button.original_size[0])

        self.pause_home_button = Button(
            'pause_home_button.png', WIDTH, 2 * HEIGHT // 3)
        self.pause_home_button.set_target(
            WIDTH + self.pause_home_button.original_size[0])

        self.title_credits = Button('title_credits.png', -750, HEIGHT // 3)
        self.title_credits.set_target(
            -self.title_credits.original_size[0])

        self.title_rules = Button('title_rules.png', -750, HEIGHT // 3)
        self.title_rules.set_target(
            -self.title_rules.original_size[0])

        self.petit_win = Button('petit_win.png', -750, HEIGHT // 10)
        self.petit_win.set_target(
            -self.petit_win.original_size[0])

        self.potam_win = Button('potam_win.png', -750, HEIGHT // 10)
        self.potam_win.set_target(
            -self.potam_win.original_size[0])

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

        # тайтлы
        self.all_sprites.add(self.title_credits)
        self.all_sprites.add(self.title_rules)
        self.all_sprites.add(self.petit_win)
        self.all_sprites.add(self.potam_win)

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
        WIDTH = src.settings.WIDTH
        HEIGHT = src.settings.HEIGHT
        SLOWING_SPEED = src.settings.SLOWING_SPEED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True

            # =========== начало обработок кнопок ============
            if self.play_button.handle_event(event):
                self.update_settings()

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
                self.title_rules.set_target(WIDTH // 2)

            if self.setting_button.handle_event(event):
                if os.name == 'nt':  # Для Windows
                    os.startfile('settings.txt')
                elif os.name == 'posix':  # Для Linux/MacOS
                    os.system(f'xdg-open settings.txt')  # Для Linux
                else:
                    os.system(f'open settings.txt')

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

                self.title_credits.set_target(WIDTH // 2)
                self.back_button.set_target(WIDTH // 2)

            if self.out_button.handle_event(event):
                self.game_end = True

            if self.back_button.handle_event(event):
                self.title_credits.set_target(
                    -self.title_credits.original_size[0])
                self.title_rules.set_target(-self.title_rules.original_size[0])

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
                    WIDTH-2*self.pause_button.original_size[0]//3)
                self.play_in_one_PC_button.set_target(
                    -self.play_button.original_size[0])
                self.play_local_inter_burron.set_target(
                    WIDTH + self.rule_button.original_size[0])
                self.back_button.set_target(-self.play_button.original_size[0])
                self.robot_1_player.set_position(200, 200)
                self.robot_2_player.set_position(600, 600)

                self.last_timer_time = pygame.time.get_ticks()

            if self.pause_button.handle_event(event):
                self.pause_game = True
                self.set_pause_sprits(True)
                self.pause_play_button.set_target(WIDTH // 2)
                self.pause_home_button.set_target(WIDTH // 2)

            if self.pause_play_button.handle_event(event):
                self.pause_game = False
                self.set_pause_sprits(False)
                self.pause_play_button.set_target(
                    -self.pause_play_button.original_size[0])
                self.pause_home_button.set_target(
                    WIDTH + self.pause_home_button.original_size[0])

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

                self.petit_win.set_target(-self.petit_win.original_size[0])
                self.potam_win.set_target(-self.potam_win.original_size[0])
                self.robot_1_player.set_position(WIDTH, HEIGHT)
                self.robot_2_player.set_position(WIDTH, HEIGHT)
                self.pause_button.set_target(
                    WIDTH + self.pause_home_button.original_size[0])
                self.pause_play_button.set_target(
                    -self.pause_play_button.original_size[0])
                self.pause_home_button.set_target(
                    WIDTH + self.pause_home_button.original_size[0])
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
        TIMER_INTERVAL = src.settings.TIMER_INTERVAL
        TIMER_SEE = src.settings.TIMER_SEE
        WIDTH = src.settings.WIDTH

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
            self.pause_button.set_target(
                WIDTH + self.pause_home_button.original_size[0])
            self.pause_home_button.set_target(WIDTH // 2)

            if self.robot_1_player.get_hp() <= 0:
                self.potam_win.set_target(WIDTH // 2)
            else:
                self.petit_win.set_target(WIDTH // 2)

    def start_anarxiya(self) -> None:
        for s in self.all_sprites:
            if s.get_status() == 'WEAPON':
                s.set_mode(True)
        for sound in self.all_sounds:
            sound.play()

    def stop_anarxiya(self) -> None:
        for s in self.all_sprites:
            if s.get_status() == 'WEAPON':
                s.set_mode(False)
        for sound in self.all_sounds:
            sound.stop()

    def create_weapon(self) -> None:
        count_weapon = randint(1, src.settings.MAX_COUNT_WEAPON)
        position = randint(1, 5)
        self.all_sounds = []

        cnt = 0
        for x, y in src.settings.COORDINATE_DISK[position]:
            if randint(0, 100) <= src.settings.CHANCE_APPEARANCE_DISK:
                cnt += 1
                self.all_sprites.add(Disk(x, y, self.all_sprites))
        if cnt:
            self.all_sounds.append(pygame.mixer.Sound('sounds\disk.mp3'))
            count_weapon -= 1

        if not count_weapon:  # больше нельзя ставить
            return self.create_dirt()

        cnt = 0
        for x, y, angl in src.settings.COORDINATE_GUN:
            if randint(0, 100) <= src.settings.CHANCE_APPEARANCE_GUN:
                cnt += 1
                self.all_sprites.add(Gun(x, y, angl, self.all_sprites))
        if cnt:
            count_weapon -= 1

        if not count_weapon:  # больше нельзя ставить
            return self.create_dirt()

        cnt = 0
        for x, y, angl in src.settings.COORDINATE_LASER:
            if randint(0, 100) <= src.settings.CHANCE_APPEARANCE_LASER:
                cnt += 1
                self.all_sprites.add(Laser(x, y, angl, self.all_sprites))
        if cnt:
            self.all_sounds.append(pygame.mixer.Sound('sounds\laser.mp3'))
            count_weapon -= 1

        self.create_dirt()

    def create_dirt(self) -> None:
        count_dirt = randint(0, src.settings.MAX_COUNT_DIRT)
        for _ in range(count_dirt):
            self.all_sprites.add(Dirt(randint(200, 800), randint(200, 500)))

    def kill_sprite(self, sprite_kill: tuple) -> None:
        for s in self.all_sprites:
            if s.get_status() in sprite_kill:
                pass
                s.kill()
        for sound in self.all_sounds:
            sound.stop()

    def set_pause_sprits(self, state_pause: bool) -> None:
        for sprite in self.all_sprites:
            if sprite.get_status() in ['WEAPON', 'SUPPORT_WEAPON']:
                sprite.pause(state_pause)

    def update_settings(self) -> None:         # обновление настроек
        with open('settings.txt', 'r', encoding='UTF-8') as file:
            all_line = tuple(
                map(lambda s: float(s.split()[-1].rstrip()), file.readlines()))
            src.settings.FPS = all_line[0]
            src.settings.TIMER_INTERVAL = all_line[1]
            src.settings.TIMER_SEE = all_line[2]
            src.settings.MAX_COUNT_WEAPON = all_line[3]
            src.settings.MAX_COUNT_DIRT = all_line[4]
            src.settings.SPEED = all_line[5]
            src.settings.HP = all_line[6]
            src.settings.SLOWING_SPEED = all_line[7]
            src.settings.DAMAGE_GUN = all_line[8]
            src.settings.SPEED_BULLET = all_line[9]
            src.settings.COOLDOWN_GUN = all_line[10]
            src.settings.CHANCE_APPEARANCE_GUN = all_line[11]
            src.settings.DAMAGE_LASER = all_line[12]
            src.settings.COOLDOWN_LASER = all_line[13]
            src.settings.CHANCE_APPEARANCE_LASER = all_line[14]
            src.settings.DAMAGE_DISK = all_line[15]
            src.settings.COOLDOWN_DISK = all_line[16]
            src.settings.CHANCE_APPEARANCE_DISK = all_line[17]

    def __draw(self) -> None:
        """"""
        if self.main_game:
            self.screen.blit(self.field_game, (0, 0))
        else:
            self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption(self.title)
        self.main_sound = pygame.mixer.Sound('sounds\main.mp3')
        self.main_sound.play(5)

        while not self.game_end:
            self.__check_events()
            self.__check_logic()
            self.__draw()
            self.clock.tick(src.settings.FPS)
