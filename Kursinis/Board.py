import random
from Cell import Cell


class Board:
    def __init__(self, width, height, total_mines):
        self.width = width
        self.height = height
        self.total_mines = total_mines
        self.cells = [[Cell(x, y, None, self) for x in range(width)] for y in range(height)]
        self.populate_mines()
        self.calculate_adjacent_mines()

    def set_buttons(self, buttons):
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                cell.gui_button = buttons[y][x]

    def populate_mines(self):
        mines_placed = 0
        while mines_placed < self.total_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.cells[y][x].is_mine:
                self.cells[y][x].is_mine = True
                mines_placed += 1

    def get_cell_by_axis(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        return None

    def calculate_adjacent_mines(self):
        for row in self.cells:
            for cell in row:
                cell.adjacent_mines = cell.surrounded_cells_mines_length

    def get_surrounding_cells(self, x, y):
        cells = [
            self.get_cell_by_axis(x - 1, y - 1),
            self.get_cell_by_axis(x - 1, y),
            self.get_cell_by_axis(x - 1, y + 1),
            self.get_cell_by_axis(x, y - 1),
            self.get_cell_by_axis(x + 1, y - 1),
            self.get_cell_by_axis(x + 1, y),
            self.get_cell_by_axis(x + 1, y + 1),
            self.get_cell_by_axis(x, y + 1)
        ]
        return [cell for cell in cells if cell is not None]




