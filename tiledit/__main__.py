import pyray as rl
from colors import Colors
from colors import get_color_dict

class ColoredRect():
    def __init__(self, posx: float, posy: float, width: float, height: float, color: rl.Color) -> None:
        self.rect = rl.Rectangle(posx,posy,width,height)
        self.clr = color
    def draw(self):
        rl.draw_rectangle_rec(self.rect, self.clr)

class Selection():
    def __init__(self, pos: rl.Vector2, width:int, thickness:int) -> None:
        self.selection_clr = rl.Color(200,200,200,255)
        self.timer = 0

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
        self.timer += 1

        if self.timer % 60 == 0:
            self.selection_clr.a = 255
        elif self.timer % 60 == 30:
            self.selection_clr.a = 0


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
        self.grid = [[Colors.nothing for _ in range(50)] for _ in range(50)]
        
        self.clr_dict = get_color_dict()
        self.modes = ["color picker", "edit", "menu"]
        self.mode = "color picker"

        rl.init_window(1200,800,"TileEdit")
        rl.set_target_fps(60)

        self.window_banner = "[NEW FILE]"
        self.window_title = f"TileEdit -- {self.window_banner}"
        self.selection = Selection(rl.Vector2(660,150),40,5)

        rl.set_window_title(self.window_title)
        print(len(self.clr_dict))

        self.draw_color_ypos = 0
        self.draw_color_xpos = 660

        while not rl.window_should_close():
            self.update()
            rl.begin_drawing()
            rl.clear_background(Colors.raywhite)
            self.draw()
            rl.end_drawing()
        rl.close_window()

    def draw(self) -> None:
        rl.draw_text(self.window_title, 10, 10, 30, Colors.black)
        rl.draw_rectangle(100,100,525,525,Colors.gray) # border
        draw_checkerboard(rl.Color(235,235,235,255), Colors.raywhite, 18,50, 6)
        rl.draw_rectangle(10,650,1180,140,rl.Color(235,235,235,255)) # toolbox btm
        rl.draw_rectangle(650,100,500,525,rl.Color(235,235,235,255)) # toolbox right

        rl.draw_text("Colors", 660,110,30,Colors.black)
        rl.draw_text("Info", 20,660,30,Colors.black)
        rl.draw_text(f"Current Mode: {self.mode}", 20, 690, 20, Colors.black)

        # color grid
        for count, clr in enumerate(self.clr_dict.values()):
            if count in range(0,12):
                self.draw_color_ypos = 150
            if count in range(13,24):
                self.draw_color_ypos = 190
            if count in range(25,36):
                self.draw_color_ypos = 230
            if count in range(37,48):
                self.draw_color_ypos = 270
            
            if (count == 13 or count == 25 or count == 37) and self.draw_color_xpos > 620:
                self.draw_color_xpos = 660
            elif self.draw_color_xpos > 620 and count == 0:
                self.draw_color_xpos = 620
            else:
                self.draw_color_xpos += 40
            rl.draw_rectangle(self.draw_color_xpos,self.draw_color_ypos,40,40,clr)
        if self.mode == self.modes[0]:
            self.selection.draw()

    def update(self) -> None:
        if self.mode == self.modes[0]:
            self.selection.update()

if __name__ == "__main__":
    Game()
