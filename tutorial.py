import pygame
import classes

pygame.init()
WINDOW = pygame.display.set_mode((500, 600))
BLACK = (0, 0, 0)
WHITE = (255,255,255) 
# menu button colors 
button_light = (170,170,170) 
button_dark = (100,100,100)
WIDTH = WINDOW.get_width()
HEIGHT = WINDOW.get_height()
# defining a font 
smallfont = pygame.font.SysFont('Corbel',25)
bigfont = pygame.font.SysFont('Corbel',50) 

inTutorialtext = bigfont.render("How to Play", True, WHITE)
gobacktext = smallfont.render("Go back to Main Menu", True, WHITE)
p1 = smallfont.render("Moves character right as it is held", True, WHITE)
p2 = smallfont.render("Moves character left as it is held", True, WHITE)
p3 = smallfont.render("Boosts character as it is held", True, WHITE)

akey = pygame.image.load("akey.png")
dkey = pygame.image.load("dkey.png")
spacekey = pygame.image.load("spacekey.png")
akey = pygame.transform.scale(akey, (50, 50))
dkey = pygame.transform.scale(dkey, (50, 50))
spacekey = pygame.transform.scale(spacekey, (170, 50))

while True:
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #\/ is actually the play button
            if WIDTH/2-60 <= mouse[0] <= WIDTH/2+60 and HEIGHT/2-110 <= mouse[1] <= HEIGHT/2-50: 
                pygame.quit()  

    WINDOW.fill(BLACK)
    mouse = pygame.mouse.get_pos() 
    
    # DRAW THE BOXES
    if WIDTH/2-200 <= mouse[0] <= WIDTH/2+40 and HEIGHT/2+200 <= mouse[1] <= HEIGHT/2+245: 
        pygame.draw.rect(WINDOW, button_light,[WIDTH/2 - 200,HEIGHT/2 + 200,240,45]) 
    else: 
        pygame.draw.rect(WINDOW, button_dark,[WIDTH/2 - 200,HEIGHT/2 + 200,240,45]) 
        
    
    
    WINDOW.blit(inTutorialtext , (100 ,HEIGHT/2 - 220))
    WINDOW.blit(gobacktext , (WIDTH/2 - 170,HEIGHT/2 + 210))
    WINDOW.blit(akey, (80, 150))
    WINDOW.blit(dkey, (80, 250))
    WINDOW.blit(spacekey, (30, 350))
    WINDOW.blit(p2, (150, 160))
    WINDOW.blit(p1, (150, 270))
    WINDOW.blit (p3, (220, 370))
    
    
    pygame.display.update()