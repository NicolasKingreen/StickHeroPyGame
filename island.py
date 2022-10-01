import pygame
from pygame import Rect
from colors import GROUND_COLOR


class Island:
    def __init__(self, x0, width):
        self.rect = Rect(x0, 448, width, 640 - 448)

        self.can_move = False
        self.speed = 0

    def update(self, frame_time_s):
        if self.can_move:
            self.rect.x -= self.speed * frame_time_s

    def start_moving(self):
        self.can_move = True
        self.speed = self.rect.x

    def draw(self, surface):
        pygame.draw.rect(surface, GROUND_COLOR, self.rect)
