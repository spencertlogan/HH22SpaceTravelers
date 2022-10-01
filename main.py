import pygame

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
BLACK = (0, 0, 0)

class Obstacle:
    
    def __init__(self, xpos, ypos, img=None):
        self.xpos = xpos
        self.ypos = ypos
        self.img = img

    


running = True
while running:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False