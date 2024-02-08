import pygame
from random import *

class Cell(pygame.sprite.Sprite):
    def __init__(self, state=None):
        super().__init__()
        if state is None:
            self.r = random()
            if self.r <= 0.5: self.state = 1
            else: self.state = 0
        else:
            self.state = state

    def draw(self, surface, x, y, resolution):
        if self.state == 1:
            color = (0, 0, 0)  # Черный цвет для заполненной клетки
        else:
            color = (255, 255, 255)  # Белый цвет для пустой клетки
        pygame.draw.rect(surface, color, (x, y, resolution, resolution))


