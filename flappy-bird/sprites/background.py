import pygame

class City(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/city.png')
        self.rect = self.image.get_rect()

        self.surface = pygame.display.get_surface()


        self.rect.center = self.surface.get_rect().center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/road.png')
        self.rect = self.image.get_rect()    
        self.image1 = pygame.image.load('assets/images/road.png')
        self.rect1 = self.image.get_rect()    


        self.surface = pygame.display.get_surface()

        self.rect.midbottom = self.surface.get_rect().midbottom
        self.rect1.midleft = self.rect.midright
        self.rect.y += 25
        self.rect1.y += 25

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.x -= 2
        self.rect1.x -= 2

        if self.rect.right < 0:
            self.rect.midleft = self.rect1.midright
        if self.rect1.right < 0:
            self.rect1.midleft = self.rect.midright