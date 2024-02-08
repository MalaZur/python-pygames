import pygame
import sys

from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstacles import Cactus
from sprites.game import Game
from sprites.game import GameOver

pygame.init()


# Константы
WIDTH = 700
HEIGHT = 500
FPS = 60


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

def main():
    # Спрайты
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Game()


    game_over = False
    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)


        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    main()

        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle) and not game_over:
                pygame.mixer.Sound("assets/sounds/die.wav").play()
                game_over = True
                end = GameOver()

        # Рендеринг
        screen.fill((255,255,255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        obstacles.draw(screen)
        score.draw(screen)

        if game_over:
            end.draw(screen)

        


        # Обновление спрайтов
        if not game_over:
            road.update()
            clouds.update()
            if len(clouds) < 3:
                cloud = Cloud()
                clouds.add(cloud)
            player.update()
            obstacles.update()
            if len(obstacles) < 1:
                cactus = Cactus()
                obstacles.add(cactus)
            score.update()
            



        # Обновление экрана
        pygame.display.update()

if __name__ == "__main__":
    main()