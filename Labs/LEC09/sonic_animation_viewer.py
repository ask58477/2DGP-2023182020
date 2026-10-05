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


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    running = True

    while running:
        for event in get_events():
            if event.type == SDL_QUIT or (
                event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
            ):
                running = False

        clear_canvas()
        update_canvas()
        delay(0.01)

    close_canvas()


if __name__ == '__main__':
    main()