import pygame

class Game(pygame.sprite.Sprite):
    def __init__(self, text, ind):
        super().__init__()
        if ind == 1:
            self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 20)
            self.image = self.font.render(text, True, (83,83,83))
            self.rect = self.image.get_rect()
            self.rect.center = pygame.display.get_surface().get_rect().center

        elif ind == 2:
            self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 10)
            self.image = self.font.render(text, True, (83,83,83))
            self.rect = self.image.get_rect()
            self.rect.center = pygame.display.get_surface().get_rect().centerx, \
                               pygame.display.get_surface().get_rect().centery + 30



    def draw(self, surface):
        surface.blit(self.image, self.rect)
