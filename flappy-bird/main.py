import pygame
import sys

from sprites.background import City, Road
from sprites.bird import Bird
from sprites.pipes import Pipe
from sprites.score import Score

pygame.init()
 
# Константы/Constants
WIDTH = 288
HEIGHT = 512
FPS = 60
 
# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

def main():
    # Спрайты/Sprites
    city = City()
    road = Road()
    player = Bird()
    pipes = pygame.sprite.Group()
    pipes.add(Pipe())
    score = Score()

    game_over = False
    checkpoint = False
    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)
    
        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    main()

        if pipes.sprites()[0].rect1.x < player.rect.x and not checkpoint:
            score.points += 1
            checkpoint = True
            pygame.mixer.Sound('assets/sounds/point.wav').play()
        
        if (player.rect.top < 0 or player.rect.colliderect(road.rect) or player.rect.colliderect(road.rect1)) and not game_over :
            player.death_s.play()
            game_over = True

        for pipe in pipes:
            if ((pipe.rect1.collidepoint(player.rect.midbottom)) or \
               (pipe.rect2.collidepoint(player.rect.midtop))) and not game_over:
                player.death_s.play()
                game_over = True


        # Рендеринг/Rendering
        city.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        road.draw(screen)
        player.draw(screen)
        score.draw(screen)


        # Обновление спрайтов/Updating sprites
        if not game_over:
            road.update()
            player.update()
            pipes.update()
            if len(pipes) < 1:
                pipes.add(Pipe())
                checkpoint = False
        # Обновление экрана/Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()




