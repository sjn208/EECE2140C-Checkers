from piece import Piece


class Black(Piece):
    name = '⚾'

    def __init__(self, x, y):
        self.allowed = -1
        super().__init__(x, y, self.allowed, False)
        self.picture = ' ⚾ '


    def __str__(self):
        return self.picture

    def check_crown(self):
        if self.col == 0:
            self.picture = ' ♔ '
            self.crowned = True




