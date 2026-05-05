import pygame
from random import randint

class Star(pygame.sprite.Sprite):
    """Класс управления звездами на фоне."""

    def __init__(self, ai_game):
        """Инициализирует звезду и ее позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Случайный размер.
        size = randint(1, 4)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Случайный оттенок белого/голубоватого.
        brightness = randint(180, 255)
        blue_tint = randint(200, 255)
        color = (brightness, brightness, blue_tint)

        # Прозрачность.
        alpha_value = randint(100, 220)

        # Рисуем круглую звезду.
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)
        
        self.image.set_alpha(alpha_value)
        self.rect = self.image.get_rect()

        # Случайная позиция.
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)

    def draw_star(self):
        """Рисует звезду."""
        self.screen.blit(self.image, self.rect)
