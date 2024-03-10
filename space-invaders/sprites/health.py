import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, health):
        super().__init__()
        self.hearts = []
        for i in range(health):
            self.image = pygame.image.load("assets/images/heart.png")
            self.rect = self.image.get_rect()
            self.rect.topright = (pygame.display.get_surface().get_width() - (10 + 35*i), 10)
            self.hearts.append((self.image, self.rect))


    def draw(self, surface):
        surface.blits(self.hearts)