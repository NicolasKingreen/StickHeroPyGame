import pygame

from math import cos, sin, radians

from colors import POLE_COLOR


class Pole:

    def __init__(self, height):
        self.height = height
        self.x0 = 90 + 4
        self.x1 = 90 + 4
        self.y1 = 640 - 400 - 48 - height

        self.is_falling = True

        self.can_move = False
        self.speed = 200

        self.angle = 90  # start angle
        self.angle_speed = 120  # deg per sec

    def update(self, frame_time_s):
        if self.is_falling:
            self.angle -= frame_time_s * self.angle_speed
            self.x1 = self.x0 + self.height * cos(radians(self.angle))
            self.y1 = (640 - (640 - 448)) - self.height * sin(radians(self.angle))
            print(self.angle, self.x1, self.y1)
        if self.angle <= 0:
            self.is_falling = False
            self.angle = 0
        if self.can_move:
            self.x0 -= self.speed * frame_time_s
            self.x1 -= self.speed * frame_time_s

    def start_moving(self):
        self.can_move = True

    def draw(self, surface):
        pygame.draw.line(surface, POLE_COLOR,
                         (self.x0, 400 + 48),
                         (self.x1, self.y1),
                         8)

