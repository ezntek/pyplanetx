import pyray as rl
from raylib import KEY_LEFT, KEY_RIGHT
from colors import Colors, get_color_dict

if __name__ == "__main__":
    rl.init_window(800,100,"color demo")
    rl.set_target_fps(60)
    
    colors = get_color_dict() 

    camera = rl.Camera2D(
        rl.Vector2(0,0),
        rl.Vector2(0,0),
        0,1
    )
    
    while not rl.window_should_close():
        rl.clear_background(Colors.raywhite)
    
        if rl.is_key_down(KEY_RIGHT):
            camera.target.x += 15
        elif rl.is_key_down(KEY_LEFT):
            camera.target.x -= 15
        
        rl.begin_drawing()
        rl.begin_mode_2d(camera)
        
        for count,(key, value) in enumerate(colors.items()):
            rl.draw_text(f"{key}", (count*100)+10, 10, 10, Colors.black)
            rl.draw_rectangle((count*100)+10,30,90, 60,value)
        
        rl.end_mode_2d()
        rl.end_drawing()
