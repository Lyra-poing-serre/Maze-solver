from src.graphics import Window
from src.game_elements import Maze


def main():
    width, height = 1920, 1080
    maze = Maze(0, 0, 10, 5, 192, 216, Window(width, height))
    maze._win.wait_for_close()

if __name__ == "__main__":
    main()
