import pygame
from random import *

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_run1 = pygame.image.load("assets/images/1_.png")
        self.image_run2 = pygame.image.load("assets/images/2_.png")

        self.image = self.image_run1
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        self.rect.bottom = surface.get_rect().centery + 5
        self.rect.left = 60

        self.step = 0
        self.height = 15
        self.jumping = False
        self.sound_jump = pygame.mixer.Sound("assets/sounds/jump.wav")

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        if self.step % 7 == 0:
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.sound_jump.play()

        if self.jumping:
            self.jump()

    def jump(self):
        self.rect.y -=self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False