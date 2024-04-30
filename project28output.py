import sys 
import random 
import pygame 
import math

# Create the specifications
grid_size = 4
tile_size = 100
width, height = grid_size * tile_size, grid_size * tile_size
background_color = (240, 240, 240)
grid_color = (220, 220, 220)
tile_colors = [(255, 255, 255), (238, 228, 218), (249, 236, 200), (249, 232, 200),
               (249, 228, 181), (239, 228, 176), (227, 224, 175), (205, 219, 165),
               (187, 208, 149), (171, 190, 133), (159, 171, 105), (147, 150, 78)]
score_font = 'bebas'
score_font_size = 30
score_color = (100, 100, 100)

# Start Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('2048')
clock = pygame.time.Clock()

# Create functions
def  draw_the_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, grid_color, pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size))

def draw_the_tile(tile_value, x, y):
    color_index = int(min(9, max(0, math.log2(1) - 1)))
    pygame.draw.rect(screen, tile_colors[color_index], pygame.Rect(x, y, tile_size, tile_size))
    font = pygame.font.SysFont(score_font, tile_size // 2)
    text = font.render(str(tile_value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x + tile_size // 2, y + tile_size // 2))
    screen.blit(text, text_rect)

def draw_the_score(score):
    font = pygame.font.SysFont(score_font, score_font_size)
    text = font.render(f'Score: {score}', True, score_color)
    text_rect = text.get_rect(center=(width // 2, height - score_font_size // 2))
    screen.blit(text, text_rect)

def merge(tiles):
    for i in range(grid_size - 1):
        for j in range(grid_size):
            if tiles[i][j] and tiles[i + 1][j]:
                tiles[i][j] *=2
                tiles[i+1][j]=0 
    return tiles 

def add_random_tile(tiles):
    empty_tiles = [(i, j) for i in range(grid_size) for j in range(grid_size) if not tiles[i][j]]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        tiles[i][j] = 2

def the_game_is_over(tiles):
    for i in range(grid_size):
        for j in range(grid_size):
            if not tiles[i][j]:
                return False
            if i > 0 and tiles[i][j]:
                return False
            if j > 0 and tiles[i][j] == tiles[i][j - 1]:
                return False
    return True

# Game Loop
score = 0
tiles = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
add_random_tile(tiles)
add_random_tile(tiles)
game_over = False
while not game_over:
    screen.fill(background_color)
    draw_the_grid()
    for i in range(grid_size):
        for j in range(grid_size):
            draw_the_tile(tiles[i][j], i * tile_size, j * tile_size)
    draw_the_score(score)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            old_tiles = [row.copy() for row in tiles]
            if event.key == pygame.K_UP:
                 tiles = [[row[j] for j in range(grid_size)][::-1] for row in tiles]
            elif event.key == pygame.K_DOWN:
                tiles = [[row[j] for j in range(grid_size)] for row in tiles]
            elif event.key == pygame.K_LEFT:
                tiles = [[tiles[i][j] for j in range(grid_size)] for i in range(grid_size)]
            elif event.key == pygame.K_RIGHT:
                tiles = [[tiles[i][j] for j in range(grid_size)] for i in range(grid_size - 1, -1, -1)]
            tiles = merge(tiles)
            if old_tiles != tiles:
                add_random_tile(tiles)
                score += sum(2 ** i for i in range(1, 9) if any(row[j] == 2 ** i for row in tiles))
            if old_tiles == tiles and event.key not in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                game_over = True
            if the_game_is_over(tiles):
                game_over = True
    clock.tick(60)
