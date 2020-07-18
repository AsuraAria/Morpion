# ====================================================
# Import
# ====================================================

import grille
import player
import pygame

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
# Class Definition
# ====================================================


class game:

    """
            Method class definition : used to make main object
    """

# ====================================================
# Constructors
# ====================================================

    def __init__(self):
        """
                Constructor of the method class
        """
        self.grille = grille.grille()
        self.playerA = player.player()
        self.playerB = player.player()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

# ====================================================
# Setters & Getters
# ====================================================

# ====================================================
# Functions
# ====================================================

    def clear(self):
        self.grille = grille.grille()
        self.playerA = player.player()
        self.playerB = player.player()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)      

    def initPlay(self, window):

        self.clear()

        self.playerA.setName("PlayerA")
        self.playerA.setIcon(icon00)
        self.playerA.setActive(True)
        self.playerB.setName("PlayerB")
        self.playerB.setIcon(icon01)
        self.playerB.setActive(False)

        window.fill((225, 225, 225))
        pygame.draw.line(window, (0, 0, 0), (0, 265), (800, 265), 10)
        pygame.draw.line(window, (0, 0, 0), (0, 535), (800, 535), 10)
        pygame.draw.line(window, (0, 0, 0), (265, 0), (265, 800), 10)
        pygame.draw.line(window, (0, 0, 0), (535, 0), (535, 800), 10)
        pygame.display.flip()


    def restart(self, window,run):
        """
                Start a new game
        """
        window.fill((225, 225, 225))
        pygame.display.flip()
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if (event.type == pygame.MOUSEBUTTONDOWN):                    
                    self.initPlay(window)
                    return True


    def pos_to_case(self,pos):

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


    def fillcase(self, case, pos, window):

        window.blit(case.getContent(), (pos[1]*270+30, pos[0]*270+30))
        pygame.display.flip()


    def gameEnd(self):
        """
                Detect end of game
        """
        win = self.win()
        draw = self.draw()
        if (win or draw):
            if (win):
                if (self.playerA.getActive()):
                    print(self.playerA.getName(), " won!")
                else:
                    print(self.playerB.getName(), " won!")
            else:
                print("It's a draw")
            print("End of game")
            return 1


    def win(self):
        """
                Detect end of game by win
        """
        for i in range(3):
            if (self.grille.cases[i][0].getContent() == self.grille.cases[i][1].getContent()) and (self.grille.cases[i][1].getContent() == self.grille.cases[i][2].getContent()) and (self.grille.cases[i][0].getContent() != ""):
                return 1
            if (self.grille.cases[0][i].getContent() == self.grille.cases[1][i].getContent()) and (self.grille.cases[1][i].getContent() == self.grille.cases[2][i].getContent()) and (self.grille.cases[0][i].getContent() != ""):
                return 1
        if (self.grille.cases[0][0].getContent() == self.grille.cases[1][1].getContent()) and (self.grille.cases[1][1].getContent() == self.grille.cases[2][2].getContent()) and (self.grille.cases[1][1].getContent() != ""):
            return 1
        if (self.grille.cases[0][2].getContent() == self.grille.cases[1][1].getContent()) and (self.grille.cases[1][1].getContent() == self.grille.cases[2][0].getContent()) and (self.grille.cases[1][1].getContent() != ""):
            return 1
        return 0


    def draw(self):
        """
                Detect end of game by draw
        """

        for i in range(3):
            for j in range(3):
                if (self.grille.cases[i][j].getContent() != ""):
                    print("FLAG",i,j,self.grille.cases[i][j].getContent())
                else:
                    return 0
        return 1

# ====================================================
# Game loop
# ====================================================

    def gameExe(self, window):

        self.initPlay(window)
        activePlayer, waitingPlayer = self.playerA,self.playerB
        run = True

        while run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    """
                            Exit input
                    """
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(activePlayer.getName(), waitingPlayer.getName())
                    """
                            Mouse input
                    """
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        """
                                Right button input
                        """
                        caseNumbers = self.pos_to_case(pygame.mouse.get_pos())
                        currentCase = self.grille.cases[caseNumbers[0]
                                                        ][caseNumbers[1]]

                        if (currentCase.getContent() == ""):
                            """
                                    Case not occupied
                            """
                            currentCase.setContent(activePlayer.getIcon())
                            self.fillcase(currentCase, caseNumbers, window)
                            if (self.gameEnd()):
                                run=self.restart(window,run)
                            else:
                                if(self.playerA.getActive()):
                                    self.playerA.setActive(False)
                                    self.playerB.setActive(True)
                                else:
                                    self.playerB.setActive(False)
                                    self.playerA.setActive(True)                                    
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
                        run=self.restart(window,run)
        pygame.quit()

# ====================================================
# End
# ====================================================
