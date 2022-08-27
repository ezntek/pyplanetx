"""
Main Game Launcher
"""

import pyray as rl

def _draw():
    rl.clear_background(rl.Color(245,245,245,255))

def _2dcam():
    pass

def _update(dt: float):
    pass

def launch() -> int:
    screen_width, screen_height = 1200,800

    rl.init_window(screen_width, screen_height,"pyplanetx")
    rl.set_target_fps(60)

    camera: rl.Camera2D = rl.Camera2D(rl.Vector2(screen_width/2, screen_height/255), rl.Vector2(20,20), 0.0, 1.1)


    while not rl.window_should_close():
        rl.begin_drawing()
        _draw()
        rl.begin_mode_2d(camera)
        _2dcam()
        rl.end_mode_2d()
        _update(rl.get_frame_time())
        rl.end_drawing()
    rl.close_window()
    return 0

