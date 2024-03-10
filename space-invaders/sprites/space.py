import pygame

class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image1 = pygame.image.load("assets/images/space.png")
        self.image2 = pygame.image.load("assets/images/space.png")
        
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

        self.surface = pygame.display.get_surface()
        self.rect1.midbottom = self.surface.get_rect().midbottom

        self.rect2.midbottom = self.rect1.midtop
    
    def draw(self, surface):
        surface.blit(self.image1, self.rect1)
        surface.blit(self.image2, self.rect2)

    def update(self):
        self.rect1.y += 1
        self.rect2.y += 1

        if self.rect1.top >= pygame.display.get_surface().get_rect().height:
            self.rect1.midbottom = self.rect2.midtop
        if self.rect2.top >= pygame.display.get_surface().get_rect().height:
            self.rect2.midbottom = self.rect1.midtop