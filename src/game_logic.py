class PokerGame:
    def __init__(self):
        self.hand = []  # Текущая рука (например, две карты)
        self.board = [] # Карты на столе

    def evaluate_hand(self):
        """
        Оценить силу текущей руки.
        """
        # Пример: если есть пара, возвращаем "high_pair"
        ranks = [card.rank for card in self.hand + self.board]

        if ranks.count(self.hand[0].rank) == 2:
            return "high_pair"
        # Добавить дополнительную логику оценки руки
        return "weak_hand"

    def update_hand(self, hand):
        self.hand = hand

    def update_board(self, board):
        self.board = board

# Пример карты
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
