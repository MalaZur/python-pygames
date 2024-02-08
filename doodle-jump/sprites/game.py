import pygame
from random import *


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points = 0

        self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"HI {self.points}", True, (83,83,83))
        self.rect = self.image.get_rect()

        self.rect.topleft = (20,20)
        


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"{self.points}", True, (83,83,83))
    
    def update(self, offset):
        self.points += offset



class GameOver(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        
        self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 40)
        self.g_o = self.font.render(f"G A M E  O V E R", True, (83,83,83))
        self.rectg = self.g_o.get_rect()


        surface = pygame.display.get_surface()

        self.rectg.center = surface.get_rect().center

    def draw(self, surface):
        surface.blit(self.g_o, self.rectg)
