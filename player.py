import pygame
from pygame.math import Vector2

from colors import PLAYER_COLOR


class Player:
    def __init__(self):
        self.pos = Vector2(50, 400)

        self.can_move = False
        self.speed = 300

        self.offsetting = False
        self.offset_speed = 0

    def update(self, frame_time_s):
        if self.can_move:
            self.pos.x += self.speed * frame_time_s
        if self.offsetting:
            self.pos.x -= self.offset_speed * frame_time_s
            # if self.pos.x <= 50:
            #     self.pos.x = 50
            #     self.offsetting = False

    def start_moving(self):
        self.can_move = True

    def start_offsetting(self, speed):
        self.offsetting = True
        self.offset_speed = speed
        # self.offset_speed = (self.pos.x - 50) / 0.5

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR,
                         (self.pos, (32, 48)))
