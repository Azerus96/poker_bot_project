import tkinter as tk
from src.poker_bot import PokerBot

class PokerGUI:
    def __init__(self):
        self.bot = PokerBot()

        self.root = tk.Tk()
        self.root.title("Poker Bot")

        self.start_button = tk.Button(self.root, text="Запустить бота", command=self.start_bot)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Бот не работает")
        self.status_label.pack(pady=10)

    def start_bot(self):
        self.status_label.config(text="Бот запущен и работает!")
        self.bot.run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = PokerGUI()
    gui.run()
