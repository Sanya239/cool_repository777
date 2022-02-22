import pygame
screen = pygame.display.set_mode((400,300),pygame.RESIZABLE)
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False


