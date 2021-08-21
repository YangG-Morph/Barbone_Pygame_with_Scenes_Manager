import pygame as pg
from components.Scenes.Scene import Scene
from components.Button import Button

class Playing(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.menu_button = Button("Main Menu", (500, 90), (0, 250), center_x=True)
        self.settings_button = Button("Settings", (250, 90), (0, 350), center_x=True)
        self.menu_button.clicked = lambda: self.game.scene_manager.next_scene("MainMenu")
        self.settings_button.clicked = lambda: self.game.scene_manager.next_scene("Settings")
        self.button_group = [self.menu_button, self.settings_button]

    def draw_background(self):
        super().draw_background()

    def draw_foreground(self):
        super().draw_foreground()
        [button.draw(self.game.screen) for button in self.button_group]

    def handle_keys(self, event):
        super().handle_keys(event)

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