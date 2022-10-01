import pygame

pygame.init()
WINDOW = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)

running = True
while running:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False