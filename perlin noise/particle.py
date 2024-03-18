from p5 import *
import pygame
from random import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, scl):
        super().__init__()

        self.pos = Vector(randint(0,pygame.display.get_surface().get_width()-1), randint(0,pygame.display.get_surface().get_height()-1))
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

        self.surface = pygame.display.get_surface()
        self.scl = scl

        self.maxspeed = 4

        self.prev = self.pos.copy()
    

    def update(self):
        self.vel += self.acc
        self.vel.limit(self.maxspeed)
        self.pos += self.vel
        self.acc *= 0
        

    def applyForce(self, force):
        self.acc += force

    def draw(self, surface):

        pygame.draw.line(surface, start_pos=(self.pos.x, self.pos.y), end_pos=(self.prev.x, self.prev.y), width=1, color=[0,0,0,30])
        #pygame.draw.circle(surface, center=(self.pos.x, self.pos.y), color=[0,0,0,100], radius=1)
        self.updatePrev()
    
    def updatePrev(self):
        self.prev.x = self.pos.x
        self.prev.y = self.pos.y

    def edges(self):
        if self.pos.x > self.surface.get_width():
            self.pos.x = 0
            self.updatePrev()

        if self.pos.x < 0:
            self.pos.x = self.surface.get_width()-1
            self.updatePrev()

        if self.pos.y > self.surface.get_height():
            self.pos.y = 0
            self.updatePrev()

        if self.pos.y < 0:
            self.pos.y = self.surface.get_height()-1
            self.updatePrev()

    def follow(self, vectors):
        cols = self.surface.get_width() // self.scl
        x = floor(self.pos.x // self.scl)
        y = floor((self.pos.y) // self.scl)
        index = x + y * cols
        #print(f"x:{x}\ny:{y}\ny pos:{self.pos.y}\nind:{index}\nind len:{len(vectors)}\ncols:{cols}")
        force = vectors[index]
        self.applyForce(force)
