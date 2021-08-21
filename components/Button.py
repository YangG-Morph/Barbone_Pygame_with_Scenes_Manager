import pygame as pg
from components.Text import Text
from components.Helper import Helper
from components.CONSTANTS import *


class Button:
    def __init__(self,
                 text: str = "",
                 size: tuple = (100, 50),
                 position: tuple = (0, 0),
                 bg_color: pg.Color = pg.Color("black"),
                 fg_color: pg.Color = pg.Color("white"),
                 center_x: bool = False,
                 center_y: bool = False,
                 ):
        self.text = text
        self.rendered_text = None
        self.surface = pg.Surface(size)
        self.size = size
        self.x, self.y = position
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.center_x = center_x
        self.center_y = center_y
        self.rect = None
        self.hovered = False
        self.update()

    def update(self):
        if self.center_x:
            self.x = GAME_SIZE[0] / 2 - self.size[0] / 2
        if self.center_y:
            self.y = GAME_SIZE[1] / 2 - self.size[1] / 2
        self.rect = pg.Rect((self.x, self.y), self.size)
        self.surface.fill(self.bg_color)
        self.rendered_text = Text(text=self.text, color=self.fg_color).rendered_text

    def draw(self, screen):
        Helper.draw_centered(self.surface, self.rendered_text)
        screen.blit(self.surface, (self.x, self.y))
        if self.hovered:
            hovered_rect = pg.Rect((self.x, self.y), self.surface.get_size())
            pg.draw.rect(screen, pg.Color("white"), hovered_rect, 5)

    def clicked(self):
        pass

    def change_text(self, text):
        self.text = text
        self.update()

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]
