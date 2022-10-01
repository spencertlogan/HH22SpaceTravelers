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
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont('Corbel',50) 
# rendering a text written in 
# this font 
quitText = smallfont.render('quit' , True , WHITE) 
playText = smallfont.render('play' , True , WHITE)
titleText = bigfont.render("Untitled game", True, WHITE)

while True: 
      
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
                pygame.quit()  

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
