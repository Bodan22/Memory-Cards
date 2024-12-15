import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Card Game")
        self.master.geometry("400x450")

        self.symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:8] * 2
        random.shuffle(self.symbols)
        self.board = [self.symbols[i:i+4] for i in range(0, 16, 4)]
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        self.revealed = [[False for _ in range(4)] for _ in range(4)]
        self.first_guess = None
        self.pairs_found = 0
        self.moves = 0

        self.create_widgets()

    def create_widgets(self):
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(pady=20)

        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.game_frame, text="", width=8, height=4,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn

        self.info_frame = tk.Frame(self.master)
        self.info_frame.pack(pady=10)

        self.moves_label = tk.Label(self.info_frame, text="Moves: 0")
        self.moves_label.pack(side=tk.LEFT, padx=10)

        self.pairs_label = tk.Label(self.info_frame, text="Pairs Found: 0")
        self.pairs_label.pack(side=tk.LEFT, padx=10)

    def on_click(self, row, col):
        if self.revealed[row][col]:
            return

        self.buttons[row][col].config(text=self.board[row][col])
        self.revealed[row][col] = True

        if self.first_guess is None:
            self.first_guess = (row, col)
        else:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")

            if self.board[row][col] == self.board[self.first_guess[0]][self.first_guess[1]]:
                self.pairs_found += 1
                self.pairs_label.config(text=f"Pairs Found: {self.pairs_found}")
                if self.pairs_found == 8:
                    messagebox.showinfo("Congratulations!", f"You won in {self.moves} moves!")
            else:
                self.master.after(1000, self.hide_cards, row, col, self.first_guess[0], self.first_guess[1])

            self.first_guess = None

    def hide_cards(self, row1, col1, row2, col2):
        self.buttons[row1][col1].config(text="")
        self.buttons[row2][col2].config(text="")
        self.revealed[row1][col1] = False
        self.revealed[row2][col2] = False

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
