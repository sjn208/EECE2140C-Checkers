# Jasmine Sajna - board.py

from spaces import Node
from players import Red, Black


class Board:
    """class to create a 2d list board for all pieces"""

    def __init__(self):
        # track number of reds/blacks to check when one is 0
        self.red_pcs = 12
        self.black_pcs = 12
        self.grid = [[Node() for x in range(8)] for y in range(8)]  # 'empty' list of Nodes

    def initialize_board(self):
        """ method to set the initial placements of all pieces"""
        for i in range(8):
            for j in range(3):  # Player 🔴 on first half of board
                if (i + j) % 2 == 1:
                    self.grid[i][j] = Red(i, j)

            for j in range(5, 8):  # player ⚾ on second half of board
                if (i + j) % 2 == 1:
                    self.grid[i][j] = Black(i, j)

    def show_board(self):
        """method to print the 2d list as a board"""
        print('\n===============CURRENT BOARD===============')
        print('    C  1 　 2 　 3　   4　  5　   6　  7　  8')
        print('R   ┏—–——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┓')
        for row in range(8):
            print(row + 1, '  │', end=' ')
            for node in self.grid[row]:
                print(node, '│', end=' ')
            print()
            if row != 7:
                print('    ┣—–——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——┫')
        print('    ┗—–——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┛')

    def move_pc(self, srow, scol, mrow, mcol):
        """method to switch pieces from a selected spot to a new spot (only called when selected and moved are valid)
        :param srow: int of selected row
        :param scol: int of selected col
        :param mrow: int of move position row
        :param mcol: int of move position col
        """
        # adjust the row and col of the piece from the board
        self.grid[srow][scol].row = mrow
        self.grid[srow][scol].col = mcol

        # make moved spot on board the piece that was selected & adjust if reached end to crowned
        self.grid[mrow][mcol] = self.grid[srow][scol]
        self.grid[mrow][mcol].check_crown()
        self.grid[srow][scol] = Node()  # make old moved piece as a node

    def delete_pc(self, row, col):
        """method to delete a piece after it has been jumped over
        :param row: int row of pc to delete
        :param col: int col of pc to delete
        """
        player = type(self.grid[row][col])  # check the type of piece being deleted

        # adjust counts of pieces
        if player == Red:
            self.red_pcs -= 1
        elif player == Black:
            self.black_pcs -= 1
        self.grid[row][col] = Node()  # make deleted piece 'empty'

    def check_win(self):
        """ method to check if game has been won--one player's pieces are all gone
        :return: True or False
        """
        if self.red_pcs == 0:
            print('\n****Black Won!!!****')
            return True
        elif self.black_pcs == 0:
            print('\n****Red Won!!!*****')
            return True
        else:
            return False  # neither's pieces are at 0 - noone has won

    def check_movable(self, row, col, opp):
        """method to check if a piece can be moved
        :param row: int row of selected piece
        :param col: int col of selected piece
        :param opp: type Red or Black of opponent
        :return: True or False (that piece can move)
        """
        possible_moves = []  # list of tuples of possible spots to move a piece to
        crowned = self.grid[row][col].crowned  # true or false if piece is crowned
        allowed = self.grid[row][col].allowed  # 1 or -1 for direction pc can move
        double = 2 * allowed  # max size

        # go through all 8 spots around the selected spot (4 areas for jumps), (4 areas directly next to)
        try:  # using try in case position is at an edge -- meaning that row-1,col-1... does not exist
            if type(self.grid[row - 1][col - allowed]) == opp and type(
                    self.grid[row - 2][col - double]) == Node and crowned:
                possible_moves.append(((row - 1), (col - double + 1)))  # add the possible move to the list
        except:
            pass
        try:
            if type(self.grid[row + 1][col - allowed]) == opp and type(
                    self.grid[row + 2][col - double]) == Node and crowned:
                possible_moves.append(((row + 3), (col - double + 1)))
        except:
            pass
        try:
            if type(self.grid[row - 1][col + allowed]) == opp and type(self.grid[row - 2][col + double]) == Node:
                possible_moves.append(((row - 1), (col + double + 1)))
        except:
            pass
        try:
            if type(self.grid[row + 1][col + allowed]) == opp and type(self.grid[row + 2][col + double]) == Node:
                possible_moves.append(((row + 3), (col + double + 1)))
        except:
            pass

        try:
            if type(self.grid[row - 1][col - allowed]) == Node and crowned:
                possible_moves.append(((row), (col - allowed + 1)))
        except:
            pass

        try:
            if type(self.grid[row + 1][col - allowed]) == Node and crowned:
                possible_moves.append(((row + 2), (col - allowed + 1)))
        except:
            pass

        try:
            if type(self.grid[row - 1][col + allowed]) == Node:
                possible_moves.append(((row), (col + allowed + 1)))
        except:
            pass

        try:
            if type(self.grid[row + 1][col + allowed]) == Node:
                possible_moves.append(((row + 2), (col + allowed + 1)))
        except:
            pass

        print(f'Possible moves: {possible_moves}')
        if len(possible_moves) > 0:  # if no moves, moveable is false
            return True
        else:
            return False
