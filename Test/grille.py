# ====================================================
# Import
# ====================================================

# ====================================================
# Class Definition
# ====================================================

#======================
# Own
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

# ====================================================
# End
# ====================================================
