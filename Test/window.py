# ====================================================
# Import
# ====================================================

# ======================
# Vendors
import pygame

# ======================
# Own
import game
import grille

# ====================================================
# Colors & Fonts
# ====================================================

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0, 0, 0)

# ====================================================
# Images
# ====================================================

button00 = pygame.image.load("Ressources\panel_exit.png")
button01 = pygame.image.load("Ressources\panel_play.png")

button00 = pygame.transform.scale(button00, (240, 50))
button01 = pygame.transform.scale(button01, (240, 50))

# ====================================================
# Class Definition
# ====================================================


class window:
    """
            Method class definition : used to make main object
    """
# ====================================================
# Constructors
# ====================================================

    def __init__(self, x, y):
        """
                Constructor of the method class
        """
        self.x = x
        self.y = y
        self.surface = pygame.display.set_mode((x, y))
        self.game = game.game()

    def setSize(self, x, y):
        self.x = x
        self.y = y
        self.surface = pygame.display.set_mode((x, y))

    def getSize(self):
        return (self.x, self.y)


# ====================================================
# Setters & Getters
# ====================================================

# ====================================================
# Functions
# ====================================================

    def drawMenu(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(button01, (280, 300))
        self.surface.blit(button00, (280, 500))
        pygame.display.flip()

    def showWinner(self,player):
        font = pygame.font.Font('freesansbold.ttf', 48)
        self.surface.fill((0, 0, 0)) 
        text = ('Bravo ' + str(player) + " you win!")
        textField = font.render(text, True, white)
        textRect = textField.get_rect()
        textRect.center = (400,400)         
        self.surface.blit(textField, textRect) 
        pygame.display.update()

        run = True
        while(run):
            for event in pygame.event.get():        
                if event.type == pygame.QUIT:
                    """
                            Exit input
                    """
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

    def run(self):
        pygame.init()
        pygame.display.set_caption('Fluffy Morpion')
        self.runMenu()

    def runGame(self):
        return self.game.gameExe(self.surface)

    def runMenu(self):
        run=True
        self.drawMenu()
        while(run):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    """
                            Exit input
                    """
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        x=pygame.mouse.get_pos()[0]
                        y=pygame.mouse.get_pos()[1]
                        if (280<x<520):
                            if (300<y<350):
                                res = self.runGame()
                                if res[0] :
                                    self.showWinner(res[1])
                                else :
                                    pass #drawtext
                                self.drawMenu()
                            if (500<y<550):
                                run=False                
        pygame.quit()


# ====================================================
# End
# ====================================================
