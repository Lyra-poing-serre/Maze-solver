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
    )
    mid.draw()
    rdm = Cell(
        win,
        Point(width * 1 / 8, height * 1 / 8),
        Point(width * 3 / 8, height * 3 / 8)
    )
    rdm.draw()
    mid.draw_move(rdm)
    win.wait_for_close()


if __name__ == '__main__':
    #main()
    width, height = 1920, 1080
    win = Window(width, height)
    print([Cell(win)] * 10)