import pygame
import random
import classes

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
# color declaration
BLACK = (0, 0, 0)
RED = (255, 87, 51)
WHITE = (255,255,255) 
# menu button colors 
button_light = (170,170,170) 
button_dark = (100,100,100)
WIDTH = WINDOW.get_width()
HEIGHT = WINDOW.get_height()
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont('Corbel',50) 
# rendering a text written in 
# this font 
quitText = smallfont.render('quit' , True , WHITE) 
playText = smallfont.render('play' , True , WHITE)
titleText = bigfont.render("Untitled game", True, WHITE)

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
current_state = "menu"
running = True
aDown = False
DDown = False

while running:
    if current_state == "menu":
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
                    pygame.quit()
                #\/ is actually the play button
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50: 
                    current_state = "game"
    
        WINDOW.fill(BLACK)
        mouse = pygame.mouse.get_pos() 
        
        # DRAW THE BOXES
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
            
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 - 110,120,60]) 
            
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 - 110,120,60]) 
        
        
        WINDOW.blit(titleText , (100 ,HEIGHT/2 - 220))
        WINDOW.blit(quitText , (WIDTH/2 - 30,HEIGHT/2 + 100))
        WINDOW.blit(playText , (WIDTH/2 - 30,HEIGHT/2 - 100))
        
        
        pygame.display.update()
    
    if current_state == "game":
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
                player.xpos -= 0.1
                if player.xpos < 0:
                    player.xpos = 0
        if DDown:
            player.xpos += 0.1
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
        idx += 1

    pygame.display.update()
        



