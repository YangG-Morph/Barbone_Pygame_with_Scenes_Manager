import pygame as pg
from components.Scenes.Scene import Scene
from components.Button import Button

class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.play_button = Button("Play", (150,90), (0, 150), center_x=True)
        self.settings_button = Button("Settings", (250, 90), (0, 250), center_x=True)
        self.quit_button = Button("Quit", (150, 90), (0, 350), center_x=True)
        self.play_button.clicked = lambda: self.game.scene_manager.next_scene()
        self.settings_button.clicked = lambda: self.game.scene_manager.next_scene("Settings")
        self.quit_button.clicked = lambda: self.handle_exit(pg.event.Event(pg.QUIT))
        self.button_group = [self.play_button, self.settings_button, self.quit_button]

    def draw_background(self):
        super().draw_background()

    def draw_foreground(self):
        super().draw_foreground()
        [button.draw(self.game.screen) for button in self.button_group]

    def handle_keys(self, event):
        super().handle_keys(event)
        if event.type in [pg.KEYDOWN]:
            if event.key in [pg.K_a]:
                self.game.scene_manager.next_scene("Splash")

    def handle_mouse(self, event):
        super().handle_mouse(event)
        mouse_pos = pg.mouse.get_pos()

        for button in self.button_group:
            if button.rect.collidepoint(mouse_pos):
                button.hovered = True
            else:
                button.hovered = False

        if event.type in [pg.MOUSEBUTTONDOWN]:
            if event.button == 1:
                for button in self.button_group:
                    if button.rect.collidepoint(mouse_pos):
                        button.clicked()

    def scene_enter(self):
        super().scene_enter()

    def scene_exit(self):
        super().scene_exit()
        for button in self.button_group:
            button.hovered = False