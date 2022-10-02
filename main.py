import pygame
import random
import classes

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
# color declaration
BLACK = (0, 0, 0)
RED = (255, 87, 51)
WHITE = (255,255,255) 
GREY = (128, 128, 128)
# menu button colors 
button_light = (170,170,170) 
button_dark = (100,100,100)
WIDTH = WINDOW.get_width()
HEIGHT = WINDOW.get_height()
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)
smallerfont = pygame.font.SysFont('Corbel',15)
bigfont = pygame.font.SysFont('Corbel',50) 
scorefont = pygame.font.SysFont('Corbel',20)
# rendering a text written in 
# this font 
score = 0

quitText = smallfont.render('quit' , True , WHITE) 
playText = smallfont.render('play' , True , WHITE)
titleText = bigfont.render("Untitled game", True, WHITE)
authorsText = smallerfont.render("Created by Christion Bradley, Specer Logan, Sam Cole, and Revanth Myana", True, WHITE)
replayText = smallfont.render('play again' , True , WHITE)
deathText = bigfont.render("Better Luck Next Time", True, RED)

#background image
spaceBackground = pygame.image.load("starryBackground.PNG").convert()
spaceBackground = pygame.transform.scale(spaceBackground, (500,600))

#initialize player variables
playerHealth = 100
playerSpeed = 0.1
playerHeight = 50
playerWidth = 50
playerXpos = (WINDOW.get_width() / 2) - (playerWidth / 2)
playerYpos = (WINDOW.get_height() / 2) - (playerHeight/2)
playerImg = pygame.image.load("Alien.png")
playerImgRed = pygame.image.load("redalien.png")
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerHeight))
playerImgRed = pygame.transform.scale(playerImgRed, (playerWidth, playerHeight))

player = classes.Player(playerXpos, playerYpos, playerHealth, playerSpeed, playerWidth, playerHeight, playerImg)

def player_collides(player, rect):
    # react - len=x | width=y
    if (rect.xpos - rect.len) <= player.xpos <= (rect.xpos + rect.len):
        if (rect.ypos - rect.width) <= player.ypos <= (rect.ypos + rect.width):
            return True
    return False

def collides(rect1, rect2):
    # fix this to be interactive
    if (rect1.xpos - rect1.len) <= rect2.xpos <= (rect1.xpos + rect1.len): 
        if (rect1.ypos - rect1.width) <= rect2.ypos <= (rect1.ypos + rect1.width):
            return True
    return False


obstacle_list = list()
health_bar = classes.Rectangle(380, 20, 100, 25)
boost_bar = classes.Rectangle(0, 20, 100, 25)
asteroid_image = pygame.image.load("asteroid.png")
last_collision = 0

# main loop
current_state = "menu"
running = True
aDown = False
DDown = False
spaceDown = False


SPEEDEVENT = pygame.event.custom_type()
pygame.time.set_timer(SPEEDEVENT, 1000)

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
        WINDOW.blit(spaceBackground, (0, 0))
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
        WINDOW.blit(authorsText , (25,HEIGHT/2 + 280))
        
        
        pygame.display.update()
    
    if current_state == "death":
        scoreText = smallfont.render("You traveled {} ligthyears!".format(score), True, RED)
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
                    pygame.quit()
                #\/ is actually the replay button
                if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50: 
                    playerHealth = 100
                    playerSpeed = 0.1
                    playerHeight = 50
                    playerWidth = 50
                    playerXpos = (WINDOW.get_width() / 2) - (playerWidth / 2)
                    playerYpos = (WINDOW.get_height() / 2) - (playerHeight/2)
                    player = classes.Player(playerXpos, playerYpos, playerHealth, playerSpeed, playerWidth, playerHeight, playerImg)
                    obstacle_list = list()
                    health_bar = classes.Rectangle(380, 20, 100, 25)
                    boost_bar = classes.Rectangle(0, 20, 100, 25)
                    last_collision = 0
                    score = 0
                    aDown = False
                    DDown = False
                    spaceDown = False
                    current_state = "game"
                    

        mouse = pygame.mouse.get_pos() 
        
        # DRAW THE BOXES
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
            
        if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 90,HEIGHT/2 - 110,180,60]) 
            
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 90,HEIGHT/2 - 110,180,60]) 
        
        
        WINDOW.blit(quitText , (WIDTH/2 - 30,HEIGHT/2 + 100))
        WINDOW.blit(replayText , (WIDTH/2 - 70,HEIGHT/2 - 100))
        WINDOW.blit(deathText , (30,HEIGHT/2 - 220))
        WINDOW.blit(scoreText , (WIDTH/2 - 180,HEIGHT/2 - 160))
        
        
        pygame.display.update()
    
    if current_state == "game":
        WINDOW.fill(BLACK)
        WINDOW.blit(spaceBackground, (0, 0))
        #handles events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            #detects if keys are down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    aDown = True
                elif event.key == pygame.K_d:
                    DDown = True
                elif event.key == pygame.K_SPACE:
                    spaceDown = True
                    player.speed /= 2.0
            #detects if keys are up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    aDown = False
                elif event.key == pygame.K_d:
                    DDown = False
                elif event.key == pygame.K_SPACE:
                    spaceDown = False
                    player.speed *= 2.0
            elif event.type == SPEEDEVENT:
                if spaceDown:
                    player.speed += 0.0025
                else:
                    player.speed += 0.005
        #updates according to inputs
        if aDown:
                player.xpos -= 0.3
                if player.xpos < 0:
                    player.xpos = 0
        if DDown:
            player.xpos += 0.3
            if player.xpos > 450:
                player.xpos = 450
        #player image
        WINDOW.blit(player.img, (player.xpos, player.ypos))

        # checking for collision with player
        # makes player_collision report only one colsion
        if pygame.time.get_ticks() > (last_collision + 500) and pygame.time.get_ticks() % 100 == 0:
            for obstacle in obstacle_list:
                if player_collides(player, obstacle):
                    last_collision = pygame.time.get_ticks()
                    player.health -= 25
        
        # Implementing Flickering
        if pygame.time.get_ticks() > 1000 and pygame.time.get_ticks() <= (last_collision + 1000): # and pygame.time.get_ticks() % 250 == 0:
            player.img = playerImgRed if player.img == playerImg else playerImg
        else:
            player.img = playerImg

        
        # creating obstacles and moving them
        # will go across the screen and randomly create rectangles
        # len = x value | width = y value
        curr_pixel = 0
        while curr_pixel <= 500:
            
            upper_bound = max(10, 7500 - (pygame.time.get_ticks() // 50))
            if random.randint(0, upper_bound) == 0:
                # curr_len = random.randint(25, 100)
                # curr_width = random.randint(25, 50)

                

                new_rect = classes.Rectangle(curr_pixel, 600, 20, 20)
                for obstacle in obstacle_list:
                    if collides(new_rect, obstacle): # if collides, do not add new box
                        break
                else: 
                    obstacle_list.append(new_rect)
                    curr_pixel = curr_pixel + 50 # curr_len

            curr_pixel += 25


        # moving and deleting boxes
        idx = 0
        while idx < len(obstacle_list):
            obstacle_list[idx].ypos -= player.speed
            
            WINDOW.blit(pygame.transform.scale(asteroid_image, (40, 40)), (obstacle_list[idx].xpos - 10, obstacle_list[idx].ypos - 10))
            # pygame.draw.rect(WINDOW, GREY, (obstacle_list[idx].xpos, obstacle_list[idx].ypos, obstacle_list[idx].len, obstacle_list[idx].width))

            if obstacle_list[idx].ypos < -20: # if the obstacle is off the screen, remove from list
                obstacle_list.pop(idx)
            
            idx += 1
        health_bar.len = player.health
        pygame.draw.rect(WINDOW, WHITE, (health_bar.xpos-3, health_bar.ypos-3, 106, health_bar.width+6))
        pygame.draw.rect(WINDOW, RED, (health_bar.xpos, health_bar.ypos, health_bar.len, health_bar.width))
        
        if player.health <= 0:
            current_state = "death"
        
        scoretext = scorefont.render("Distance: {}".format(score), True, WHITE)
        WINDOW.blit(scoretext, (380, 50))
        if pygame.time.get_ticks() % 50 == 0:
            score += 1
        
    pygame.display.update()
        



