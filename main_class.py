import pygame
import os
import menu
import multy_mode
import single_mode

FPS = 60


class app():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('нарды ахах')
        self.clock = pygame.time.Clock()
        self.sprites = []
        self.mode = 0

        self.menu = menu.main_menu(self.screen)
        self.game1 = multy_mode.multy_game(self.screen)
        self.game2 = single_mode.single_game(self.screen)
        #self.menu.screen = self.screen
        self.running = True

    def update(self):
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.mode == 0:
                    self.menu.update(event)
                    self.clock.tick(FPS)

                    if self.menu.general_mode== 1:
                        self.mode = 1

                        pygame.display.flip()
                        pygame.time.delay(150)
                        self.game1.start_a_game()
                        pygame.display.flip()
                    if self.menu.general_mode == 2:
                        self.mode = 2
                        pygame.display.flip()
                        pygame.time.delay(150)
                        self.game2.start_a_game()
                        pygame.display.flip()

                elif self.mode == 1:

                    self.game1.update(event)

                    self.clock.tick(FPS)

                elif self.mode == 2:

                    self.game2.update(event)

                    self.clock.tick(FPS)


        pygame.display.flip()


produt = app()

while produt.running:

    produt.update()

