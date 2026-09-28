from pico2d import *
import math

#캐릭터 출력 및 캔버스
open_canvas(800, 600)
character = load_image('character.png')

def new_func(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_top():
    for y in range(300, 500, 5):
        new_func(600 ,y)
    

def draw_left():
    for x in range(600, 200, -5):
        new_func(x ,500)
    pass    

def draw_bottom():
    for y in range(500, 100, -5):
        new_func(200 ,y)
    pass

def draw_right():
    for x in range(200, 600, 5):
        new_func(x, 100)

def move_1():
    pass

def move_2():
    pass

def move_3():
    pass
    
def move_circle():
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    for degree in range(360):
        theta = math.radians(degree)
        x= 400 + 200 * math.cos(theta)
        y= 300 + 200 * math.sin(theta)
        new_func(x,y)
    pass

def move_rectangle():
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()
    pass

def move_triangle():
    move_1()
    move_2()
    move_3()
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()

    pass


