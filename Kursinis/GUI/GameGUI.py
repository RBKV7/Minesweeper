import tkinter as tk
import tkinter.messagebox as messagebox
import config
from Board import Board


# todo: add a timer
# todo: add a mines counter
# todo: add a restart button
class Minesweeper_GUI:
    def __init__(self, root):
        self.root = root
        self.grid_height = config.height
        self.grid_width = config.width
        self.total_mines = config.total_mines
        self.buttons = []
        self.create_grid()
        self.board = Board(self.grid_width, self.grid_height, self.total_mines)
        self.board.set_buttons(self.buttons)
        self.initialize_gui()

    def initialize_gui(self):
        self.configure_grid_expansion()

    def create_grid(self):
        self.buttons = []
        for i in range(self.grid_height):
            row = []
            for j in range(self.grid_width):
                btn = tk.Button(self.root, text='')
                btn.grid(row=i, column=j, sticky='nsew')
                btn.bind("<Button-1>", lambda event, x=i, y=j: self.reveal_cell(y, x))
                btn.bind("<Button-2>", lambda event, x=i, y=j: self.flag_cell(y, x))

                row.append(btn)
            self.buttons.append(row)

    def configure_grid_expansion(self):
        for i in range(self.grid_height):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(self.grid_width):
            self.root.grid_columnconfigure(j, weight=1)

    def reveal_cell(self, x, y):
        cell = self.board.get_cell_by_axis(x, y)
        if cell and not cell.is_revealed:
            cell.reveal()
            if cell.is_mine:
                self.end_game(False)
            else:
                self.check_victory()

    def flag_cell(self, x, y):
        cell = self.board.get_cell_by_axis(x, y)
        if cell and not cell.is_revealed:
            cell.toggle_flag()

    def check_victory(self):
        for row in self.board.cells:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.end_game(True)

    def end_game(self, won):
        for row in self.board.cells:
            for cell in row:
                cell.reveal()
        if won:
            message = "Congratulations! You've won!"
        else:
            message = "Game Over! You've hit a mine!"

        tk.messagebox.showinfo("Game Over", message)
