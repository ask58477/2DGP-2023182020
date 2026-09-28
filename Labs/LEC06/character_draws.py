from pico2d import *
import math

#캐릭터 출력 및 캔버스
open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    for degree in range(360):
        theta = math.radians(degree)
        x= 400 + 200 * math.cos(theta)
        y= 300 + 200 * math.sin(theta)
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)
    pass

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()

    pass


