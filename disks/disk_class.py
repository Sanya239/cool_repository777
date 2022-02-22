import pygame
import os

game_folder = os.path.dirname(__file__)




class disk(pygame.sprite.Sprite):
    def __init__(self,colour,position):
        pygame.sprite.Sprite.__init__(self)

        self.black_disk = pygame.image.load(os.path.join(game_folder, 'black_disk2.bmp')).convert()
        self.black_disk.set_colorkey((255,0,0))
        self.white_disk = pygame.image.load(os.path.join(game_folder, 'white_disk2.bmp')).convert()
        self.white_disk.set_colorkey((255,0,0))
        self.colour = colour
        if self.colour == 2:
            self.image = self.black_disk
        else:
            self.image = self.white_disk
        self.rect = self.image.get_rect()
        self.rect.center = (position[0]*80+120,position[1]*80+120)
    def flip(self):
        self.colour = 3-self.colour
        if self.colour == 2:
            self.image = self.black_disk
        else:
            self.image = self.white_disk
