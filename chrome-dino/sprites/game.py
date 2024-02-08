import pygame
from random import *


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0

        self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"HI {self.points}", True, (83,83,83))

        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        self.rect.right = surface.get_width()-self.rect.width
        self.rect.top = 60
        


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"HI {self.points}", True, (83,83,83))
    
    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1


class GameOver(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        
        self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 20)
        self.g_o = self.font.render(f"G A M E  O V E R", True, (83,83,83))
        self.rectg = self.g_o.get_rect()

        self.reset = pygame.image.load("assets/images/reset.png")
        self.rectr = self.reset.get_rect()

        surface = pygame.display.get_surface()

        self.rectg.center = (surface.get_width()/2, surface.get_height()/4)
        self.rectr.midtop = (self.rectg.centerx, self.rectg.bottom+20)

    def draw(self, surface):
        surface.blit(self.g_o, self.rectg)
        surface.blit(self.reset, self.rectr)
