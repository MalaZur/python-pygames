import pygame
import sys
from random import *



pygame.init()


# Константы
WIDTH = 500
HEIGHT = 500
FPS = 60


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")
clock = pygame.time.Clock()


# Классы
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/ball-game/ball.png')
        self.rect = self.image.get_rect()
        self.stepX = randint(3,6)
        self.stepY = randint(3,6)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.dupe = 0
        self.rect.x += self.stepX
        self.rect.y += self.stepY
        if self.rect.right > 500:
            self.stepX = -randint(3,6)
            self.dupe = 1
        if self.rect.left < 0:
            self.stepX = randint(3,6)
            self.dupe = 1
        if self.rect.top < 0:
            self.stepY = randint(3,6)
            self.dupe = 1
        if self.rect.bottom > 500:
            self.stepY = -randint(3,6)
            self.dupe = 1
# Спрайты
balls = [Ball()]


running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)


    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Рендеринг
    screen.fill(0)
    for ball in balls:
        ball.draw(screen)


    # Обновление спрайтов
    for ball in balls:
        ball.update()
        if ball.dupe == 1:
            balls.append(Ball())
            ball.dupe = 0

    # Обновление экрана
    pygame.display.update()