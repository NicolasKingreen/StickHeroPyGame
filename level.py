import pygame

from random import randint

from colors import *
from player import Player
from pole import Pole


GROUND_Y = 400 + 48
PLAYER_GROUND_WIDTH = 120

MIN_DIST, MAX_DIST = 100, 200
MIN_WIDTH, MAX_WIDTH = 50, 200
PERFECT_WIDTH = 8
PERFECT_HEIGHT = 4


class Level:
    def __init__(self):
        self.player = Player()
        self.pole = None

        self.next_ground_distance = randint(MIN_DIST, MAX_DIST)
        self.next_ground_width = randint(MIN_WIDTH, MAX_WIDTH)
        self.perfect_range = PLAYER_GROUND_WIDTH + self.next_ground_distance + (self.next_ground_width - PERFECT_WIDTH) // 2,\
                             PLAYER_GROUND_WIDTH + self.next_ground_distance + (self.next_ground_width + PERFECT_WIDTH) // 2

        self.hit_ground = False

    def update(self, frame_time_s):
        if self.pole:
            self.pole.update(frame_time_s)

    def draw(self, surface):
        surf_size = surface.get_size()

        # player ground
        pygame.draw.rect(surface,
                         GROUND_COLOR,
                         (0, GROUND_Y, PLAYER_GROUND_WIDTH,
                          surf_size[1] - GROUND_Y))

        # nearest ground
        pygame.draw.rect(surface,
                         GROUND_COLOR,
                         (PLAYER_GROUND_WIDTH + self.next_ground_distance,
                          GROUND_Y,
                          self.next_ground_width,
                          surf_size[1] - GROUND_Y))

        # perfect range
        pygame.draw.rect(surface, PERFECT_COLOR,
                         (self.perfect_range[0], GROUND_Y,
                          PERFECT_WIDTH, PERFECT_HEIGHT))

        self.player.draw(surface)
        if self.pole:
            self.pole.draw(surface)
            if not self.pole.is_falling:
                # check if hit ground
                # ...

                if self.perfect_range[0] <= self.pole.x1 <= self.perfect_range[1]:
                    print("PERFECT!!! +1")

    def create_pole(self, height):
        self.pole = Pole(height)

