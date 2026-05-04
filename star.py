import pygame
from random import randint

class Star():
    """Класс управления звездами на фоне."""

    def __init__(self, ai_game):
        """Инициализирует звезду и ее позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузить изобрашение.
        self.image = pygame.image.load("images/star.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Случайная позиция.
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)

    def draw_star(self):
        """Рисует звезду."""
        self.screen.blit(self.image, self.rect)
