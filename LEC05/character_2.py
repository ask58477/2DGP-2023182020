from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

x, y= 400,300
angle=0
radius=200
while True:
    clear_canvas()
    x = 400 + radius * math.cos(angle)
    y = 300 + radius * math.sin(angle)
    character.draw(x, y)
    update_canvas()
    angle+=0.05
    delay(0.01)


   

close_canvas()
