import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                return f"Player {'O' if self.current_player == 'X' else 'X'} wins!"
            elif ' ' not in self.board:
                return "It's a tie!"
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
        else:
            return "Invalid move. Try again."
        return None





    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def reset_board(self):
        self.board = [' ']*9
        self.current_player = 'X'

class GuiTicTacToe:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = []
        self.setup_board()

    def setup_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2)
                button.grid(row=i, column=j)
                button.config(command=lambda button=button, row=i, col=j: self.on_button_click(button, row, col))
                self.buttons.append(button)

    def on_button_click(self, button, row, col):
        index = row * 3 + col
        result = self.game.make_move(index)
        if result:
            messagebox.showinfo("Game Over", result)
            self.game.reset_board()
            self.update_buttons()
        else:
            button.config(text=self.game.current_player)

    def update_buttons(self):
        for i in range(9):
            self.buttons[i].config(text=self.game.board[i])


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game = TicTacToe()
    gui_game = GuiTicTacToe(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()
