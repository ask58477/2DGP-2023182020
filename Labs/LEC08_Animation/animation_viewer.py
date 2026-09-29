from pico2d import *

open_canvas()

character = load_image('cuby.png')


def one():
    frame = 0
    for x in range(0,800,5):
            clear_canvas()
            character.clip_draw(
                frame * 29 + 2, 705, 26, 26, x, 90
            )
            update_canvas()
    
            frame =(frame + 1) % 12
            delay(0.05)
    pass

def two():
    pass

def three():
    pass

def four():
    pass

while True:
     
    one()

    two()

    three()

    four()
    pass