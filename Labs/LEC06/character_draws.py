from pico2d import *
import math

#캐릭터 출력 및 캔버스
open_canvas(800, 600)
character = load_image('character.png')

CIRCLE_CENTER_X = 400
CIRCLE_CENTER_Y = 300
CIRCLE_RADIUS = 200

RECTANGLE_LEFT = 200
RECTANGLE_RIGHT = 600
RECTANGLE_TOP = 100
RECTANGLE_BOTTOM = 500

TRIANGLE_BOTTOM_X = 400
TRIANGLE_BOTTOM_Y = 500
TRIANGLE_LEFT_X = 200
TRIANGLE_TOP_Y = 150
TRIANGLE_RIGHT_X = 600

def new_func(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_top():
    for y in range(300, RECTANGLE_BOTTOM, 5):
        new_func(RECTANGLE_RIGHT, y)
    

def draw_left():
    for x in range(RECTANGLE_RIGHT, RECTANGLE_LEFT, -5):
        new_func(x, RECTANGLE_BOTTOM)

def draw_bottom():
    for y in range(RECTANGLE_BOTTOM, RECTANGLE_TOP, -5):
        new_func(RECTANGLE_LEFT, y)

def draw_right():
    for x in range(RECTANGLE_LEFT, RECTANGLE_RIGHT, 5):
        new_func(x, RECTANGLE_TOP)

def move_1():
    for i in range(101):
        x = TRIANGLE_BOTTOM_X - 2 * i
        y = TRIANGLE_BOTTOM_Y - 3.5 * i
        new_func(x, y)

def move_2():
    for x in range(TRIANGLE_LEFT_X, TRIANGLE_RIGHT_X + 1, 4):
        new_func(x, TRIANGLE_TOP_Y)

def move_3():
    for i in range(101):
        x = TRIANGLE_RIGHT_X - 2 * i
        y = TRIANGLE_TOP_Y + 3.5 * i
        new_func(x, y)
    
def move_circle():
    clear_canvas()
    character.draw(CIRCLE_CENTER_X, CIRCLE_CENTER_Y)
    update_canvas()
    for degree in range(360):
        theta = math.radians(degree)
        x = CIRCLE_CENTER_X + CIRCLE_RADIUS * math.cos(theta)
        y = CIRCLE_CENTER_Y + CIRCLE_RADIUS * math.sin(theta)
        new_func(x, y)

def move_rectangle():
    clear_canvas()
    character.draw(CIRCLE_CENTER_X, CIRCLE_CENTER_Y)
    update_canvas()
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()

def move_triangle():
    move_1()
    move_2()
    move_3()

while True:
    move_circle()
    move_rectangle()
    move_triangle()



