import pyray as rl
from colors import Colors as clr

def draw_checkerboard():
    pass

class Game():
    def __init__(self) -> None:
        self.grid = [[clr.nothing for _ in range(50)] for _ in range(50)]

        self.modes = ["color_picker", "edit", "menu"]
        self.selection = rl.Vector2(25,25)

        rl.init_window(1200,800,"TileEdit")
        rl.set_target_fps(60)

        while not rl.window_should_close():
            self.update()
            rl.begin_drawing()
            rl.clear_background(clr.raywhite)
            self.draw()
            rl.end_drawing()
        rl.close_window()

    def draw(self) -> None:
        pass

    def update(self) -> None:
        pass

if __name__ == "__main__":
    Game()
