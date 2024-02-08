import pygame
import sys
from random import *
from cell import Cell

def make2DArray(rows, cols):
    array = []
    for i in range(rows):
        array.append([0] * cols)
    return array


def countNeighbors(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1,2):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows
            sum += grid[col][row].state
    sum -= grid[x][y].state
    return sum







pygame.init()

# Константы/Constants
WIDTH = 1200
HEIGHT = 900
FPS = 60

cols = int(WIDTH/10)
rows = int(HEIGHT/10)
resolution = 10



# Пример использования:



# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

grid = make2DArray(cols, rows)

cells = pygame.sprite.Group()
for i in range(cols):
    for j in range(rows):
        cell = Cell()
        cells.add(cell)
        grid[i][j] = cell

def main():
    global grid
    global cells


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
                if event.key == pygame.K_SPACE:
                    cells.empty()
                    for i in range(cols):
                        for j in range(rows):
                            cell = Cell()
                            cells.add(cell)
                            grid[i][j] = cell
                    print(countNeighbors(grid, 0,0))
                    print(len(cells))
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Проверяем, что была нажата левая кнопка мыши
                mouse_x, mouse_y = event.pos[0] // resolution, event.pos[1] // resolution  # Координаты мыши в координатах клеток
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_x = mouse_x + i
                        new_y = mouse_y + j
                        # Проверяем, чтобы новые координаты не выходили за пределы сетки и чтобы клетка была пустой (состояние 0)
                        if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_x][new_y].state == 0:
                            grid[new_x][new_y].state = 1  # Изменяем состояние клетки на 1
                
    
        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        
        #for i in range(cols):
        #     for j in range(rows):
        #        grid[i][j].draw(screen, i*10, j*10, resolution-1)
    
        # Обновление спрайтов/Updating sprites
 
        next_grid = make2DArray(cols, rows)  # Создаем новую сетку для следующего поколения клеток
        
        for i in range(cols):
            for j in range(rows):
                neighbors = countNeighbors(grid, i, j)
                state = grid[i][j].state
                if (state == 0 and neighbors == 3):
                    next_grid[i][j] = 1
                elif (state == 1 and (neighbors < 2 or neighbors > 3)):
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = state
        
        # Применяем новое состояние ко всем клеткам одновременно
        for i in range(cols):
            for j in range(rows):
                grid[i][j].state = next_grid[i][j]
                grid[i][j].draw(screen, i*10, j*10, resolution-1)
                    

        # Обновление экрана/Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()
