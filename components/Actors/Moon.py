from components.Actors.Entity import Entity
from components.CONSTANTS import GAME_SIZE, FPS

class Moon(Entity):
    def __init__(self,
                 name: str = "No Name",
                 position: tuple = (0,0),
                 center_x: bool = False,
                 center_y: bool = False,
                 images=None,
                 fps=FPS,
                 ):
        super().__init__(name, position, center_x, center_y, images)
        self.max_index = len(self.images) if images else 0
        self.index = self.max_index + 1
        self.count = 0
        self.fps = fps
        self.update()

    def update(self):
        if self.images:
            self.count += 1
            if self.count > self.max_index / self.fps:
                self.index += 1
                self.count = 0

            if self.index >= len(self.images) + 1:
                self.index = 1

            self.current_image = self.images.get(str(self.index))
            self.size = self.current_image.get_size()
            if self.center_x:
                self.x = GAME_SIZE[0] / 2 - self.size[0] / 2
            if self.center_y:
                self.y = GAME_SIZE[1] / 2 - self.size[1] / 2

    def draw(self, screen):
        if self.images:
            screen.blit(self.current_image, (self.x, self.y))
            self.update()