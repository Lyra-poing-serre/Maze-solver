from tkinter import Tk, BOTH, Canvas
from types import NoneType


class Window:
    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title = "pyMaze"
        self.root.maxsize(width, height)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

    def draw_line(self, line, fill_color: str ="black") -> None:
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, first: Point, second: Point) -> None:
        self.first = first
        self.second = second

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
            self.first.x,
            self.first.y,
            self.second.x,
            self.second.y,
            fill=fill_color,
            width=2,
        )

    def __repr__(self) -> str:
        return f"Line({repr(self.first)}, {repr(self.second)})"


class Cell:
    def __init__(self, window: Window, top_left=None, bot_right=None) -> None:
        self._win = window
        self.visited = False

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.top_left = top_left
        self.bot_right = bot_right

    def __repr__(self) -> str:
        return f"Cell(VISITED={self.visited}, TOP_LEFT={repr(self.top_left)}, BOT_RIGHT={repr(self.bot_right)}, WALL={self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall})"

    def draw(self, x1, y1, x2, y2) -> None:
        if isinstance(self._win, NoneType):
            return
        self.top_left = Point(x1, y1)
        self.bot_right = Point(x2, y2)
        top_right = Point(x2, y1)
        bot_left = Point(x1, y2)

        wall = Line(self.top_left, top_right)
        self._win.draw_line(wall, "black" if self.has_top_wall else "white")

        wall = Line(top_right, self.bot_right)
        self._win.draw_line(wall, "black" if self.has_right_wall else "white")

        wall = Line(bot_left, self.bot_right)
        self._win.draw_line(wall, "black" if self.has_bottom_wall else "white")

        wall = Line(self.top_left, bot_left)
        self._win.draw_line(wall, "black" if self.has_left_wall else "white")

    def get_middle(self):
        if not self.top_left and not self.bot_right:
            raise Exception("Cell position not defined !")
        return Point(
            (self.top_left.x + self.bot_right.x) / 2,
            (self.top_left.y + self.bot_right.y) / 2,
        )

    def draw_move(self, to_cell, undo=False):
        if isinstance(self._win, NoneType):
            return
        color = "gray" if undo else "red"
        self._win.draw_line(Line(self.get_middle(), to_cell.get_middle()), color)
