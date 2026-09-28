from pico2d import *
import math


open_canvas(800, 600)
character = load_image('character.png')


def move_circle():
	for degree in range(360):
		theta = math.radians(degree)
		x = 400 + 200 * math.cos(theta)
		y = 300 + 200 * math.sin(theta)
		clear_canvas()
		character.draw(x, y)
		update_canvas()
		delay(0.01)


def move_rectangle_top():
	for x in range(200, 601, 5):
		clear_canvas()
		character.draw(x, 150)
		update_canvas()
		delay(0.01)


def move_rectangle_left():
	for y in range(150, 451, 5):
		clear_canvas()
		character.draw(600, y)
		update_canvas()
		delay(0.01)


def move_rectangle_bottom():
	for x in range(600, 199, -5):
		clear_canvas()
		character.draw(x, 450)
		update_canvas()
		delay(0.01)


def move_rectangle_right():
	for y in range(450, 149, -5):
		clear_canvas()
		character.draw(200, y)
		update_canvas()
		delay(0.01)


def move_rectangle():
	move_rectangle_top()
	move_rectangle_left()
	move_rectangle_bottom()
	move_rectangle_right()


def move_triangle_first():
	for step in range(101):
		x = 400 - 2 * step
		y = 500 - 3.5 * step
		clear_canvas()
		character.draw(x, y)
		update_canvas()
		delay(0.01)


def move_triangle_second():
	for step in range(101):
		x = 200 + 4 * step
		y = 150
		clear_canvas()
		character.draw(x, y)
		update_canvas()
		delay(0.01)


def move_triangle_third():
	for step in range(101):
		x = 600 - 2 * step
		y = 150 + 3.5 * step
		clear_canvas()
		character.draw(x, y)
		update_canvas()
		delay(0.01)


def move_triangle():
	move_triangle_first()
	move_triangle_second()
	move_triangle_third()


while True:
	move_circle()
	move_rectangle()
	move_triangle()
