# main script
from players import Red, Black
from board import Board
from spaces import Node

def select_pc(player, board, opp):
    """function to check if a selected piece is valid
    :param player: class type Red or Black
    :param board: class type Board
    :param opp: class type of opponent (Red or Black)
    """
    select = False
    # creates a loop until the selected piece is valid
    while not select:
        try:
            print(f"****Player {player.name}'s turn****")
            piece = input('Select piece "(R,C)": ')
            srow = int(piece[1]) - 1
            scol = int(piece[3]) - 1

            # call function to check if type at selected spot is player's
            if not correct_sel(player, board.grid, srow, scol):
                print(f'{piece} is not your piece! Enter again!')
                continue
            elif board.check_movable(srow, scol, opp):  # uses board method to check that piece can move
                select = True

        except ValueError:  # case that user enter invalid type ex: (j,s)
            print('Invalid input type!')

    mrow, mcol = move_pc(board, srow, scol, opp)
    board.move_pc(srow, scol, mrow, mcol)

def move_pc(board, srow, scol, opp):
    """ function to check if move position spot is valid
    :param board: type Board
    :param srow: int of current spot's row
    :param scol: int of current spot's col
    :param opp: opponent's type (Red or Black)
    :return: mrow, mcol - int of chosen move spot row and column
    """
    moved = False
    crowned = board.grid[srow][scol].crowned
    allowed = board.grid[srow][scol].allowed

    # loop to confirm that move position is valid
    while not moved:
        try:
            # grab move spot from user
            spot = input('Move to "(R,C)": ')
            mrow = int(spot[1]) - 1
            mcol = int(spot[3]) - 1

            if not correct_sel(Node, board.grid, mrow, mcol):  # if move spot not empty (not Node type at spot)
                print(f'Position {spot} taken! Try again!')
                continue
            elif abs(srow - mrow) == 1:  # if player is trying to move only directly next to selected spot
                if (mcol - scol) == allowed or (abs(mcol - scol)==1 and crowned):  # check direction is allowed
                    return mrow, mcol
                else:
                    print('Invalid jump!')
                    continue
            elif abs(srow-mrow) == 2:  # player is trying to jump over another piece
                if (mcol - scol) == (2*allowed) or (abs(mcol - scol) == 2 and crowned):  # check if direction is allowed
                    jrow = (srow + mrow) // 2
                    jcol = (scol + mcol) // 2
                    if correct_sel(opp, board.grid, jrow, jcol):  # check if the jumped over piece is the opponent's
                        board.delete_pc(jrow, jcol)
                        return mrow, mcol
                    else:  # piece is not opponents
                        print('Invalid Jump!')
                        continue
            else:
                print('NOT A POSITION')
        except ValueError:
            print('Invalid input type!')


def correct_sel(expected_type, grid, row, col):
    """ function for checking if a spot is the piece type it needs to be
    :param expected_type:  type Red, Black, or Node
    :param grid: type Board, of grid
    :param row: int of row
    :param col: int of col
    :return: True or False (that piece is correct)
    """
    if type(grid[row][col]) == expected_type:
        return True
    else:
        return False

boards = Board()
boards.initialize_board()
player = Red
opp = Black

win = False
while not win:
    boards.show_board()
    select_pc(player, boards, opp)  # get player to choose piece, which calls move piece methods and functions

    player, opp = opp, player  # switch off current player and opponent
    win = boards.check_win()