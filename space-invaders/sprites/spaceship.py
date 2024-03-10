import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, bullets):
        super().__init__()

        self.bullets = bullets
        self.image = pygame.image.load("assets/images/spaceship.png")
        self.rect = self.image.get_rect()

        self.cooldown = 500

        self.surface = pygame.display.get_surface().get_rect()
        self.rect.midbottom = self.surface.midbottom
        self.rect.y -= 40

        self.last_shot = pygame.time.get_ticks()

        self.shot_sound = pygame.mixer.Sound("assets/sounds/laser.wav")
        self.shot_sound.set_volume(0.075)

        self.sound_damage = pygame.mixer.Sound("assets/sounds/damage.wav")
        self.sound_damage.set_volume(0.1)

        self.health = 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= 3
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if self.rect.right < self.surface.width:
                self.rect.x += 3
        now = pygame.time.get_ticks()
        if key[pygame.K_SPACE] and now - self.last_shot > self.cooldown:
            self.shot_sound.play()
            bullet = Bullet(self.rect.midtop)
            self.bullets.add(bullet)
            self.last_shot = now

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()

        self.image = pygame.image.load("assets/images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= 5

        if self.rect.y <= 0: self.kill()