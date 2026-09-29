from pico2d import *

open_canvas()

character = load_image('cuby.png')


def one():
    frames = [
        (5, 709, 20, 20),
        (31, 709, 20, 21),
        (57, 709, 20, 21),
        (83, 709, 20, 20),
        (109, 709, 21, 19),
        (136, 709, 22, 19),
        (164, 709, 22, 20),
        (192, 709, 27, 21),
        (225, 709, 26, 21),
        (257, 709, 24, 20),
        (287, 709, 21, 19),
        (315, 709, 19, 20)
    ]

    frame = 0

    for x in range(400, 600, 5):
        clear_canvas()

        fx, fy, fw, fh = frames[frame]

        character.clip_draw(
            fx, fy, fw, fh,
            x, 300, 50, 50
        )

        update_canvas()

        frame = (frame + 1) % len(frames)
        delay(0.05)


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
    frame = 0
    for y in range(300,500,5):
            clear_canvas()
            character.clip_draw(
                frame * 29, 741, 29, 29, 400, y
            )
            update_canvas()
        
            frame =(frame + 1) % 11
            delay(0.05)
    pass

def four():
    pass

while True:
     
    one()

    two()

    three()

    four()
    pass