import pygame
from random import *

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('assets/images/pipe1.png')
        self.image2 = pygame.image.load('assets/images/pipe2.png')

        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

        self.surface = pygame.display.get_surface()


        self.rect1.x = self.surface.get_rect().right
        self.rect1.y = randint(150,350)

        self.rect2.x = self.rect1.x
        self.rect2.y = self.rect1.y - 450

    def draw(self, surface):
        surface.blit(self.image1, self.rect1)
        surface.blit(self.image2, self.rect2)

    def update(self):
        self.rect1.x -= 2
        self.rect2.x -= 2
        if self.rect1.right  < 0:
            self.kill()