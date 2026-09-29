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
    frames = [
        (5, 677, 27, 20),
        (38, 676, 24, 22),
        (68, 676, 23, 23),
        (97, 676, 23, 23),
        (126, 677, 24, 21),
        (156, 676, 23, 23),
        (185, 676, 23, 22),
        (214, 676, 25, 22),
        (251, 677, 24, 21),
        (281, 677, 9, 26),
        (296, 677, 24, 13)
    ]

    frame = 0

    for x in range(600, 400, -5):
        clear_canvas()

        fx, fy, fw, fh = frames[frame]

        character.clip_composite_draw(
            fx, fy, fw, fh,
            0, 'h',
            x, 300, 50, 50
        )

        update_canvas()

        frame = (frame + 1) % len(frames)
        delay(0.05)

def three():
    frames = [
        (5, 740, 23, 22),
        (34, 740, 24, 22),
        (63, 740, 21, 27),
        (90, 741, 19, 24),
        (115, 740, 21, 21),
        (142, 740, 21, 23),
        (169, 741, 23, 24),
        (197, 740, 25, 21),
        (228, 740, 20, 31),
        (255, 740, 19, 31)
    ]

    frame = 0

    for y in range(300, 401, 10):
        clear_canvas()

        fx, fy, fw, fh = frames[frame]

        character.clip_draw(
            fx, fy, fw, fh,
            400, y, 50, 50
        )

        update_canvas()

        frame = (frame + 1) % len(frames)
        delay(0.05)

    for y in range(400, 299, -10):
        clear_canvas()

        fx, fy, fw, fh = frames[frame]

        character.clip_draw(
            fx, fy, fw, fh,
            400, y, 50, 50
        )

        update_canvas()

        frame = (frame + 1) % len(frames)
        delay(0.05) 


def four():
    frames = [
        (4, 639, 24, 28),
        (34, 639, 23, 30),
        (61, 639, 25, 29),
        (89, 639, 24, 28),
        (118, 639, 25, 29)
    ]

    for frame in range(len(frames)):
        clear_canvas()

        fx, fy, fw, fh = frames[frame]

        character.clip_draw(
            fx, fy, fw, fh,
            400, 300, 50, 50
        )

        update_canvas()

        if frame == 4:
            delay(0.3)
        else:
            delay(0.05)
    pass

while True:

    for i in range(5):
        one()

    delay(1)
    for i in range(5):
        two()
    delay(1)
    for i in range(5):
        three()
    delay(1)
    for i in range(5):
        four()
    delay(1)
    pass