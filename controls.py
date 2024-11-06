import pygame, sys


def events(gun):
    """Обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.move_right = True
            #влево
            elif event.key == pygame.K_LEFT:
                gun.move_left = True
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.move_right = False
            #влево
            elif event.key == pygame.K_LEFT:
                gun.move_left = False