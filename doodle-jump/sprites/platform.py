import pygame
from random import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        if randint(1,100) in range(1,11):
            self.image = pygame.image.load('assets/images/blue.png')
            self.color = "blue"
        elif randint(1,100) in range(1,11):
            self.image = pygame.image.load('assets/images/red.png')
            self.broken = pygame.image.load('assets/images/red_1.png')
            self.color = "red" 
        else:
            self.image = self.image = pygame.image.load('assets/images/green.png')
            self.color = "green"
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

        self.surface = pygame.display.get_surface()

        self.stepX = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, offset):
        self.rect.y += offset
        if self.rect.top > self.surface.get_height():
            self.kill()
        
        if self.color == "blue":
            self.rect.x += self.stepX
            if self.rect.right > self.surface.get_width():
                self.stepX = -5
            if self.rect.left <= 0:
                self.stepX = 5