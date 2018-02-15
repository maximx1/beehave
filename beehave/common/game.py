import pygame, sys
from beehave.common.constants import Colors
from beehave.display.camera import Camera

class BeehaveGame:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window_d = (800, 600)
        self.screen = pygame.display.set_mode(self.window_d)
        self.clock = pygame.time.Clock()
        #self.camera = Camera(self.window_d[0], self.window_d[1], 1800, 1400)

    def play(self):
        done = False
        while not done:
            game_time = self.clock.tick(60)
            self.screen.fill(Colors.WHITE)

            pygame.display.flip()
        pygane.quit()
