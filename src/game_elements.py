import time
import random

from src.graphics import Cell, Point


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        if seed:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for y in range(self.num_cols):
            for x in range(self.num_rows):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        if self._win is None:
            return

        x1 = self.x1 + y * self._cell_size_x
        y1 = self.y1 + x * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[y][x].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, y, x):
        self._cells[y][x].visited = True
        while True:
            to_visit = []

            if y > 0 and not self._cells[y - 1][x].visited:
                to_visit.append((y - 1, x))
            if y < self.num_cols - 1 and not self._cells[y + 1][x].visited:
                to_visit.append((y + 1, x))
            if x > 0 and not self._cells[y][x - 1].visited:
                to_visit.append((y, x - 1))
            if x < self.num_rows - 1 and not self._cells[y][x + 1].visited:
                to_visit.append((y, x + 1))

            if len(to_visit) == 0:
                self._draw_cell(y, x)
                return
            selected_y, selected_x = random.choice(to_visit)

            if x + 1 == selected_x:
                self._cells[y][x].has_bottom_wall = False
                self._cells[y][x + 1].has_top_wall = False
            if y + 1 == selected_y:
                self._cells[y][x].has_right_wall = False
                self._cells[y + 1][x].has_left_wall = False
            if x - 1 == selected_x:
                self._cells[y][x].has_top_wall = False
                self._cells[y][x - 1].has_bottom_wall = False
            if y - 1 == selected_y:
                self._cells[y][x].has_left_wall = False
                self._cells[y - 1][x].has_right_wall = False

            self._break_walls_r(selected_y, selected_x)

    def _reset_cells_visited(self):
        for y in range(self.num_cols):
            for x in range(self.num_rows):
                self._cells[y][x].visited = False
                print(self._cells[y][x])

    def _solve_r(self):
        pass
