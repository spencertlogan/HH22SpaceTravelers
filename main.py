import pygame
import random
import classes

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
# color declaration
BLACK = (0, 0, 0)
RED = (255, 87, 51)

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

def collides(rect1, rect2):
    # fix this to be interactive
    if (rect1.xpos - rect1.len) <= rect2.xpos <= (rect1.xpos + rect1.len): 
        if (rect1.ypos - rect1.width) <= rect2.ypos <= (rect1.ypos + rect1.width):
            return True
    return False


obstacle_list = list()

# main loop
running = True
aDown = False
DDown = False

while running:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                aDown = True
            elif event.key == pygame.K_d:
                DDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                aDown = False
            elif event.key == pygame.K_d:
                DDown = False
        
        if aDown:
            if player.xpos > 0:
                player.xpos -= 5
                if player.xpos < 0:
                    player.xpos = 0
        if DDown:
            if player.xpos < 400:
                player.xpos += 5
                if player.xpos > 400:
                    player.xpos = 400
                
    WINDOW.blit(player.img, (player.xpos, player.ypos))
    
    # creating obstacles and moving them
    # will go across the screen and randomly create rectangles
    # len = x value | width = y value
    curr_pixel = 0
    while curr_pixel <= 500:

        if random.randint(0, 20000) == 0:
            curr_len = random.randint(25, 100)
            curr_width = random.randint(25, 50)

            # WILL NOT WORK FOR NON-RECTANGLES
            

            new_rect = classes.Rectangle(curr_pixel, 600, curr_len, curr_width)
            for obstacle in obstacle_list:
                if collides(new_rect, obstacle): # if collides, do not add new box
                    break
            else: 
                obstacle_list.append(new_rect)
                curr_pixel = curr_pixel + curr_len

        curr_pixel += 25


    # moving and deleting boxes
    idx = 0
    while idx < len(obstacle_list):
        obstacle_list[idx].ypos -= 0.1
        
        
        pygame.draw.rect(WINDOW, RED, (obstacle_list[idx].xpos, obstacle_list[idx].ypos, obstacle_list[idx].len, obstacle_list[idx].width))

        if obstacle_list[idx].ypos < -20: # if the obstacle is off the screen, remove from list
            obstacle_list.pop(idx)
        
        idx += 1

    
    pygame.display.update()
        



