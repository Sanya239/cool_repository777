import pygame
import os
import buttons.button_class

game_folder = os.path.dirname(__file__)


class main_menu():

    def __init__(self, screen):
        self.general_mode =0
        self.screen = screen
        self.buttons = pygame.sprite.Group()

        self.multy_play_button = buttons.button_class.button()
        self.multy_play_button.rect.center = (400, 100)
        self.buttons.add(self.multy_play_button)

        self.single_play_button = buttons.button_class.button()
        self.single_play_button.rect.center = (400, 200)
        self.buttons.add(self.single_play_button)

        self.settings_button = buttons.button_class.button()
        self.settings_button.rect.center = (400,300)
        self.buttons.add(self.settings_button)

        screen.fill((0, 255, 0))
        self.buttons.draw(screen)


    def update(self,event):
            self.buttons.update(event)
            self.buttons.draw(self.screen)
            if self.multy_play_button.message == True:
                self.general_mode = 1
            elif self.single_play_button.message == True:
                print('aa')
                self.general_mode = 2




