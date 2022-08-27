import pyray as rl

def _draw():
    rl.clear_background([245,245,245,255])

def _update(dt: float):
    pass

def launch() -> int:
    rl.init_window(800,600,"pyplanetx")
    rl.set_target_fps(60)

    while not rl.window_should_close():
        rl.begin_drawing()
        _draw()
        _update(rl.get_frame_time())
        rl.end_drawing()
