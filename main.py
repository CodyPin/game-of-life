import pygame
import random

grid = []
cols = 10
rows = 10
res = 10
width = 1280
height = 1280


def make2DArray(c, r):
    arr = []
    for _ in range(r):
        row = []
        for _ in range(c):
            random_bit = random.randint(0, 1)
            row.append(random_bit)
        arr.append(row)
    return arr


def countNeighbors(x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                neighbor_row = (x + i + rows) % rows
                neighbor_col = (y + j + cols) % cols
                sum += grid[neighbor_row][neighbor_col]
    return sum


def toggle_cell(c, r):
    grid[c][r] = 1


if __name__ == '__main__':
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    drawing = False

    # Set the window title
    pygame.display.set_caption("Game of Life")

    cols = int(width / res)
    rows = int(height / res)

    grid = make2DArray(cols, rows)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i in range(cols):
            for j in range(rows):
                x = i * res
                y = j * res
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, "white", (x, y, res, res))

        next_grid = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            for j in range(rows):
                state = grid[i][j]
                neighbors = countNeighbors(i, j)
                if state == 0 and neighbors == 3:
                    next_grid[i][j] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = state

        grid = next_grid

        # flip() the display to put your work on screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    mouse_pos = pygame.mouse.get_pos()
                    row = mouse_pos[0] // res
                    col = mouse_pos[1] // res
                    if 0 <= row < rows and 0 <= col < cols:
                        toggle_cell(row, col)

        clock.tick(60)  # limits FPS

    pygame.quit()
