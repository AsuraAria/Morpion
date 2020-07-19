# ====================================================
# Import
# ====================================================

#======================
# Vendors
import pygame

#======================
# Own
import game
import grille

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

    def run(self):
        pygame.init()
        pygame.display.set_caption('Fluffy Morpion')
        self.game.gameExe(self.surface)

# ====================================================
# End
# ====================================================
