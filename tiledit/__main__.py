import pyray as rl
from colors import Colors as clr
from colors import get_color_dict

class Selection():
    def __init__(self, pos: rl.Vector2, width:int, thickness:int) -> None:
        self.selection_clr = rl.Color(200,200,200,255)
        
        self.cycle_count = 0
        self.count = 0

        self.rect_above = rl.Rectangle(pos.x-thickness, pos.y-thickness,width+(thickness*2), thickness)
        self.rect_below = rl.Rectangle(pos.x-thickness, pos.y+width,width+(thickness*2), thickness)
        self.rect_left = rl.Rectangle(pos.x-thickness, pos.y-thickness, thickness, width+(thickness*2))
        self.rect_right = rl.Rectangle(pos.x+width, pos.y-thickness, thickness,width+(thickness*2))
    
    def draw(self):
        rl.draw_rectangle_rec(self.rect_above, self.selection_clr)
        rl.draw_rectangle_rec(self.rect_below, self.selection_clr)
        rl.draw_rectangle_rec(self.rect_left, self.selection_clr)
        rl.draw_rectangle_rec(self.rect_right, self.selection_clr)
    
    def update(self):
        self.count += 1
        if self.count % 10 == 0:
            self.cycle_count += 1
        
        if self.cycle_count % 2 == 0:
            self.selection_clr.a -= 35
        else:
            self.selection_clr.a += 35

def draw_checkerboard(base_color: rl.Color, alt_color: rl.Color, begin: int, length: int, tilesize: int):
        is_alt_color: bool = True
        for y in range(begin*tilesize, begin+(length*tilesize*2), tilesize):
            is_alt_color = not is_alt_color
            for x in range(begin*tilesize, begin+(length*tilesize*2), tilesize):
                if is_alt_color:
                    rl.draw_rectangle(x,y,tilesize,tilesize, alt_color)
                    is_alt_color = not is_alt_color
                else:
                    rl.draw_rectangle(x,y,tilesize,tilesize, base_color)
                    is_alt_color = not is_alt_color
            is_alt_color = not is_alt_color

class Game():
    def __init__(self) -> None:
        self.grid = [[clr.nothing for _ in range(50)] for _ in range(50)]
        
        self.clr_dict = get_color_dict()
        self.modes = ["color_picker", "edit", "menu"]
        self.selection = rl.Vector2(25,25)

        rl.init_window(1200,800,"TileEdit")
        rl.set_target_fps(60)

        self.window_banner = "[NEW FILE]"
        self.window_title = f"TileEdit -- {self.window_banner}"
        self.test_selection = Selection(rl.Vector2(10,10),35,5)

        while not rl.window_should_close():
            self.update()
            rl.begin_drawing()
            rl.clear_background(clr.raywhite)
            self.draw()
            rl.end_drawing()
        rl.close_window()

    def draw(self) -> None:
        self.test_selection.draw()
        rl.draw_text(self.window_title, 10, 10, 30, clr.black)
        rl.draw_rectangle(100,100,525,525,clr.gray) # border
        draw_checkerboard(rl.Color(235,235,235,255), clr.raywhite, 18,50, 6)
        rl.draw_rectangle(10,650,1180,140,rl.Color(235,235,235,255)) # toolbox btm
        rl.draw_rectangle(650,100,500,525,rl.Color(235,235,235,255)) # toolbox right

        rl.draw_text("Colors", 660,110,30,clr.black)
        rl.draw_text("Toolbox -- Info", 20,660,20,clr.black)

    def update(self) -> None:
        self.test_selection.update()

if __name__ == "__main__":
    Game()
