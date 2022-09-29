import pygame
from pygame.locals import *


from colors import *
from level import Level, GROUND_Y


WIN_SIZE = 480, 640


class Game:

    def __init__(self):
        pygame.display.set_caption("Stick Hero [PyGame]")
        self.surface = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.level = Level()

        self.pole_creation_speed = 500

        self.lmb_pressed = False
        self.lmb_time = 0  # in seconds

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick()
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        self.lmb_pressed = True
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        self.lmb_pressed = False
                        self.level.create_pole(self.lmb_time * self.pole_creation_speed)
                        self.lmb_time = 0

            # updates
            if self.lmb_pressed:
                self.lmb_time += frame_time_s
            # print(self.lmb_time)
            self.level.update(frame_time_s)

            # drawings
            self.surface.fill(BG_COLOR)
            self.level.draw(self.surface)
            if self.lmb_pressed:
                pygame.draw.rect(self.surface,
                                 POLE_COLOR,
                                 (90,
                                  self.surface.get_height() - (self.surface.get_height() - GROUND_Y) - self.lmb_time * self.pole_creation_speed + 1,
                                  8,
                                  self.lmb_time * self.pole_creation_speed),
                                 )
            pygame.display.update()

    def terminate(self):
        self.is_running = False


if __name__ == '__main__':
    Game().run()
