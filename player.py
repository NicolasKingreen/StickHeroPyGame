import pygame
from pygame.math import Vector2

from colors import PLAYER_COLOR

class Player:
    def __init__(self):
        self.pos = Vector2(50, 400)

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR,
                         (self.pos, (32, 48)))
