import pygame
import sys

from sprites.space import Space
from sprites.spaceship import Spaceship
from sprites.alien import Alien, generate_aliens
from sprites.explosion import Explosion
from sprites.health import HealthBar
from sprites.game import Game

pygame.init()
 
# Константы
WIDTH = 600
HEIGHT = 700
FPS = 60
 
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
 
def main():
    # Спрайты
    
    space = Space()

    player_bullets = pygame.sprite.Group()

    players = pygame.sprite.Group()
    player = Spaceship(player_bullets)
    players.add(player)

    aliens = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()
    generate_aliens(aliens, alien_bullets)

    explosions = pygame.sprite.Group()

    healthbar = HealthBar(player.health)

    game = pygame.sprite.Group()

    playing = True


    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)
    
        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for alien in aliens.sprites():
            if pygame.sprite.spritecollide(alien, player_bullets, True, pygame.sprite.collide_mask):
                exp = Explosion(alien.rect.center)
                exp.exp_sound.play()
                explosions.add(exp)
                alien.kill()

        for player in players.sprites():
            if pygame.sprite.spritecollide(player,alien_bullets, True, pygame.sprite.collide_mask):
                player.health -= 1
                healthbar.hearts.pop()
                if player.health < 1:
                    exp = Explosion(player.rect.center)
                    exp.exp_sound.play()
                    explosions.add(exp)
                    player.kill()
                else:
                    player.sound_damage.play()
        
        if not aliens.sprites() and playing:
            playing = False
            game.add(Game("Y O U  W I N", 1))
            game.add(Game("press ESC to play again", 2))


        elif not players.sprites() and playing:
            playing = False
            game.add(Game("Y O U  W I N", 1))
            game.add(Game("press ESC to play again", 2))
        
        if not playing:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                main()

        
    
        # Рендеринг
        screen.fill((0, 0, 0))
        space.draw(screen)
        aliens.draw(screen)
        alien_bullets.draw(screen)
        player_bullets.draw(screen)
        players.draw(screen)
        
        explosions.draw(screen)

        healthbar.draw(screen)

        game.draw(screen)
    
        # Обновление спрайтов
        space.update()
        aliens.update()
        alien_bullets.update()
        players.update()
        player_bullets.update()
        
        explosions.update()

        game.update()

        # Обновление экрана
        pygame.display.update()
 
if __name__ == "__main__":
    main()




