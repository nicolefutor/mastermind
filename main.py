import pygame

width_of_window = 700
height_of_window = 750

pygame.init()
screen = pygame.display.set_mode((width_of_window,height_of_window))

# set colors
white = (255, 255, 255)
black = (0, 0, 0)

# screen background color
screen.fill(white)

pygame.display.set_caption("Mastermind")

gameboard = []

running  = True
while running:
    # Check for event if user has pushed 
    # any event in queue 
    for event in pygame.event.get(): 
        #Render the title at the top of the screen
        #change color later
        # font = pygame.font.Font('debrosee.ttf', 90)
        font = pygame.font.Font(None, 90)
        text = font.render('Mastermind', True, black)
        titlePos = (175, 15)
        screen.blit(text, titlePos)

        #render buttons
        #Check button
        pygame.draw.rect(screen, black, pygame.Rect(100, 400, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('Check', True, black)
        titlePos = (125, 410)
        screen.blit(text, titlePos)

        #Clear button
        pygame.draw.rect(screen, black, pygame.Rect(100, 450, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('Clear', True, black)
        titlePos = (135, 460)
        screen.blit(text, titlePos)

        #New game button
        pygame.draw.rect(screen, black, pygame.Rect(100, 500, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('New Game', True, black)
        titlePos = (110, 510)
        screen.blit(text, titlePos)

        pygame.display.update()
        # if event is of type quit then  
        # set running bool to false 
        if event.type == pygame.QUIT: 
            running = False

        # update screen
        pygame.display.flip()

pygame.quit()

