"""
Main Game Launcher
"""

import pyray as rl
from raylib import KEY_LEFT, KEY_RIGHT, KEY_DOWN, KEY_UP, KEY_W, KEY_A, KEY_S, KEY_D

class Game(): 
    def __init__(self) -> None:
        self.screen_width, self.screen_height = 1200, 800

        self.mode = 1
        self.available_modes = [
            "play",
            "pan",
            "select"
        ]

        rl.init_window(self.screen_width, self.screen_height,"pyplanetx")

        self.camera: rl.Camera2D = rl.Camera2D(
                rl.Vector2(0,0), 
                rl.Vector2(-500,-300), 
                0.0, 
                1.0,
        )

        self.camera_pan_queue: list[int] = []

        while not rl.window_should_close():
            rl.begin_drawing()
            rl.begin_mode_2d(self.camera)
            rl.clear_background(rl.Color(245,245,245,255))
            self._2dcam()
            rl.end_mode_2d()
            self._draw()
            self._update(rl.get_frame_time())
            rl.draw_text("camera target: {} {}".format(str(round(self.camera.target.x,2)), str(round(self.camera.target.y,2))) ,20, 660, 20, rl.Color(0,0,0,255))
            rl.draw_text(f"player coordinate: ", 20, 685, 20, rl.Color(0,0,0,255))
            rl.draw_text(f"mode: {self.available_modes[self.mode]}", 20, 710, 20,rl.Color(0,0,0,225))
            rl.end_drawing()
        rl.close_window()
   
    def _draw_checkerboard(self, base_color: rl.Color, alt_color: rl.Color, begin: int, to: int, tilesize: int):
        is_alt_color: bool = True
        for y in range(begin*tilesize, to*tilesize, tilesize):
            for x in range(begin*tilesize, to*tilesize, tilesize):
                if is_alt_color:
                    rl.draw_rectangle(x,y,tilesize,tilesize, alt_color)
                    is_alt_color = not is_alt_color
                else:
                    rl.draw_rectangle(x,y,tilesize,tilesize, base_color)
                    is_alt_color = not is_alt_color
            is_alt_color = not is_alt_color

    def _draw(self):
        rl.draw_fps(20,20)
        rl.draw_rectangle(0, self.screen_height-150, self.screen_width, 150, rl.Color(245,245,245,255))
        rl.draw_rectangle(self.screen_width-150, 0, 150, self.screen_height, rl.Color(245,245,245,255))
        

    def _2dcam(self):
        self._draw_checkerboard(rl.Color(225,225,225,255),rl.Color(205,205,205,205), -50, 50,50)
        rl.draw_rectangle(0,0,50,50, rl.Color(5,5,5,255))

    def _movement(self, dt) -> None:
        if self.available_modes[self.mode] == "pan":
            try:
                if self.camera_pan_queue[0] == KEY_A:
                    self.camera.target.x -= 350 * dt
                    self.camera_pan_queue = self.camera_pan_queue[1:]
                if self.camera_pan_queue[0] == KEY_D:
                    self.camera.target.x += 350 * dt
                    self.camera_pan_queue = self.camera_pan_queue[1:]
                if self.camera_pan_queue[0] == KEY_W:
                    self.camera.target.y -= 350 * dt
                    self.camera_pan_queue = self.camera_pan_queue[1:]
                if self.camera_pan_queue[0] == KEY_S:
                    self.camera.target.y += 350 * dt
                    self.camera_pan_queue = self.camera_pan_queue[1:]
            except IndexError:
                pass

            if rl.is_key_down(KEY_A):
                self.camera_pan_queue.append(KEY_A)
            if rl.is_key_down(KEY_D):
                self.camera_pan_queue.append(KEY_D)
            if rl.is_key_down(KEY_W):
                self.camera_pan_queue.append(KEY_W)
            if rl.is_key_down(KEY_S):
                self.camera_pan_queue.append(KEY_S)
        
    def _update(self, dt: float) -> None:
        self._movement(dt) 
