
class Piece():

    def __init__(self, x, y, allowed, crowned):
        self.row = x
        self.col = y
        self.allowed = allowed
        self.crowned = crowned

    def move_pc(self, x, y):
        self.row = x
        self.col = y

