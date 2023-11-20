class Cell:
    def __init__(self, x, y, gui_button, board):
        self.x = x
        self.y = y
        self.board = board
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0
        self.gui_button = gui_button

    @property
    def surrounded_cells(self):
        return self.board.get_surrounding_cells(self.x, self.y)

    @property
    def surrounded_cells_mines_length(self):
        return sum(1 for cell in self.surrounded_cells if cell.is_mine)

    def toggle_flag(self):
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
            self.update_gui_representation()
        print(f"Toggling flag at ({self.x}, {self.y})")

    def reveal(self):
        if not self.is_flagged:
            self.is_revealed = True
            self.update_gui_representation()
            if self.adjacent_mines == 0:
                for adjacent_cell in self.surrounded_cells:
                    if not adjacent_cell.is_revealed and not adjacent_cell.is_flagged:
                        adjacent_cell.reveal()

    def safe_to_reveal(self):
        if not self.is_flagged and not self.is_revealed:
            self.reveal()
            return True
        return False

    def update_gui_representation(self):
        if self.gui_button is not None:
            if self.is_revealed:
                if self.is_mine:
                    self.gui_button.config(text='*')
                else:
                    self.gui_button.config(text=str(self.adjacent_mines))
            elif self.is_flagged:
                self.gui_button.config(text='F')
            else:
                self.gui_button.config(text='')
