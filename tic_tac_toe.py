import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    a = 0
    b = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                a += 1
            elif board[i][j] == O:
                b += 1
    if a <= b:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                s.add((i,j))
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a = action[0]
    b = action[1]
    if board[a][b] != EMPTY:
        raise Exception("Invalid move")
    board1 = [[EMPTY for i in range(len(board))]for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            board1[i][j] = board[i][j]
    h = player(board)

    board1[a][b] = h
    return board1



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == X:
        return X
    elif board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == O:
        return O
