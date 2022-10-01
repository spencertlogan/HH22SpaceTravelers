import pygame
import classes

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
BLACK = (0, 0, 0)

#initialize player variables
playerHealth = 100
playerSpeed = 0
playerHeight = 50
playerWidth = 50
playerXpos = (WINDOW.get_width() / 2) - (playerWidth / 2)
playerYpos = (WINDOW.get_height() / 2) - (playerHeight/2)
playerImg = pygame.image.load("Alien.png")
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerHeight))

player = classes.Player(playerXpos, playerYpos, playerHealth, playerSpeed, playerWidth, playerHeight, playerImg)





running = True
while running:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    WINDOW.blit(player.img, (player.xpos, player.ypos))
    pygame.display.update()