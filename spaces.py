# Jasmine Sajna - spaces.py

class Piece:
    """class for a piece on the board either red or black"""
    def __init__(self, x, y, allowed, crowned):
        self.row = x
        self.col = y
        self.allowed = allowed  # will be -1 or 1, for direction that a piece can move through columns
        self.crowned = crowned  # if at edge


class Node:
    """class for representing an empty spot on the board"""
    def __init__(self):
        self.picture = '    '  # visual of empty space that fits the size of the board

    def __str__(self):
        return self.picture
