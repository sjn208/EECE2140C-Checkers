# Jasmine Sajna
# Final Project - Game of Checkers
import numpy as np

# player 1 = ♛🔴 goes first
# player 2 = ♔⚾

pl, plking, opp, oppking, allowed = ' 🔴 ', ' ♛ ', ' ⚾ ', ' ♔ ', 1
prevpl, prevplk, prevo, prevok, prevall = ' ⚾ ', ' ♔ ', ' 🔴 ', ' ♛ ', -1

count1 = 12
count2 = 12

grid = np.full((8, 8), '    ')  # 8x8 empty board


def show_board(board):
    """displays array (board) as a more clear board"""
    print('\n===============CURRENT BOARD===============')
    print('    C  1 　 2 　 3　   4　  5　   6　  7　  8')
    print('R   ┏—–——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┳—‐——┓')
    for row in range(8):
        print(row + 1, '  │', end=' ')
        for node in board[row]:
            print(node, '│', end=' ')
        print()
        if row != 7:
            print('    ┣—–——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——╋—‐——┫')
    print('    ┗—–——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┻—‐——┛')


def initialize_board(board):
    """function to reset board"""
    for i in range(8):
        for j in range(3):  # Player 🔴 on first half of board
            if (i + j) % 2 == 1:
                board[i][j] = ' 🔴 '

        for j in range(5, 8):  # player ⚾ on second half of board
            if (i + j) % 2 == 1:
                board[i][j] = ' ⚾ '


def get_piece(board, player, playerkingpc, opp, oppking, allowed):
    """function to check if a selected piece is valid
    :param board: numpy array of grid
    :param player: string of player 🔴 or ⚾
    :param playerkingpc: string of the king version of player
    :param opp: opponent string
    :param oppking: opponent's king string
    :param allowed: int (1 or -1), represents how player can move through board's columns
    """
    value = False
    while not value:
        try:
            print(f"****Player {player}'s turn****")
            piece = input('Select piece (R,C): ')
            row = int(piece[1]) - 1
            col = int(piece[3]) - 1
            marker = board[row][col]  # gets the string in place at chosen spot
            if marker != player and marker != playerkingpc:
                print(f'{piece} is not your piece! Enter again!')
                print(f'marker is {marker}, player is {player}')
                continue
            else:  # condition that the selected piece is the player's
                board[row][col] = '    '   # clear the position
                value = True
        except:
            TypeError("Enter valid type for piece location!")

    playerking = marker == playerkingpc  # true or false value based on if chosen piece is a king
    move_piece(board, marker, playerking, opp, oppking, row, col, allowed)  # begins moving piece when selected is ok


def move_piece(board, player, playerking, opp, oppking, srow, scol, allowed):
    """function to change a node to a piece, all parameters are same as get_piece except for below:
    :param player: string of selected piece (can be king)
    :param playerking: True or False (is piece a king)
    :param srow: int selected piece row
    :param scol: int selected piece column
    """

    value = False
    while not value:   # loop that breaks when move position is considered valid
        try:
            spot = input('Move to (R,C): ')
            mrow = int(spot[1]) - 1
            mcol = int(spot[3]) - 1
            move = board[mrow][mcol]
            if move != '    ' and (mcol-scol) == allowed:  # if move spot not empty
                print(f'Position {spot} taken! Try again!')
                continue
            else:
                if abs(srow - mrow) == 1:  # if player is moving only 1 spot away
                    # check if direction of move is valid (kings go both ways, originals go only in allowed direction)
                    if (mcol - scol) == allowed or (abs(mcol - scol) == 1 and playerking):
                        board[mrow][mcol] = player  # valid, so change position to hold piece
                        value = True
                    else:
                        print('Not valid movement!')
                        continue
                elif abs(srow - mrow) == 2:  # if player is trying to make a jump
                    # check direction considering king or not
                    if (mcol - scol) == (2 * allowed) or (abs(mcol - scol) == 2 and playerking):
                        midrow = (srow + mrow) // 2
                        midcol = (scol + mcol) // 2
                        btwn = board[midrow][midcol]
                        if btwn == opp or btwn == oppking:  # compares piece being jumped over to check if opponent
                            board[mrow][mcol] = player
                            delete_piece(board, opp, midrow, midcol)  # delete fn to remove the opponent's piece

                            value = True
                        else:
                            print('Invalid Jump!')  # the jump is not over opponent piece
                            continue
                else:
                    print('NOT A POSITION')  # player tries to make jump larger than 2
        except TypeError as e:
            print(str(e))
            print('Invalid!')
    check_king(board, mrow, mcol, allowed)


def delete_piece(board, player, row, col):
    """function to empty a position at node (called when jumped over), and lower register count of pieces
    :param board: grid array
    :param player: string at current spot
    :param row: int row of jumped piece
    :param col: int col of jumped piece
    """
    global count1
    global count2
    board[row][col] = '    '  # clears position
    # adjust the count of pieces
    if player == ' 🔴 ' or player == ' ♛ ':
        count1 = count1 - 1
    elif player == ' ⚾ ' or player == ' ♔ ':
        count2 = count2 - 1


def check_win():
    """Function to check if board is all one player
    :return: True or Falase
    """
    global count1
    global count2
    if count1 == 0:
        print('Player  ⚾  Won!')
        return True
    elif count2 == 0:
        print('Player  🔴  Won!')
        return True
    else:
        return False


def check_king(board, row, col, allowed):
    """ function to check if a piece has reached the opposite edge
    :param board: grid array
    :param row: int row of piece
    :param col: int col of piece
    :param allowed: int -1 or 1 to identify which piece to make king
    """
    if allowed == -1 and col == 0:
        board[row][col] = ' ♔ '
    if allowed == 1 and col == 7:
        board[row][col] = ' ♛ '


initialize_board(grid)
win = False
while not win:  # main loop to alternate turns

    show_board(grid)
    get_piece(grid, pl, plking, opp, oppking, allowed)

    # switching previous player components to current player
    temppl, templk, tempopp, tempok, tempall = pl, plking, opp, oppking, allowed
    pl, plking, opp, oppking, allowed = prevpl, prevplk, prevo, prevok, prevall
    prevpl, prevplk, prevo, prevok, prevall = temppl, templk, tempopp, tempok, tempall
    win = check_win()

