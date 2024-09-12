from src.game_logic import PokerGame
from src.browser_automation import BrowserAutomation

class PokerBot:
    def __init__(self):
        self.game = PokerGame()
        self.browser = BrowserAutomation()

    def make_decision(self):
        """
        Принять решение в зависимости от текущей игровой ситуации.
        """
        # Пример логики: если есть пара, делаем колл
        hand_strength = self.game.evaluate_hand()

        if hand_strength == "high_pair":
            self.browser.call()
        elif hand_strength == "flush_draw":
            self.browser.raise_bet()
        else:
            self.browser.fold()

    def run(self):
        """
        Основная функция для запуска бота.
        """
        self.browser.start_browser()
        self.browser.navigate_to_game()

        while True:
            self.browser.update_game_state(self.game)
            self.make_decision()
