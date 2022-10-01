import pygame
from pygame.math import Vector2

from colors import PLAYER_COLOR


class Player:
    def __init__(self):
        self.pos = Vector2(50, 400)
        self.can_move = False
        self.speed = 300

    def update(self, frame_time_s):
        if self.can_move:
            self.pos.x += self.speed * frame_time_s

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR,
                         (self.pos, (32, 48)))
