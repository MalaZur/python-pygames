import pygame
from random import *

class Alien(pygame.sprite.Sprite):
    def __init__(self, coordinates, bullets):
        super().__init__()
        images = [r"assets/images/alien{}.png".format(i) for i in range(1,6)]
        self.image = pygame.image.load(choice(images))
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

        self.step = 1
        self.steps = 0

        self.bullets = bullets
        self.cooldown = randint(3000, 15000)
        self.last_shot = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.step
        self.steps += abs(self.step)

        if self.steps >= 50:
            self.steps *= -1
            self.step *= -1
        
        time_now = pygame.time.get_ticks()
        if time_now - self.last_shot > self.cooldown:
            bullet = Bullet((self.rect.centerx, self.rect.bottom))
            self.bullets.add(bullet)
            self.last_shot = time_now
            self.cooldown = randint(3000,15000)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()

        self.image = pygame.image.load("assets/images/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y += 2

        if self.rect.y >= pygame.display.get_surface().get_height(): 
            self.kill()

def generate_aliens(group, bullets):
    for column in range(1,6):
        for row in range(1,5):
            x = 100 * column
            y = 75 * row
            alien = Alien((x,y), bullets)
            group.add(alien)

