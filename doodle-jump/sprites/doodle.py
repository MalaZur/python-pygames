import pygame

class Doodle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.left = pygame.image.load('assets/images/left.png')
        self.left_1 = pygame.image.load('assets/images/left_1.png')

        self.right = pygame.transform.flip(self.left, True, False)
        self.right_1 = pygame.transform.flip(self.left_1, True, False)

        self.image = self.left
        self.rect = self.image.get_rect()
        self.surface = pygame.display.get_surface()

        self.rect.center = self.surface.get_rect().center

        self.gravity = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, offset):
        self.rect.y += offset
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 10
            self.image = self.left
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 10
            if self.gravity < 0:
                self.image = self.right
            else:
                self.image = self.right_1
        
        if (self.image == self.left or self.image == self.left_1) and self.gravity > 0: 
            self.image = self.left_1
        elif (self.image == self.left or self.image == self.left_1) and self.gravity < 0:
            self.image = self.left

        if (self.image == self.right or self.image == self.right_1) and self.gravity > 0:
            self.image = self.right_1
        elif (self.image == self.right or self.image == self.right_1) and self.gravity < 0:
            self.image = self.right

        if self.rect.right < 0: self.rect.left = self.surface.get_width()
        if self.rect.left > self.surface.get_width(): 
            self.rect.right = 0
        
        self.rect.y -= self.gravity
        self.gravity -= 1