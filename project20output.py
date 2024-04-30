import pygame
import random
import sys

# Starting Pygame
pygame.init()

# The attributes of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_SIZE = 30
BG_COLOR = (30, 30, 30)
TARGET_COLOR = (255, 0, 0)
FPS = 60
score = 0

# The game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Train Your Aim!")

# Clock
clock = pygame.time.Clock()

# Function to draw target
def draw_target(x, y):
    pygame.draw.rect(screen, TARGET_COLOR, (x, y, TARGET_SIZE, TARGET_SIZE))

# Function to spawn a new target
def spawn_target():
    x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)
    return x, y

# Randomly spawn first target
target_x, target_y = spawn_target()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + TARGET_SIZE and target_y < mouse_y < target_y + TARGET_SIZE:
                score += 1
                target_x, target_y = spawn_target()  # Spawn new target on hit

    # Fill background
    screen.fill(BG_COLOR)
    
    # Draw target
    draw_target(target_x, target_y)

    # Show score
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()

    # FPS
    clock.tick(FPS)
