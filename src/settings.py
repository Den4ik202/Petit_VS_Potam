# ================== главный экран
FPS = 60
WIDTH = 1200
HEIGHT = 800
# ================== игровое поле
WIDTH_FIELD = 1000
HEIGHT_FIELD = 600
TIMER_INTERVAL = 2000   # время на отдых/битвы на поле
TIMER_SEE = 500         # время для того, чтоб увидить расположение анархии
MAX_COUNT_WEAPON = 4    # макс. количество ВИДОВ орудий  (мин 1, макс 4)
MAX_COUNT_DIRT = 0      # макс. количество грязи на поле
# ================== игрок
SPEED = 10
HP = 1000
SLOWING_SPEED = 0.3        # замедление при уроне
# ================== пушка
DAMAGE_GUN = 20
SPEED_BULLET = 5
COOLDOWN_GUN = 500
CHANCE_APPEARANCE_GUN = 60
COORDINATE_GUN = ((50, 0, (1, 1)), (250, 0, (1, 1)), (500, 0, (1, 1)), (750, 0, (-1, 1)), (1000, 0, (-1, 1)),
                  (50, 700, (1, -1)), (250, 700, (1, -1)), (500, 700, (-1, -1)), (750, 700, (-1, -1)), (1000, 700, (-1, -1)))
# ================== лазер
DAMAGE_LASER = 10
COOLDOWN_LASER = 100
CHANCE_APPEARANCE_LASER = 40
COORDINATE_LASER = ((0, 50, (1, 1)), (0, 600, (1, -1)), (1100, 50, (-1, 1)), (1100, 600, (-1, -1)))
# ================== пила (диск)
DAMAGE_DISK = 5
COOLDOWN_DISK = 50
CHANCE_APPEARANCE_DISK = 50
COORDINATE_DISK = {1: ((200, 200), (200, 500), (400, 350), (600, 200), (600, 500), (800, 350), (1000, 200), (1000, 500)),
                   2: ((200, 200), (200, 500), (400, 350), (600, 200), (600, 500), (800, 350), (1000, 200), (1000, 500)),
                   3: ((200, 350), (400, 350), (600, 200), (600, 500), (800, 350), (1000, 200), (1000, 500)),
                   4: ((200, 350), (400, 350), (600, 200), (600, 500), (800, 350), (1000, 200), (1000, 500)),
                   5: ()}
# ================== пила
DAMAGE_SAW = 5
COOLDOWN_SAW = 50
CHANCE_APPEARANCE_SAW = 40
COORDINATE_SAW = ((0, 50, (1, 1)), (0, 600, (1, -1)), (1100, 50, (-1, 1)), (1100, 600, (-1, -1)))
# ================== цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
