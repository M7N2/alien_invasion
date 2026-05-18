import json
import os

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализация статистики."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры.""" 
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Загружает рекорд из файла."""
        filename = 'high_score.json'

        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                return 0
            else:
                return 0

    def save_high_score(self):
        """Сохраняет рекорд в файл."""
        filename = 'high_score.json'
        try:
            with open(filename, 'w') as f:
                json.dump(self.high_score, f)
        except Exception:
            pass        
