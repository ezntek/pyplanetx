import pyray as rl
from raylib import KEY_LEFT, KEY_RIGHT
from colors import Colors
if __name__ == "__main__":
    rl.init_window(800,100,"color demo")
    rl.set_target_fps(60)
    colors = Colors.__dict__
    camera = rl.Camera2D(
        rl.Vector2(0,0),
        rl.Vector2(0,0),
        0,1
    )
    count = 0
    while not rl.window_should_close():
        rl.clear_background(Colors.raywhite)
        if rl.is_key_pressed(KEY_RIGHT):
            camera.target.x += 15
        elif rl.is_key_pressed(KEY_LEFT):
            camera.target.x -= 15
        rl.begin_drawing()
        rl.begin_mode_2d(camera)
        for key, value in enumerate(colors.values()):
            rl.draw_text(f"{key}", (count*100)+10, 10, 20, Colors.black)
            rl.draw_rectangle((count*100)+10,30,90, 60,value)
            count += 1
        rl.end_mode_2d()
        rl.end_drawing()
