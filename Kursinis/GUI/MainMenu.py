import tkinter as tk
from GUI.GameGUI import Minesweeper_GUI


class Main_menu:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.center_window(300, 200)
        self.create_buttons()

    def center_window(self, width=300, height=200):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def create_buttons(self):
        new_game_btn = tk.Button(self.root, text="New Game", fg="black", bg="white", command=self.new_game)
        new_game_btn.pack(pady=11)
        high_scores_btn = tk.Button(self.root, text="Exit", fg="black", bg="white", command=self.exit_game)
        high_scores_btn.pack(pady=11)

    def new_game(self):
        self.open_new_window(Minesweeper_GUI)

    def open_new_window(self, window_class):
        new_window = tk.Toplevel(self.root)
        new_window.title("Minesweeper")
        window_class(new_window)

    def exit_game(self):
        self.root.destroy()
