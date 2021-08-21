from components.Actors.Entity import Entity
from components.Scenes.SceneManager import SceneManager
from components.CONSTANTS import *


pg.init()

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.running = True
        self.scene_manager = SceneManager(self)

    def run(self):
        while self.running:
            self.scene_manager.draw_background()
            self.scene_manager.draw_foreground()
            self.scene_manager.handle_events()

            self.clock.tick(FPS)
            pg.display.update()

if __name__ == '__main__':
    display = pg.display.set_mode(GAME_SIZE, flags=0)
    pg.display.set_caption(GAME_NAME)

    Game(display).run()





























