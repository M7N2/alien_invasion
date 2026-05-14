class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)
        
        # Настройки корабля.
        self.ship_limit = 3

        # Параметры снаряда.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
        self.bullets_allowed = 3

        # Настройки звезд.
        self.number_of_stars = 50

        # Настройки пришельцев.
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed =  3.0
        self.alien_speed = 1.0

        # Подсчет очков.
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо, а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает насстройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
    def set_hard_difficulty(self):
        """Устанавливает настройки для сложного режима."""
        self.ship_speed = 2.5
        self.bullet_speed = 4.5
        self.alien_speed = 1.8
        self.fleet_drop_speed = 15
        self.bullets_allowed = 3
        self.ship_limit = 2
