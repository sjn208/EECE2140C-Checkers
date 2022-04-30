# main script
from red import Red
from black import Black
from board import Board
from node import Node

def select_pc(player, board, opp):
    # print(f'sel type board = {type(board)}')
    select = False
    while not select:
        try:
            print(f"****Player {player.name}'s turn****")
            piece = input('Select piece (R,C): ')
            srow = int(piece[1]) - 1
            scol = int(piece[3]) - 1
            # print(board.grid[srow][scol], ' is what u chose')
            if not correct_sel(player, board.grid, srow, scol):
                print(f'{piece} is not your piece! Enter again!')
                continue
            else:
                select = True
        except ValueError as e:
            print(str(e))

    mrow, mcol = move_pc(board, srow, scol, opp)
    board.move_pc(srow, scol, mrow, mcol)

def move_pc(board, srow, scol, opp):
    moved = False
    crowned = board.grid[srow][scol].crowned
    allowed = board.grid[srow][scol].allowed

    while not moved:
        try:
            spot = input('Move to (R,C): ')
            mrow = int(spot[1]) - 1
            mcol = int(spot[3]) - 1
            if not correct_sel(Node, board.grid, mrow, mcol):  # if move spot not empty
                print(f'Position {spot} taken! Try again!')
                continue
            elif abs(srow - mrow) == 1:
                if (mcol - scol) == allowed or (abs(mcol - scol)==1 and crowned):
                    return mrow, mcol
                else:
                    print('Invalid jump!')
                    continue
            elif abs(srow-mrow) == 2:
                if (mcol - scol) == (2*allowed) or (abs(mcol - scol) == 2 and crowned):
                    jrow = (srow + mrow) // 2
                    jcol = (scol + mcol) // 2
                    if correct_sel(opp, board.grid, jrow, jcol):
                        board.delete_pc(jrow, jcol)
                        return mrow, mcol
                    else:
                        print('Invalid Jump!')
                        continue
            else:
                # print(f'mcol-scol = {mcol - scol}, allowed = {allowed}, crown = {crowned}')
                print('NOT A POSITION')
        except ValueError as e:
            print(str(e))


def correct_sel(expected_type, grid, row, col):
    # print(f'type of thing {type(grid[row][col])} should be {expected_type}')
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
    # print(f'type board = {type(boards)}')
    boards.show_board()
    select_pc(player, boards, opp)

    player, opp = opp, player
    win = boards.check_win()