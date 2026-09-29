from pico2d import *

open_canvas()

character = load_image('cuby.png')


def one():
    frame = 0
    for x in range(400,600,5):
            clear_canvas()
            character.clip_draw(
                frame * 29, 705, 26, 26, x, 300
            )
            update_canvas()
    
            frame =(frame + 1) % 12
            delay(0.05)
    pass

def two():
    frame = 0
    for x in range(600,400,-5):
            clear_canvas()
            character.clip_composite_draw(
                frame * 29, 677, 29, 29, 0, 'h', x, 300, 50, 50
            )
            update_canvas()
        
            frame =(frame + 1) % 8
            delay(0.05)
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