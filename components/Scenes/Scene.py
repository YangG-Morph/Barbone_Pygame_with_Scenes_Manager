import random
import sys
import pygame as pg

from components.Text import Text

class Scene:
    def __init__(self, game):
        self.game = game
        self.text = Text(text=str(self.__class__.__name__))
        self.rand_color = random.SystemRandom().sample(range(0, 180), 3)

    def draw_background(self):
        self.game.screen.fill(pg.Color(self.rand_color))

    def draw_foreground(self):
        self.text.draw(self.game.screen)

    def handle_exit(self, event):
        if event.type in [pg.QUIT] or event.type in [pg.KEYDOWN] and event.key in [pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def handle_keys(self, event):
        pass

    def handle_mouse(self, event):
        pass

    def scene_enter(self):
        self.rand_color = random.SystemRandom().sample(range(0, 180), 3)

    def scene_exit(self):
        pass

