# ====================================================
# Import
# ====================================================

import pygame
import grille
import player

# ====================================================
# Images
# ====================================================

icon00 = pygame.image.load("Ressources\icon00.png")
icon01 = pygame.image.load("Ressources\icon01.png")
icon02 = pygame.image.load("Ressources\icon02.png")
icon03 = pygame.image.load("Ressources\icon03.png")
icon04 = pygame.image.load("Ressources\icon04.png")

icon00 = pygame.transform.scale(icon00, (200, 200))
icon01 = pygame.transform.scale(icon01, (200, 200))
icon02 = pygame.transform.scale(icon02, (200, 200))
icon03 = pygame.transform.scale(icon03, (200, 200))
icon04 = pygame.transform.scale(icon04, (200, 200))


# ====================================================
# Functions
# ====================================================


def pos_to_case(pos):

    case = [0, 0]

    if pos[1] <= 260:
        case[0] = 0
    elif 270 <= pos[1] <= 530:
        case[0] = 1
    elif 540 <= pos[1]:
        case[0] = 2
    else:
        return [0, 0]

    if pos[0] <= 260:
        case[1] = 0
    elif 270 <= pos[0] <= 530:
        case[1] = 1
    elif pos[0] >= 540:
        case[1] = 2
    else:
        return [0, 0]

    return case


def fillcase(case, pos):

    window.blit(case.getContent(), (pos[1]*270+30, pos[0]*270+30))
    pygame.display.flip()


def initPlay():

    window.fill((225, 225, 225))
    pygame.draw.line(window, (0, 0, 0), (0, 265), (800, 265), 10)
    pygame.draw.line(window, (0, 0, 0), (0, 535), (800, 535), 10)
    pygame.draw.line(window, (0, 0, 0), (265, 0), (265, 800), 10)
    pygame.draw.line(window, (0, 0, 0), (535, 0), (535, 800), 10)
    pygame.display.flip()

def checkstate(game):
    """
            Detect end of game
    """
    win = game.win()
    draw = game.draw()
    if (win or draw):
        if (win):
            print(activePlayer," won!")
        print("End of game")
        restart()


def restart():
    """
            Start a new game
    """
    rerun = True
    window.fill((225, 225, 225))
    pygame.display.flip()
    while(rerun):
        clock.tick(60)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rerun = False            
            if (event.type == pygame.MOUSEBUTTONDOWN):
                rerun = False                
    initPlay()


def show():
    print("     0)  1)  2)")
    for i in range(3):
        print("\n   -------------")
        for j in range(3):
            print(game.cases[i][j].getContent(), end="")
    print("\n   -------------\n")

# ====================================================
# Execution
# ====================================================

pygame.init()
pygame.display.set_caption('Fluffy Morpion')
window = pygame.display.set_mode((800, 800))
initPlay()

game = grille.grille()

playerA = player.player()
playerB = player.player()

playerA.setName("A")
playerB.setName("B")
playerA.setIcon(icon00)
playerB.setIcon(icon01)

activePlayer = playerA
waitingPlayer = playerB

print("activePlayer is ",activePlayer)
print("waitingPlayer is ",waitingPlayer)




# ====================================================
# Game loop
# ====================================================

run = True
clock = pygame.time.Clock()
show()

while run:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            """
                    Exit input
            """
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            """
                    Mouse input
            """       
            if pygame.mouse.get_pressed() == (1, 0, 0):
                """
                        Right button input
                """
                caseNumbers = pos_to_case(pygame.mouse.get_pos())
                currentCase=game.cases[caseNumbers[0]][caseNumbers[1]]

                if (currentCase.getContent() == ""):
                    """
                            Case not occupied
                    """
                    currentCase.setContent(activePlayer.getIcon())
                    fillcase(currentCase,caseNumbers)
                    show()
                    checkstate(game)
                    activePlayer, waitingPlayer = waitingPlayer, activePlayer
                else:
                    """
                            Case already occupied
                    """
                    print("Case occupied")


            if (pygame.mouse.get_pressed() == (0, 0, 1)):
                """
                        Left button input
                """
                restart()
pygame.quit()

# ====================================================
# End
# ====================================================
