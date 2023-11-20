import tkinter as tk
from GUI.MainMenu import Main_menu


def main():
    root = tk.Tk()
    root.title("Minesweeper")
    Main_menu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
