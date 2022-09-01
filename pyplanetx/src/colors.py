from pyray import Color
class Colors:
    nothing             = Color(255,255,255,0)

    # grayscale colors
    
    black               = Color(0,0,0,255)
    dark_gray           = Color(55,55,55,255)
    gray                = Color(105,105,105,255)
    light_gray          = Color(185,185,185,255)
    raywhite            = Color(245,245,245,255)

    # reds

    brick_red           = Color(160,0,0,255)
    pure_red            = Color(255,0,0,255)
    red                 = Color(255,25,25,255)
    light_red           = Color(255,155,155,255)

    # pinks and magentas
    
    hibiscus            = Color(255,50,155,255)
    rlpink              = Color(255,109,194,255)
    pink                = Color(255,140,175,255)
    rlmagenta           = Color(255,0,255,255)

    # oranges
    
    electric_orange     = Color(255,64,0,255)
    orange              = Color(255,128,0,255)
    light_orange        = Color(255,165,75,255)

    # yellows
    
    blinding_yellow     = Color(255,255,0,255)
    yellow              = Color(255,224,0,255)
    canary_yellow       = Color(255,255,102,255)

    # greens

    musty_green         = Color(153,204,0,255)
    light_lime          = Color(195,255,0,255)
    lime                = Color(175, 225, 0, 255)
    grass_green         = Color(115,235,0,255)
    deep_green          = Color(0,230,0,255)
    dark_green          = Color(0,175,0,255)
    sage                = Color(100,155,155,255)

    # cyans, turquoises
    green_turquoise     = Color(0,255,128,255)
    mint                = Color(100,255,180,255)
    grnish_turquoise    = Color(26,255,201,255)
    light_grn_turquoise = Color(155,255,225,255)
    turquoise           = Color(0,255,215,255)
    light_turquoise     = Color(150,255,235,255) 
    aqua                = Color(0,255,217,255)
    light_sky           = Color(150,255,255,255)

    # blues

    blueberry           = Color(79,134,247,255)
    deep_sky            = Color(0,190,255,255)
    light_blue          = Color(100,215,255,255)
    blue                = Color(0,128,255,255)
    dark_blue           = Color(0,102,204,255)
    google_blue         = Color(0,0,255,255)

    # purples, violets, etc

    maroon              = Color(153,51,102,255)
    dark_maroon         = Color(100,0,100,255)
    purple              = Color(121,77,255,255)
    violet              = Color(128,0,255,255)
    lavendar            = Color(190,125,255,255)
    shit                = Color(128,64,0,255)
    dirt                = Color(180,90,0,255)

def get_color_dict() -> dict[str,Color]:
    return {key:value for key, value in Colors.__dict__.items() if not key.startswith('__') and not callable(key)}
