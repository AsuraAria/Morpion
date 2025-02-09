# ====================================================
# Import
# ====================================================

# ====================================================
# Class Definition
# ====================================================

class player:

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
        self.name = ""
        self.icon = ""
        self.active = False

# ====================================================
# Setters & Getters
# ====================================================

    def setName(self, newname):
        self.name = newname

    def getName(self):
        return self.name

    def setIcon(self, newicon):
        self.icon = newicon

    def getIcon(self):
        return self.icon

    def setActive(self, Bool):
        self.active = Bool

    def getActive(self):
        return self.active

# ====================================================
# Functions
# ====================================================

# ====================================================
# End
# ====================================================
