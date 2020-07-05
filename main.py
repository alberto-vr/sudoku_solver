# This is a sudoku solver with Backtracking

#       x i---->
#     y
#     j
#     |
#     V



def show_board(board):
    '''
    :param board:
    :return: None
    '''
    contador_fil = 0
    print("")
    print(" ","- "*11)
    for j in range(9):
        contador_col = 0
        for i in range(9):
            if contador_col % 3 == 0:
                print("| ", end='')
            if board[j][i] != 0:
                print(f"{board[j][i]} ", end='')
            else:
                print("  ", end='')
            contador_col += 1
        print('|')
        contador_fil += 1
        if contador_fil % 3 == 0:
            print(" ","- "*11)
        else:
            pass

def valid(board, number, y, x):
    '''
    :param board: List of lists
    :param number: int
    :param y: 0-9
    :param x: 0-9
    :return: boolean
    '''
    if sol_in_row(board, number, y, x) or sol_in_column(board, number, y, x) or sol_in_square(board, number, y, x):
        return False
    else:
        return True

def sol_in_row(board, number, y, x):
    '''
    :param board: List of lists
    :param number: int
    :param y: 0-9
    :param x: 0-9
    :return: boolean
    '''
    if number in board[y]:
        return True
    return False

def sol_in_column(board, number, y, x):
    '''
    :param board: List of lists
    :param number: int
    :param y: 0-9
    :param x: 0-9
    :return: boolean
    '''
    column = [board[j][x] for j in range(9)]
    if number in column:
        return True
    return False

def sol_in_square(board, number, y, x):   # (5, 0, 2)
    '''
    :param board: List of lists
    :param number: int
    :param y: 0-9
    :param x: 0-9
    :return: boolean
    '''
    divisions = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for division in divisions:
        if y in division:
            list_j = division
        if x in division:
            list_i = division
    square = [board[j][i] for j in list_j for i in list_i]
    if number in square:
        return True
    return False

def new_blank_gap(board):
    '''
    :param board:
    :return: Next 0 with position [j,i] or None
    '''
    for j in range(9):
        for i in range(9):
            if board[j][i] == 0:
                return j, i
            else:
                continue
    return None, None

def solve(board):
    '''
    :param board:
    :return: solved_board, boolean
    '''
    board_proposal = board
    if new_blank_gap(board) == (None, None):
       return board, True

    gap_j, gap_i = new_blank_gap(board)
    for n in range(1, 10):
        if valid(board_proposal, n, gap_j, gap_i):
            print(f"[{gap_j}, {gap_i}]: {n}")
            board_proposal[gap_j][gap_i] = n
            solved_board, is_finish = solve(board_proposal)
            if is_finish == True:
                return solved_board, True
            else:
                board_proposal[gap_j][gap_i] = 0
                continue
        else:
            continue

    return board, False
