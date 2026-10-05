from pathlib import Path
from dataclasses import dataclass
import time

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
FRAME_INTERVAL = 0.08
ANIMATION_REPEATS = 5
ANIMATION_PAUSE = 1.0
EVENT_POLL_INTERVAL = 0.01
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
    (
        '동작 02',
        (
            (8, 80, 26, 37),
            (37, 80, 27, 37),
            (65, 80, 31, 38),
            (97, 80, 37, 37),
            (135, 80, 32, 35),
            (170, 79, 32, 38),
            (206, 79, 26, 38),
            (238, 80, 24, 37),
            (263, 80, 30, 37),
            (295, 80, 36, 37),
            (334, 80, 32, 36),
            (370, 79, 29, 38),
        ),
    ),
    (
        '동작 03',
        (
            (1, 124, 33, 40),
            (39, 124, 35, 39),
            (89, 125, 35, 38),
            (130, 121, 34, 42),
            (181, 122, 34, 41),
            (228, 122, 33, 40),
        ),
    ),
    (
        '동작 04',
        (
            (1, 169, 29, 30),
            (35, 167, 29, 31),
            (67, 169, 30, 29),
            (98, 169, 31, 29),
            (131, 168, 29, 30),
            (162, 168, 29, 31),
            (193, 170, 30, 29),
            (230, 170, 31, 29),
            (268, 170, 30, 30),
        ),
    ),
    (
        '동작 05',
        (
            (1, 206, 30, 27),
            (36, 206, 29, 27),
            (70, 206, 29, 27),
            (105, 206, 29, 27),
            (139, 206, 29, 27),
            (174, 206, 29, 27),
        ),
    ),
    (
        '동작 06',
        (
            (1, 239, 29, 35),
            (36, 239, 30, 35),
            (74, 239, 31, 35),
            (111, 238, 31, 36),
            (149, 239, 30, 35),
            (186, 238, 31, 36),
        ),
    ),
    (
        '동작 07',
        (
            (1, 283, 29, 35),
            (36, 283, 30, 35),
            (72, 286, 39, 31),
            (123, 285, 39, 32),
            (172, 286, 39, 31),
            (218, 285, 38, 32),
        ),
    ),
    (
        '동작 08',
        (
            (1, 326, 24, 45),
            (31, 327, 29, 44),
            (65, 327, 20, 44),
            (90, 327, 25, 43),
            (119, 327, 25, 43),
            (149, 327, 20, 44),
        ),
    ),
    (
        '동작 09',
        (
            (184, 341, 40, 28),
            (232, 341, 39, 27),
        ),
    ),
    (
        '동작 10',
        (
            (1, 379, 27, 38),
            (31, 379, 31, 36),
            (64, 379, 31, 36),
            (99, 377, 33, 38),
            (136, 379, 32, 36),
            (176, 379, 33, 36),
            (217, 379, 33, 36),
            (254, 378, 33, 36),
        ),
    ),
    (
        '동작 11',
        (
            (6, 429, 34, 40),
            (49, 426, 34, 43),
            (96, 427, 23, 39),
            (125, 427, 23, 39),
        ),
    ),
)


@dataclass
class PlaybackState:
    animation_index: int = 0
    frame_index: int = 0
    repetitions: int = 0
    next_frame_at: float = 0.0
    pause_until: float | None = None


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


def advance_playback(state: PlaybackState, now: float):
    if state.pause_until is not None:
        return
    if now < state.next_frame_at:
        return

    frames = ANIMATIONS[state.animation_index][1]
    state.frame_index += 1
    if state.frame_index == len(frames):
        state.frame_index = 0
        state.repetitions += 1
        if state.repetitions == ANIMATION_REPEATS:
            state.frame_index = len(frames) - 1
            state.pause_until = now + ANIMATION_PAUSE
            return
    state.next_frame_at = now + FRAME_INTERVAL


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_sprite()
        state = PlaybackState(next_frame_at=time.monotonic())
        running = True

        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False

            advance_playback(state, time.monotonic())
            frame = ANIMATIONS[state.animation_index][1][state.frame_index]
            clear_canvas()
            draw_frame(sprite, frame)
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()