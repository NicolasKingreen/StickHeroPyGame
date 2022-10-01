import pygame

from random import randint

from colors import *
from player import Player
from pole import Pole
from island import Island


GROUND_Y = 400 + 48
PLAYER_GROUND_WIDTH = 120

MIN_DIST, MAX_DIST = 100, 200
MIN_WIDTH, MAX_WIDTH = 50, 200
PERFECT_WIDTH = 8
PERFECT_HEIGHT = 4

GROUND_MOVE_TIME = 500  # ms


class Level:
    def __init__(self):
        self.player = Player()
        self.pole = None

        self.island0 = Island(0, PLAYER_GROUND_WIDTH)
        next_ground_distance = randint(MIN_DIST, MAX_DIST)
        next_ground_width = randint(MIN_WIDTH, MAX_WIDTH)
        self.island1 = Island(self.island0.rect.x + next_ground_distance, next_ground_width)

        self.perfect_range = PLAYER_GROUND_WIDTH + next_ground_distance + (next_ground_width - PERFECT_WIDTH) // 2,\
                             PLAYER_GROUND_WIDTH + next_ground_distance + (next_ground_width + PERFECT_WIDTH) // 2

    def update(self, frame_time_s):
        self.island0.update(frame_time_s)
        self.island1.update(frame_time_s)
        if self.pole:
            self.pole.update(frame_time_s)
            if not self.pole.is_falling:
                if not self.player.can_move and \
                        not self.island0.can_move:
                    self.player.can_move = True
                # check if hit ground
                if self.hit_ground:
                    pass
                # ...
                if self.is_perfect:
                    print("PERFECT!!! +1")
        self.player.update(frame_time_s)
        if self.player.pos.x > self.island1.rect.right - 32 \
                and self.player.can_move:
            self.player.can_move = False
            self.island0.start_moving()
            self.island1.start_moving()
            self.pole.start_moving()

    @property
    def hit_ground(self):
        return self.island1.rect.x < self.pole.x1 < self.island1.rect.x

    @property
    def is_perfect(self):
        return self.perfect_range[0] <= self.pole.x1 <= self.perfect_range[1]

    def draw(self, surface):
        surf_size = surface.get_size()

        self.island0.draw(surface)
        self.island1.draw(surface)

        # perfect range
        pygame.draw.rect(surface, PERFECT_COLOR,
                         (self.perfect_range[0], GROUND_Y,
                          PERFECT_WIDTH, PERFECT_HEIGHT))

        self.player.draw(surface)
        if self.pole:
            self.pole.draw(surface)

    def create_pole(self, height):
        self.pole = Pole(height)

