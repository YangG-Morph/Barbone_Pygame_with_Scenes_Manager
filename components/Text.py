from components.CONSTANTS import *
from components.Helper import Helper

class Text:
    def __init__(self,
                 text="None",
                 color=pg.Color("white"),
                 position=(0, 0),
                 center_x=False,
                 center_y=False,
                 font=CALIBRI):
        self.text = text
        self.rendered_text = None
        self.color = color
        self.x, self.y = position
        self.center_x = center_x
        self.center_y = center_y
        self.size = (0, 0)
        self.font = font
        self.update()

    def update(self):
        self.size = self.font.size(self.text)
        if self.center_x:
            self.x = GAME_SIZE[0] / 2 - self.size[0] / 2
        if self.center_y:
            self.y = GAME_SIZE[1] / 2 - self.size[1] / 2
        self.rendered_text = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        if self.center_x and self.center_y:
            Helper.draw_centered(screen, self.rendered_text)
        else:
            screen.blit(self.rendered_text, (self.x, self.y))

    def change_text(self, text):
        self.text = text
        self.update()

    def get_width(self):
        return self.rendered_text.get_width()

    def get_height(self):
        return self.rendered_text.get_height()