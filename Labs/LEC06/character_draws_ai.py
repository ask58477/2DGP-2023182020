import math
import os

from pico2d import *


open_canvas(800, 600)
character = load_image(os.path.join(os.path.dirname(__file__), 'character.png'))


def follow_path(points):
	for segment_index, start in enumerate(points):
		end = points[(segment_index + 1) % len(points)]
		start_x, start_y = start
		end_x, end_y = end
		steps = max(1, int(math.hypot(end_x - start_x, end_y - start_y) / 4))

		for step in range(steps + 1):
			ratio = step / steps
			x = start_x + (end_x - start_x) * ratio
			y = start_y + (end_y - start_y) * ratio
			clear_canvas()
			character.draw(x, y)
			update_canvas()
			delay(0.01)


def move_circle():
	points = [
		(400 + 200 * math.cos(math.radians(degree)),
		 300 + 200 * math.sin(math.radians(degree)))
		for degree in range(360)
	]
	follow_path(points)


def move_rectangle():
	follow_path([(200, 150), (600, 150), (600, 450), (200, 450)])


def move_triangle():
	follow_path([(400, 120), (630, 480), (170, 480)])


while True:
	move_circle()
	move_rectangle()
	move_triangle()
