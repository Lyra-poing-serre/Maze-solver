import time

from src.graphics import Cell, Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None

        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = list(
            [Cell(self._win)] * self.num_rows for _ in range(self.num_cols)
        )
        for y in range(self.num_cols):
            for x in range(self.num_rows):
                self._draw_cell(x, y)

    def _draw_cell(self, x, y):
        if self._win is None:
            return
        x1 = self.x1 + x * self._cell_size_x
        y1 = self.y1 + y * self._cell_size_y

        self._cells[y][x].top_left = Point(x1, y1)
        self._cells[y][x].bot_right = Point(
            x1 + self._cell_size_x, y1 + self._cell_size_y
        )
        self._cells[y][x].has_left_wall = True
        self._cells[y][x].has_right_wall = True
        self._cells[y][x].has_top_wall = True
        self._cells[y][x].has_bottom_wall = True
        print(f"{x} | {y}", self._cells[y][x])
        self._cells[y][x].draw()
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)
