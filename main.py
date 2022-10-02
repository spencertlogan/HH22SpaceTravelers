from time import time
from tkinter.font import BOLD
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
BLUE = (50, 50, 255)
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
highscore = 0
newHighscore = False
mute = False

quitText = smallfont.render('quit' , True , WHITE) 
playText = smallfont.render('play' , True , WHITE)
tutorialText = smallfont.render('controls' , True , WHITE)
titleText = bigfont.render("Space Traveler", True, WHITE)
blurbText = scorefont.render("Travel through space while dodging debree", True, WHITE)
authorsText = smallerfont.render("Created by Christion Bradley, Spencer Logan, Sam Cole, and Revanth Myana", True, WHITE)
replayText = smallfont.render('play again' , True , WHITE)
deathText = bigfont.render("Better Luck Next Time", True, RED)
newHighscoreText = bigfont.render("NEW HIGH SCORE", True, WHITE)
#tutorial variables
inTutorialtext = bigfont.render("How to Play", True, WHITE)
gobacktext = smallfont.render("Go back to Main Menu", True, WHITE)
p1 = smallfont.render("Moves character right", True, WHITE)
p2 = smallfont.render("Moves character left", True, WHITE)
p3 = smallfont.render("Slows down time", True, WHITE)
akey = pygame.image.load("akey.png")
dkey = pygame.image.load("dkey.png")
spacekey = pygame.image.load("spacekey.png")
akey = pygame.transform.scale(akey, (50, 50))
dkey = pygame.transform.scale(dkey, (50, 50))
spacekey = pygame.transform.scale(spacekey, (170, 50))

#mute icons
mute_img = pygame.image.load("mute.png")
mute_img = pygame.transform.scale(mute_img, (50, 50))
unmute_img = pygame.image.load("unmute.png")
unmute_img = pygame.transform.scale(unmute_img, (50, 50))

#background image
spaceBackground = pygame.image.load("starryBackground.PNG").convert()
spaceBackground = pygame.transform.scale(spaceBackground, (500,600))

#initialize player variables
playerHealth = 100
playerSpeed = 0.1
playerHeight = 50
playerWidth = 50
playerXpos = (WINDOW.get_width() / 2) - (playerWidth / 2)
playerYpos = (WINDOW.get_height() / 3) - (playerHeight/2)
playerImg = pygame.image.load("Alien.png")
playerImgRed = pygame.image.load("redalien.png")
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerHeight))
playerImgRed = pygame.transform.scale(playerImgRed, (playerWidth, playerHeight))

player = classes.Player(playerXpos, playerYpos, playerHealth, playerSpeed, playerWidth, playerHeight, playerImg)

def player_collides(player, rect):
    # react - len=x | width=y
    if (rect.xpos - (rect.len)) <= player.xpos + 10 <= (rect.xpos + (rect.len)):
        if (rect.ypos - (rect.width)) <= player.ypos <= (rect.ypos + (rect.width)):
            return True
    return False

def collides(rect1, rect2):
    # fix this to be interactive
    if (rect1.xpos - rect1.len) <= rect2.xpos <= (rect1.xpos + rect1.len): 
        if (rect1.ypos - rect1.width) <= rect2.ypos <= (rect1.ypos + rect1.width):
            return True
    return False

# will calculate the speed to throw asteroid at player
def calc_speed(player, obj, time_to_impact):
    x_dist = abs(player.xpos) - abs(obj.xpos)
    y_dist = abs(player.ypos) - abs(obj.ypos)  

    x_speed = x_dist / time_to_impact
    y_speed = y_dist / time_to_impact

    #x_speed = x_speed * -1 if player.xpos < obj.xpos else x_speed
    #y_speed = y_speed * -1 if player.ypos > obj.ypos else y_speed

    return x_speed, y_speed


def bounce_obstacle(obj):
    obj.x_speed = random.uniform(-0.5, 0.5)
    obj.y_speed = random.uniform(0.1, 0.5)
    



obstacle_list = list()
health_bar = classes.Rectangle(380, 20, 100, 25)
asteroid_image = pygame.image.load("asteroid.png")
satellite_image = pygame.image.load("satellite.png")
asteroid_image = pygame.transform.scale(asteroid_image, (40, 40))
satellite_image = pygame.transform.scale(satellite_image, (30, 30))
last_collision = 0
hurt_sound1 = pygame.mixer.Sound("Hurt_sound_1.wav")
hurt_sound2 = pygame.mixer.Sound("Hurt_sound_2.wav") 
hurt_sound3 = pygame.mixer.Sound("Hurt_sound_3.wav") 
hurt_sounds = [hurt_sound1, hurt_sound2, hurt_sound3]
main_menu_music = pygame.mixer.Sound("Temp_music.wav")
main_menu_music.set_volume(0.3)
mute = False

# main loop
current_state = "menu"
running = True
aDown = False
DDown = False
spaceDown = False
boostVal = 100


SPEEDEVENT = pygame.event.custom_type()
pygame.time.set_timer(SPEEDEVENT, 1000)

while running:
    if current_state == "menu":
        if not mute:
            pygame.mixer.unpause()
            pygame.mixer.Sound.play(main_menu_music)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.pause()
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
                    pygame.quit()
                #tutorial button
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-10 <= mouse[1] <= HEIGHT/2+50: 
                    current_state = "tutorial"
                #\/ is actually the play button
                if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50:
                    pygame.mixer.stop() # stop main menu music
                    current_state = "game"
                #mute button
                if WIDTH/2-30 <= mouse[0] <= WIDTH/2+30 and HEIGHT/2+190 <= mouse[1] <= HEIGHT/2+250: 
                    if mute:
                        mute = False
                    elif not mute:
                        mute = True
        WINDOW.fill(BLACK)
        WINDOW.blit(spaceBackground, (0, 0))
        mouse = pygame.mouse.get_pos() 
        
        # DRAW THE BOXES
        #quit box
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
        #play box   
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 - 110,120,60])   
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 - 110,120,60]) 
        #tutorial box
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-10 <= mouse[1] <= HEIGHT/2+50:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 - 10,120,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 - 10,120,60]) 
        #mute box
        if WIDTH/2-30 <= mouse[0] <= WIDTH/2+30 and HEIGHT/2+190 <= mouse[1] <= HEIGHT/2+250:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 30,HEIGHT/2 + 190, 60,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 30 ,HEIGHT/2 + 190, 60,60]) 
        
        
        WINDOW.blit(titleText , (100 ,HEIGHT/2 - 220))
        WINDOW.blit(blurbText , (80,HEIGHT/2 - 155))
        WINDOW.blit(quitText , (WIDTH/2 - 30,HEIGHT/2 + 100))
        WINDOW.blit(playText , (WIDTH/2 - 30,HEIGHT/2 - 100))
        WINDOW.blit(tutorialText , (WIDTH/2 - 55,HEIGHT/2))
        WINDOW.blit(authorsText , (25,HEIGHT/2 + 280))
        if mute:
            WINDOW.blit(mute_img, (WIDTH/2 - 25 ,HEIGHT/2 + 195))
        elif not mute:
            WINDOW.blit(unmute_img, (WIDTH/2 - 24 ,HEIGHT/2 + 195))
        
        pygame.display.update()
        
    if current_state == "tutorial":
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #\/ is actually the play button
                if WIDTH/2-170 <= mouse[0] <= WIDTH/2+170 and HEIGHT/2+200 <= mouse[1] <= HEIGHT/2+260: 
                      current_state = "menu"

        WINDOW.fill(BLACK)
        mouse = pygame.mouse.get_pos() 
        
        # DRAW THE BOXES
        if WIDTH/2-170 <= mouse[0] <= WIDTH/2+170 and HEIGHT/2+200 <= mouse[1] <= HEIGHT/2+260: 
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 170,HEIGHT/2 + 200,340,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 170,HEIGHT/2 + 200,340,60]) 
        
        WINDOW.blit(inTutorialtext , (WIDTH/2 - 120 ,HEIGHT/2 - 240))
        WINDOW.blit(gobacktext , (WIDTH/2 - 160,HEIGHT/2 + 210))
        WINDOW.blit(akey, (40, 150))
        WINDOW.blit(dkey, (40, 250))
        WINDOW.blit(spacekey, (30, 350))
        WINDOW.blit(p2, (120, 160))
        WINDOW.blit(p1, (120, 260))
        WINDOW.blit(p3, (220, 360))
        
        
        pygame.display.update()
    
    if current_state == "death":
        scoreText = smallfont.render("You traveled {} lightyears!".format(score), True, WHITE)
        if (score > highscore):
            highscore = score
            newHighscore = True
        highscoreText = smallfont.render("High Score: {} lightyears".format(highscore), True, WHITE)
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
                if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2-10 <= mouse[1] <= HEIGHT/2+50: 
                    playerHealth = 100
                    playerSpeed = 0.1
                    playerHeight = 50
                    playerWidth = 50
                    playerXpos = (WINDOW.get_width() / 2) - (playerWidth / 2)
                    playerYpos = (WINDOW.get_height() / 3) - (playerHeight/2)
                    player = classes.Player(playerXpos, playerYpos, playerHealth, playerSpeed, playerWidth, playerHeight, playerImg)
                    obstacle_list = list()
                    health_bar = classes.Rectangle(380, 20, 100, 25)
                    boost_bar = classes.Rectangle(0, 20, 100, 25)
                    last_collision = 0
                    score = 0
                    aDown = False
                    DDown = False
                    spaceDown = False
                    newHighscore = False
                    current_state = "game"
                #mute button
                if WIDTH/2-30 <= mouse[0] <= WIDTH/2+30 and HEIGHT/2+190 <= mouse[1] <= HEIGHT/2+250: 
                    if mute:
                        mute = False
                    elif not mute:
                        mute = True

        mouse = pygame.mouse.get_pos() 
        
        # DRAW THE BOXES
        if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2+90 <= mouse[1] <= HEIGHT/2+150: 
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 60,HEIGHT/2 + 90,120,60]) 
            
        if WIDTH/2-90 <= mouse[0] <= WIDTH/2+90 and HEIGHT/2-10 <= mouse[1] <= HEIGHT/2+50:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 90,HEIGHT/2 - 10,180,60]) 
            
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 90,HEIGHT/2 - 10,180,60]) 
        #mute box
        if WIDTH/2-30 <= mouse[0] <= WIDTH/2+30 and HEIGHT/2+190 <= mouse[1] <= HEIGHT/2+250:
            pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 30,HEIGHT/2 + 190, 60,60]) 
        else: 
            pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 30 ,HEIGHT/2 + 190, 60,60])
        
        WINDOW.blit(quitText , (WIDTH/2 - 30,HEIGHT/2 + 100))
        WINDOW.blit(replayText , (WIDTH/2 - 70,HEIGHT/2))
        WINDOW.blit(deathText , (30,HEIGHT/2 - 210))
        WINDOW.blit(scoreText , (WIDTH/2 - 180,HEIGHT/2 - 140))
        if (newHighscore):
            WINDOW.blit(newHighscoreText, (WIDTH/2 - 180,HEIGHT/2 - 80))
        else:
            WINDOW.blit(highscoreText , (WIDTH/2 - 170,HEIGHT/2 - 80))
        if mute:
            WINDOW.blit(mute_img, (WIDTH/2 - 25 ,HEIGHT/2 + 195))
        elif not mute:
            WINDOW.blit(unmute_img, (WIDTH/2 - 24 ,HEIGHT/2 + 195))
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
                    if spaceDown:
                        player.speed *= 2.0
                    spaceDown = False
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
        if spaceDown and boostVal > 0:
            boostVal -= 0.1
            if boostVal < 0:
                boostVal = 0
        if boostVal == 0 and spaceDown:
            spaceDown = False
            player.speed *= 2.0
        elif not spaceDown and boostVal < 100:
            boostVal += 0.025
            if boostVal > 100:
                boostVal = 100

            
        #player image
        WINDOW.blit(player.img, (player.xpos, player.ypos))

        # checking for collision with player
        # makes player_collision report only one colsion
        if pygame.time.get_ticks() > (last_collision + 500) and pygame.time.get_ticks() % 100 == 0:
            for obstacle in obstacle_list:
                if player_collides(player, obstacle):
                    if not mute:
                        pygame.mixer.Sound.play(hurt_sounds[random.randint(0, 2)])
                        pygame.mixer.music.stop()
                    bounce_obstacle(obstacle)
                    last_collision = pygame.time.get_ticks()
                    player.health -= 25
        
        # Implementing Flickering
        if pygame.time.get_ticks() > 1000 and pygame.time.get_ticks() <= (last_collision + 1000): # and pygame.time.get_ticks() % 250 == 0:
            player.img = playerImgRed if player.img == playerImg else playerImg
        else:
            player.img = playerImg

        
        
        # will go across the screen and randomly create rectangles
        # len = x value | width = y value
        curr_pixel = 0
        while curr_pixel <= 500:
            
            
            upper_bound = max(10, 5000 - (score // 10))
            if random.randint(0, upper_bound) == 0:
                # curr_len = random.randint(25, 100)
                # curr_width = random.randint(25, 50)
                obstacle_image = satellite_image if random.randint(0, 2) == 0 else asteroid_image

                if random.randint(0, 10) == 0: # creating tracking asteroid
                    start_x = -20 if random.randint(0, 1) == 0 else 500
                    start_y = random.randint(0, 150) if random.randint(0, 1) == 0 else random.randint(350, 500)
                    new_rect = classes.Rectangle(start_x, start_y, 20, 20, asteroid_image)
                    new_rect.x_speed, new_rect.y_speed = calc_speed(player, new_rect, 1500)
                else:
                    new_rect = classes.Rectangle(curr_pixel, 600, 20, 20, obstacle_image)
                for obstacle in obstacle_list:
                    if collides(new_rect, obstacle): # if collides, do not add new box
                        break
                else: 
                    obstacle_list.append(new_rect)
                    curr_pixel = curr_pixel + 50 # ensures asteroids dont spawn inside one another

            curr_pixel += 25


        # moving and deleting boxes
        idx = 0
        while idx < len(obstacle_list):
            if obstacle_list[idx].x_speed and obstacle_list[idx].x_speed: # if tracking asteroid
                obstacle_list[idx].xpos += obstacle_list[idx].x_speed
                obstacle_list[idx].ypos += obstacle_list[idx].y_speed
            else: # if normal asteroid
                obstacle_list[idx].ypos -= player.speed

            
            
            
            WINDOW.blit(pygame.transform.scale(obstacle_list[idx].img, (40, 40)), (obstacle_list[idx].xpos - 10, obstacle_list[idx].ypos - 10))
            # pygame.draw.rect(WINDOW, GREY, (obstacle_list[idx].xpos, obstacle_list[idx].ypos, obstacle_list[idx].len, obstacle_list[idx].width))

            # if asteroid off screen, remove it
            if obstacle_list[idx].ypos < -20 or obstacle_list[idx].ypos > 600 or obstacle_list[idx].xpos < -20 or obstacle_list[idx].xpos > 820: # if the obstacle is off the screen, remove from list
                obstacle_list.pop(idx)
            
            idx += 1

        health_bar.len = player.health
        pygame.draw.rect(WINDOW, WHITE, (health_bar.xpos-3, health_bar.ypos-3, 106, health_bar.width+6))
        pygame.draw.rect(WINDOW, RED, (health_bar.xpos, health_bar.ypos, health_bar.len, health_bar.width))
        
        pygame.draw.rect(WINDOW, WHITE, (health_bar.xpos-3, health_bar.ypos-3+40, 106, health_bar.width+6))
        pygame.draw.rect(WINDOW, BLUE, (health_bar.xpos, health_bar.ypos+40, boostVal, health_bar.width))
        
        if player.health <= 0:
            current_state = "death"
        
        scoretext = scorefont.render("Distance: {}".format(score), True, WHITE)
        healthtext = scorefont.render("Health: {}".format(round(player.health)), True, BLACK)
        boosttext = scorefont.render("Slomo: {}".format(round(boostVal)), True, BLACK)
        WINDOW.blit(scoretext, (380, 100))
        WINDOW.blit(boosttext, (386, 62))
        WINDOW.blit(healthtext, (386, 25))
        if pygame.time.get_ticks() % 50 == 0:
            score += 1
        
    pygame.display.update()
        



