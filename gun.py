import pygame

class Gun():

    def __init__(self, screen):
        """Инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('img/gun2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """Отрисовка пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= 2