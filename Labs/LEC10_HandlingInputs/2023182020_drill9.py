from pico2d import *




TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('animation_sheet.png')
CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 100
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

def handle_events():
    pass


def update_position():
    global character_x, character_y

    half_width = CHARACTER_WIDTH // 2
    half_height = CHARACTER_HEIGHT // 2
    character_x = max(half_width, min(character_x, TUK_WIDTH - half_width))
    character_y = max(half_height, min(character_y, TUK_HEIGHT - half_height))


def update_animation():
    pass


def draw():
    pass


def main():
    pass

