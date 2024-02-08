import pygame
import sys
from random import *

from sprites.platform import Platform
from sprites.doodle import Doodle
from sprites.springs import Spring
from sprites.game import Score, GameOver

pygame.init()
# Константы/Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
 
# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()
 
def main():
    # Спрайты/Sprites
    platfroms = pygame.sprite.Group()
    for y in range(25, screen.get_height(), 50):
        x = randint(100, screen.get_width()-100)
        platfroms.add(Platform((x,y)))

    quantity = len(platfroms)

    player = Doodle()
    springs = pygame.sprite.Group()
    score = Score()

    game_over = False
    offset = 0
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
                if event.key == pygame.K_ESCAPE:
                    main()
        
        for platform in platfroms:
            if (platform.rect.collidepoint(player.rect.bottomleft) or \
                platform.rect.collidepoint(player.rect.bottomright)) and player.gravity <= 0:
                if platform.color == "red":
                    platform.image = platform.broken
                else:
                    player.gravity = 15
        if player.rect.bottom < 0:
            offset = 20
        elif player.rect.bottom < screen.get_height() / 2: 
            offset = 10  
        else: 
            offset = 0

        for spring in springs:
            if spring.rect.collidepoint(player.rect.bottomleft) or\
            spring.rect.collidepoint(player.rect.bottomright) or \
            spring.rect.collidepoint(player.rect.midbottom):
                if spring.image != spring.relaxed:
                    spring.image = spring.relaxed
                    player.gravity = 50

        if player.rect.top > screen.get_height():
            game_over = True
            end = GameOver()
        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        for x in range(0, screen.get_width(), 10):
            pygame.draw.line(screen, (222,222,222), (x,0), (x,screen.get_height()))
        for y in range(0, screen.get_height(), 10):
            pygame.draw.line(screen, (222,222,222), (0, y), (screen.get_width(), y))

        platfroms.draw(screen)
        player.draw(screen)
        springs.draw(screen)
        score.draw(screen)

        if game_over:
            end.draw(screen)
        # Обновление спрайтов/Updating sprites

        if not game_over:
            platfroms.update(offset)
            if quantity > len(platfroms):
                x = randint(100, screen.get_width() - 100)
                platform = Platform((x, 0))
                platfroms.add(platform)
                if platform.color == "green" and randint(1,100) in range(1,10):
                    springs.add(Spring(platform.rect.topleft))
            springs.update(offset)
            player.update(offset)
            score.update(offset)

        # Обновление экрана/Screen Refresh
        pygame.display.update()



if __name__ == "__main__":
    main()
