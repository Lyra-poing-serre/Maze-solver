from src.graphics import *


def main():
    width, height = 1920, 1080
    win = Window(width, height)
    mid_bot = Cell(
        win,
        Point(width/2, height/2),
        Point(width, height)
    )
    mid_bot.draw()
    mid = Cell(
        win,
        Point(width * 5/8, height * 5/8),
        Point(width * 7/8, height * 7/8),
        top_wall=False,
        left_wall=False
    )
    mid.draw()
    win.wait_for_close()


if __name__ == '__main__':
    main()