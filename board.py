
from node import Node
from red import Red
from black import Black

class Board:
    def __init__(self):
        self.red_pcs = 12
        self.black_pcs = 12
        self.grid = [[Node() for x in range(8)] for y in range(8)]

    def initialize_board(self):
        for i in range(8):
            for j in range(3):  # Player 🔴 on first half of board
                if (i + j) % 2 == 1:
                    self.grid[i][j] = Red(i, j)

            for j in range(5, 8):  # player ⚾ on second half of board
                if (i + j) % 2 == 1:
                    self.grid[i][j] = Black(i, j)

    def show_board(self):
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
        self.grid[srow][scol].row = mrow
        self.grid[srow][scol].col = mcol
        self.grid[mrow][mcol] = self.grid[srow][scol]
        self.grid[mrow][mcol].check_crown()
        self.grid[srow][scol] = Node()

    def delete_pc(self, row, col):
        player = type(self.grid[row][col])
        if player == Red:
            self.red_pcs -= 1
        elif player == Black:
            self.black_pcs -= 1
        self.grid[row][col] = Node()

    def check_win(self):
        if self.red_pcs == 0:
            print('Black Won!')
            return True
        elif self.black_pcs == 0:
            print('Red Won!')
            return True
        else:
            return False






