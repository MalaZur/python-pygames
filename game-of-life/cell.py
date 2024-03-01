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
        self.step = 0
        self.red = 0
        self.green = 0
        self. blue = 0

    def draw(self, surface, x, y, resolution):
        if self.step == 0: 
            self.red += 1
            if self.red == 255:
                self.step = 1
        if self.step == 1:
            if self.red != 0:
                self.red -= 1
            self.green += 1
            if self.green == 255:
                self.step = 2
        if self.step == 2:
            if self.green != 0:
                self.green -= 1
            self.blue += 1
            if self.blue == 255:
                self.step = 3
        if self.state == 1:
            color = (self.red, self.green, self.blue)  # Черный цвет для заполненной клетки

        else:
            self.red = 0
            self.green = 0
            self.blue = 0
            color = (255, 255, 255)  # Белый цвет для пустой клетки
        pygame.draw.rect(surface, color, (x, y, resolution, resolution))


