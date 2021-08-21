import pygame as pg
from components.CONSTANTS import GAME_SIZE, FPS

class Entity(pg.sprite.Sprite):
    def __init__(self,
                 name: str = "No Name",
                 position: tuple = (0,0),
                 center_x: bool = False,
                 center_y: bool = False,
                 images=None,
                 fps=FPS,
                 ):
        super().__init__()
        self.name = name
        self.x, self.y = position
        self.rect = None
        self.center_x = center_x
        self.center_y = center_y
        self.images = images
        self.max_index = len(self.images) if images else 0
        self.index = self.max_index
        self.size = (0, 0)
        self.current_image = None
        self.count = 0
        self.fps = fps
        self.update()

    def update(self):
        if self.images:
            self.count += 1
            if self.count > self.max_index / self.fps:
                self.index += 1
                self.count = 0

            if self.index >= len(self.images):
                self.index = 0

            self.current_image = self.images.get(str(self.index))
            if self.center_x:
                self.x = GAME_SIZE[0] / 2 - self.size[0] / 2
            if self.center_y:
                self.y = GAME_SIZE[1] / 2 - self.size[1] / 2

    def draw(self, screen):
        if self.images:
            screen.blit(self.images.get(str(self.index)), (self.x, self.y))
            self.update()
