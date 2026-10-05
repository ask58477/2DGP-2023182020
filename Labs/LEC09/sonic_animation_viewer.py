from pathlib import Path

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SPRITE_SCALE = 6
SPRITE_HEIGHT = 525
SPRITE_PATH = Path(__file__).with_name('sonic-sprite.png')
Frame = tuple[int, int, int, int]
Animation = tuple[str, tuple[Frame, ...]]

ANIMATIONS: tuple[Animation, ...] = (
    (
        '동작 01',
        (
            (1, 39, 29, 39),
            (31, 40, 26, 38),
            (58, 39, 28, 39),
            (86, 40, 30, 38),
            (118, 40, 30, 38),
            (150, 40, 30, 38),
            (182, 40, 29, 38),
            (211, 39, 29, 38),
            (240, 39, 29, 38),
            (270, 45, 24, 32),
            (302, 51, 29, 26),
        ),
    ),
)


def load_sprite():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f'스프라이트 파일을 찾을 수 없습니다: {SPRITE_PATH}')

    return load_image(str(SPRITE_PATH))


def draw_frame(sprite, frame: Frame):
    source_x, source_y, source_width, source_height = frame
    pico2d_y = SPRITE_HEIGHT - source_y - source_height
    sprite.clip_draw(
        source_x,
        pico2d_y,
        source_width,
        source_height,
        CANVAS_WIDTH // 2,
        CANVAS_HEIGHT // 2,
        source_width * SPRITE_SCALE,
        source_height * SPRITE_SCALE,
    )


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_sprite()
        frame = ANIMATIONS[0][1][0]
        running = True

        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False

            clear_canvas()
            draw_frame(sprite, frame)
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()