import time
import random

from src.graphics import Cell, Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if seed:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells: list[list[Cell]] = list(
            [Cell(self._win)] * self.num_rows for _ in range(self.num_cols)
        )
        for y in range(self.num_cols):
            for x in range(self.num_rows):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        if self._win is None:
            return

        x1 = self.x1 + x * self._cell_size_x
        y1 = self.y1 + y * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[y][x].draw(x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y)
        print(f"new cell : {x1}, {y1} | {x2}, {y2}")
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)


    def _break_walls_r(self, x, y):
        self._cells[y][x].visited = True
        while True:
            to_visit = []
            if x - 1 >=0:
                adj = self._cells[y][x - 1]
                if not adj.visited:
                    to_visit.append((y, x - 1))
            if x + 1 < self.num_rows:
                adj = self._cells[y][x + 1]
                if not adj.visited:
                    to_visit.append((y, x + 1))
            if y - 1 >=0:
                adj = self._cells[y - 1][x]
                if not adj.visited:
                    to_visit.append((y - 1, x))
            if y + 1 < self.num_rows:
                adj = self._cells[y + 1][x]
                if not adj.visited:
                    to_visit.append((y + 1, x))

            if not to_visit:
                self._cells[y][x].draw()
                return
            selected_x, selected_y = random.choice(to_visit)

            x1, y1 = self._cells[y][x].top_left
            x2, y2 = self._cells[y][x].bot_right
            top_right = Point(x2, y1)
            bot_left = Point(x1, y2)

            if top_right == self._cells[selected_y][selected_x].bot_right:
                self._cells[y][x].has_top_wall = False
                self._cells[selected_y][selected_x].has_bottom_wall = False
            elif top_right == self._cells[selected_y][selected_x].top_left:
                self._cells[y][x].has_right_wall = False
                self._cells[selected_y][selected_x].has_left_wall = False
            elif bot_left == self._cells[selected_y][selected_x].top_left:
                self._cells[y][x].has_bottom_wall = False
                self._cells[selected_y][selected_x].has_top_wall = False
            elif bot_left == self._cells[selected_y][selected_x].bot_right:
                self._cells[y][x].has_left_wall = False
                self._cells[selected_y][selected_x].has_right_wall = False
            else:
                raise Exception(f"{self._cells[y][x]} n'est pas à côté de {self._cells[selected_y][selected_x]}")

            self._break_walls_r(selected_x, selected_y)
