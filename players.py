# Jasmine Sajna - players.py
from spaces import Piece


class Black(Piece):
    """class for representing black's pieces"""
    name = '⚾'

    def __init__(self, x, y):
        self.allowed = -1  # forwards direction is when columns decrease
        super().__init__(x, y, self.allowed, False)  # starts off as just a regular pc
        self.picture = ' ⚾ '

    def __str__(self):
        return self.picture

    def check_crown(self):
        """method for checking when a piece reaches the edge"""
        if self.col == 0:  # 0 col is the left edge (opposite) end of the board
            self.picture = ' ♔ '
            self.crowned = True


class Red(Piece):
    """class for representing red's pieces"""
    name = '🔴'

    def __init__(self, x, y):
        self.allowed = 1  # forwards direction is when columns increase
        super().__init__(x, y, self.allowed, False)  # starts off as regular pc
        self.picture = ' 🔴 '

    def __str__(self):
        return self.picture

    def check_crown(self):
        """method to check when pc reaches edge"""
        if self.col == 7:  # 7 is right-most col opposite end of red's start
            self.picture = ' ♛ '
            self.crowned = True


