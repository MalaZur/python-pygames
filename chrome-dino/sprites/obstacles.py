import os
import pygame
from random import *

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        images = ['largecactus1.png', 'largecactus2.png', 'largecactus3.png',
          'smallcactus1.png', 'smallcactus2.png', 'smallcactus3.png',]
        image = os.path.join(r'assets/images', choice(images))

        self.image = pygame.image.load(image)

        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        self.rect.bottomleft = (surface.get_width() * 2, surface.get_rect().centery+5)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

