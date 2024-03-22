#Made similar to this video: https://www.youtube.com/watch?v=BZUdGqeOD0w&ab_channel=TheCodingTrain
#However, implemented using pygame


import pygame
import sys

# Константы
WIDTH = 400
HEIGHT = 400
FPS = 60
res = 4

cols = HEIGHT//res
rows = WIDTH//res


# Создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Ripples")
clock = pygame.time.Clock()

# Инициализация массивов
current = [[0] * rows for _ in range(cols)]
previous = [[0] * rows for _ in range(cols)]
damping = 0.99

def main():
    global current, previous

    running = True
    while running:
        clock.tick(FPS)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                previous[mouse_x//res][mouse_y//res] = 255

        # Обновление спрайтов
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                current[x][y] = (previous[x - 1][y] +
                                 previous[x + 1][y] +
                                 previous[x][y - 1] +
                                 previous[x][y + 1]) / 2 - current[x][y]
                current[x][y] *= damping

        # Отрисовка
        for x in range(rows):
            for y in range(cols):
                c = abs(int(current[x][y]))
                pygame.draw.rect(screen, (c, c, c), (x*res, y*res, x+res, y+res))

        # Обновление экрана
        pygame.display.update()

        # Перезапись массивов
        temp = previous
        previous = current
        current = temp

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
