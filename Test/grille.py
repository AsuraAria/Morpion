# ====================================================
# Import
# ====================================================

# ====================================================
# Class Definition
# ====================================================

import case


class grille:
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
        self.cases = [[case.case(), case.case(), case.case()],
                      [case.case(), case.case(), case.case()],
                      [case.case(), case.case(), case.case()]]


# ====================================================
# Setters & Getters
# ====================================================


    def setCase(self, pos, content):
        """
                Set case content
        """

        self.cases[pos[0]][pos[1]].setContent(content)

    def getCase(self, pos):
        """
                Get case content
        """

        self.cases[pos[0]][pos[1]].getContent()


# ====================================================
# Functions
# ====================================================

    def clear(self):
        """
                Reset grille content
        """

        for i in self.cases:
            for j in i:
                j.clear()

    def win(self):
        """
                Detect end of game by win
        """
        for i in range(3):
            if (self.cases[i][0].getContent() == self.cases[i][1].getContent()) and (self.cases[i][1].getContent() == self.cases[i][2].getContent()) and (self.cases[i][0].getContent() != ""):
                return 1
            if (self.cases[0][i].getContent() == self.cases[1][i].getContent()) and (self.cases[1][i].getContent() == self.cases[2][i].getContent()) and (self.cases[0][i].getContent() != ""):
                return 1
        if (self.cases[0][0].getContent() == self.cases[1][1].getContent()) and (self.cases[1][1].getContent() == self.cases[2][2].getContent()) and (self.cases[1][1].getContent() != ""):
            return 1
        if (self.cases[0][2].getContent() == self.cases[1][1].getContent()) and (self.cases[1][1].getContent() == self.cases[2][0].getContent()) and (self.cases[1][1].getContent() != ""):
            return 1
        return 0

    def draw(self):
        """
                Detect end of game by draw
        """

        for i in range(3):
            for j in range(3):
                if (self.cases[i][j].getContent() != ""):
                    return 0
        return 1

# ====================================================
# End
# ====================================================
