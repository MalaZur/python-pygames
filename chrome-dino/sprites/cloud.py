import pygame
from random import *
#pygame/chrome-dino/assets/images/cloud.png
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/cloud.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        self.rect.x = surface.get_width()
        self.rect.y = randint(0, surface.get_height() / 2 - self.rect.height)

        self.stepX = randint(3,5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self):
        self.rect.x -= self.stepX

        if self.rect.right < 0:
            self.kill()