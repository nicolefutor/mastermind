import pygame
import random

width_of_window = 700
height_of_window = 750

pygame.init()
screen = pygame.display.set_mode((width_of_window,height_of_window))

def generateSolution():
    solution = []
    colors = ["R", "O", "Y", "G", "B", "V"]
    solution.append(colors[random.randint(0,5)])
    solution.append(colors[random.randint(0,5)])
    solution.append(colors[random.randint(0,5)])
    solution.append(colors[random.randint(0,5)])
    return solution

def checkGuess(guess, solution):
    accuracy = []
    for i in range(0, len(guess)):
        if solution[i] == guess[i]:
            accuracy.append("C")
        else:
            accuracy.append("I")
    for i in range(0, len(guess)):
        if not accuracy[i]=="C":
            for j in range(0, len(solution)):
                if (not accuracy[j]=="C") and solution[j] == guess[i]:
                    accuracy[i] = "K"  
    result = []
    corrects = accuracy.count("C")
    incorrects = accuracy.count("I")
    wrongSpots = accuracy.count("K")
    for i in range(0, corrects):
        result.append("C")
    for i in range(0, wrongSpots):
        result.append("K")
    for i in range(0, incorrects):
        result.append("I")
    return result                   


def addToFour(guess, color):
    if len(guess) >= 4:
        return guess
    else:
        guess.append(color)
    print(guess)
    return guess





# set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 153, 153)
orange = (255,204,153)
yellow = (255,255,153)
green = (204,255,153)
blue = (153,204,255)
purple = (204,153,255)

def returnColor(circleColor):
    if circleColor == 'R':
        color = red
    elif circleColor == 'O':
        color = orange
    elif circleColor == 'Y':
        color = yellow
    elif circleColor == 'G':
        color = green
    elif circleColor == 'B':
        color = blue
    elif circleColor == 'V':
        color = purple
    return color


pygame.display.set_caption("Mastermind")

rows = 10
columns = 4
gameboard = []
accuracies = []

currentRow = []

solution = generateSolution()

running  = True
while running:
    # Check for event if user has pushed 
    # any event in queue 
    for event in pygame.event.get(): 
        # screen background color
        screen.fill(white)
        
        #Render the title at the top of the screen
        font = pygame.font.Font(None, 90)
        text = font.render('Mastermind', True, black)
        titlePos = (175, 15)
        screen.blit(text, titlePos)

        #render buttons
        #Check button
        check = pygame.draw.rect(screen, black, pygame.Rect(100, 400, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('Check', True, black)
        titlePos = (132, 410)
        screen.blit(text, titlePos)

        #Clear button
        clear = pygame.draw.rect(screen, black, pygame.Rect(100, 450, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('Clear', True, black)
        titlePos = (135, 460)
        screen.blit(text, titlePos)

        #New game button
        newGame = pygame.draw.rect(screen, black, pygame.Rect(100, 500, 120, 40), 2)
        font = pygame.font.Font(None, 30)
        text = font.render('New Game', True, black)
        titlePos = (110, 510)
        screen.blit(text, titlePos)

        #Red button
        redButton = pygame.draw.circle(screen, black, (125, 150), 17, 2)
        pygame.draw.circle(screen, red, (125, 150), 15)

        #Orange button
        orangeButton = pygame.draw.circle(screen, black, (190, 150), 17, 2)
        pygame.draw.circle(screen, orange, (190, 150), 15)

        #Yellow button
        yellowButton = pygame.draw.circle(screen, black, (125, 225), 17, 2)
        pygame.draw.circle(screen, yellow, (125, 225), 15)

        #Green button
        greenButton = pygame.draw.circle(screen, black, (190, 225), 17, 2)
        pygame.draw.circle(screen, green, (190, 225), 15)

        #Blue button
        blueButton = pygame.draw.circle(screen, black, (125, 300), 17, 2)
        pygame.draw.circle(screen, blue, (125, 300), 15)

        #Purple button
        purpleButton = pygame.draw.circle(screen, black, (190, 300), 17, 2)
        pygame.draw.circle(screen, purple, (190, 300), 15)

        #Render the game board
        for rowCount in range(10):
            for columnCount in range(4):
                center = (columnCount * 40 + 350, rowCount * 40 + 150)
                pygame.draw.circle(screen, black, (center), 17, 2)

        #render the colored circles from the gameboard
        for rowCount in range(len(gameboard)):
            for columnCount in range(4):
                center = (columnCount * 40 + 350, rowCount * 40 + 150)

                circleColor = gameboard[rowCount][columnCount]
                
                color = returnColor(circleColor)

                pygame.draw.circle(screen, color, (center), 15)

        #Render the current row
        for columnCount in range(len(currentRow)):
            center = (columnCount * 40 + 350, len(gameboard) * 40 + 150)
            color = returnColor(currentRow[columnCount])
            pygame.draw.circle(screen, color, (center), 15)
                
        #Render the pin board
        for rowCount in range(10):
            for columnCount in range(2):
                center1 = (columnCount * 20 + 550, rowCount * 20 + 240)
                pygame.draw.circle(screen, black, (center1), 6, 2)
                center2 = (columnCount * 40 + 550, rowCount * 40 + 240)
                pygame.draw.circle(screen, black, (center2), 6, 2)
        
        pygame.display.update()
        # if event is of type quit then  
        # set running bool to false 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if redButton.collidepoint((x,y)):
                currentRow = addToFour(currentRow, "R")
            if orangeButton.collidepoint((x,y)):
                currentRow = addToFour(currentRow, "O")
            if yellowButton.collidepoint((x,y)):
                currentRow = addToFour(currentRow, "Y")
            if greenButton.collidepoint((x,y)):
                currentRow = addToFour(currentRow, "G")
            if blueButton.collidepoint((x, y)):
                currentRow = addToFour(currentRow, "B")
            if purpleButton.collidepoint((x,y)):
                currentRow = addToFour(currentRow, "V")           
            if check.collidepoint((x,y)):
                accuracies.append(checkGuess(currentRow, solution))
                gameboard.append(currentRow)
                print(solution)
                print(gameboard)
                print(accuracies)
                currentRow = []
            if clear.collidepoint((x,y)):
                currentRow = []
            if newGame.collidepoint((x,y)):
                currentRow = []
                gameboard = []
                accuracies = []
                solution = []

        # update screen
        pygame.display.flip()

pygame.quit()

