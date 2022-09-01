import pyray as rl
from colors import Colors
from colors import get_color_dict
from raylib import KEY_C, KEY_E, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

class ColoredRect():
    def __init__(self, name_str: str, posx: float, posy: float, width: float, height: float, color: rl.Color) -> None:
        self.rect = rl.Rectangle(posx,posy,width,height)
        self.clr = color
        self.name_as_str: str = name_str

    def draw(self):
        rl.draw_rectangle_rec(self.rect, self.clr)

class Selection():
    def __init__(self, pos: rl.Vector2, width:int, thickness:int) -> None:
        self.selection_clr = rl.Color(200,200,200,255)
        self.timer = 0
        self.pos = pos
        self.width = width
        self.thickness = thickness

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
        self.rect_above.x, self.rect_above.y, self.rect_above.width, self.rect_above.height = self.pos.x-self.thickness, self.pos.y-self.thickness, self.width+(self.thickness*2), self.thickness
        self.rect_below.x, self.rect_below.y, self.rect_below.width, self.rect_below.height = self.pos.x-self.thickness, self.pos.y+self.width, self.width+(self.thickness*2), self.thickness
        self.rect_left.x, self.rect_left.y, self.rect_left.width, self.rect_left.height = self.pos.x-self.thickness, self.pos.y-self.thickness, self.thickness, self.width+(self.thickness*2)
        self.rect_right.x, self.rect_right.y, self.rect_right.width, self.rect_right.height = self.pos.x+self.width, self.pos.y-self.thickness, self.thickness, self.width+(self.thickness*2)
        

        self.timer += 1

        if self.timer % 20 == 0:
            self.selection_clr.a = 255
        elif self.timer % 20 == 10:
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

class Main():
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

        self.selection_index = rl.Vector2(0,0)
        self.color_grid = [
            [ColoredRect(key,660+(count*40),150,40,40,value) 
                for count, (key, value) in enumerate(self.clr_dict.items())
                    if count in range(0,11)],
            [ColoredRect(key,180+(count*40),190,40,40,value) 
                for count, (key, value) in enumerate(self.clr_dict.items())
                    if count in range(12,23)],
            [ColoredRect(key,-300+(count*40),230,40,40,value) 
                for count, (key, value) in enumerate(self.clr_dict.items())
                    if count in range(24,35)],
            [ColoredRect(key,-780+(count*40),270,40,40,value) 
                for count, (key, value) in enumerate(self.clr_dict.items())
                    if count in range(36,48) and value != Colors.nothing],
        ]

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
        if self.mode == self.modes[0]:
            rl.draw_text(f"Selected Color: {self.color_grid[int(self.selection_index.y)][int(self.selection_index.x)].name_as_str}", 20, 710, 20, Colors.black)

        # color grid
        for column in self.color_grid:
            for clr_rect in column:
                clr_rect.draw()
        # selection
        if self.mode == self.modes[0]:
            self.selection.draw()

    def update(self) -> None:        
        if rl.is_key_pressed(KEY_E):
            self.mode = "edit"
        if rl.is_key_pressed(KEY_C):
            self.mode = "color picker"
        if self.mode == self.modes[0]:
            self.selection.update()
            self.selection.pos.x, self.selection.pos.y = self.color_grid[int(self.selection_index.y)][int(self.selection_index.x)].rect.x, self.color_grid[int(self.selection_index.y)][int(self.selection_index.x)].rect.y

            if rl.is_key_pressed(KEY_UP):
                if self.selection_index.y - 1 >= 0:
                    self.selection_index.y -= 1
            if rl.is_key_pressed(KEY_DOWN):
                if self.selection_index.y + 1 < 4:
                    self.selection_index.y += 1

            if rl.is_key_pressed(KEY_LEFT):
                if self.selection_index.x - 1 >=0:
                    self.selection_index.x -= 1
            if rl.is_key_pressed(KEY_RIGHT):
                if self.selection_index.x + 1 < 11:
                    self.selection_index.x += 1

if __name__ == "__main__":
    Main()
