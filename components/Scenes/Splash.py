import pygame as pg
from components.Scenes.Scene import Scene
from components.Actors.Moon import Moon
from components.Text import Text
from assets.paths import load_images, MOON_DIR

class Splash(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.text.change_text("Made with Pygame")
        self.text.center_x, self.text.center_y = True, True
        font = pg.font.SysFont("Calibri", 45)
        font.set_underline(True)
        self.text_continue = Text(text="Press any key to continue", position=(0, 500), center_x=True, font=font)
        self.moon = Moon(name="Moon", position=(0, 150), center_x=True, images=load_images(MOON_DIR, scale=3), fps=24)

    def draw_background(self):
        super().draw_background()
        self.moon.draw(self.game.screen)

    def draw_foreground(self):
        super().draw_foreground()
        self.text_continue.draw(self.game.screen)

    def handle_keys(self, event):
        super().handle_keys(event)
        if event.type in [pg.KEYDOWN]:
            if event.key not in[pg.QUIT, pg.K_ESCAPE]:
                self.game.scene_manager.next_scene()
        if event.type in [pg.MOUSEBUTTONDOWN]:
            self.game.scene_manager.next_scene()
            if event.button == 1: # important, dis-allow button clicking through scenes
                event.button = 0

    def handle_mouse(self, event):
        super().handle_mouse(event)

    def scene_enter(self):
        super().scene_enter()

    def scene_exit(self):
        super().scene_exit()
