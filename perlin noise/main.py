import pygame
import sys
from random import *
from p5 import *



from particle import Particle


pygame.init()

# Константы/Constants
WIDTH = 1000
HEIGHT = 1000
FPS = 60

scl = 40

rows = HEIGHT//scl
cols = WIDTH//scl








# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Perlin noise flow 2D")
clock = pygame.time.Clock()


def main():
    
    inc = 0.2
    zoff = 0
    flowfield = [Vector(0, 0) for _ in range(cols * rows)]

    
    particles = []
    for i in range(400):
        p = Particle(scl)
        particles.append(p)

    screen.fill((255, 255, 255))

    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)
        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                
    
        ## Рендеринг/Rendering
        #If you want to see each vector that affects the movement of particles, uncomment pygame.draw.line and put screen.fill into loop.
         
        noise_detail(5)
        yoff = 0
        for y in range(rows):
            xoff = 0
            for x in range(cols):
                
                index = int(x + y * cols)

                r = noise(xoff, yoff, zoff)*TWO_PI*4
                xoff += inc

                v = Vector.from_angle(r)
                
                #pygame.draw.line(screen, color="green", start_pos=[x*scl+scl*0.5, y*scl+scl*0.5], end_pos=[(x+v.x)*scl+scl*0.5, (y+v.y)*scl+scl*0.5])
                v.magnitude = 0.5

                
                flowfield[index]=v
                
            yoff += inc

            zoff += 0.0001

        for i in range(len(particles)):
            particles[i].follow(flowfield)
            particles[i].update()
            particles[i].edges()
            particles[i].draw(screen)
            
            

        
        
        # Обновление экрана/Screen Refresh
        pygame.display.update()
        
 
if __name__ == "__main__":
    main()
