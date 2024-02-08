import pygame

class Spring(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.image = pygame.image.load('assets/images/spring.png')
        self.relaxed = pygame.image.load('assets/images/spring_1.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates[0], coordinates[1]+5

    def draw(self,surface):
        surface.blit(self.image, self.rect)

    def update(self, offset):
        self.rect.y += offset