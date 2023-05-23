"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None

class InvalidAction(Exception):
    "Raise exception for invalid action"
    pass

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
    x_counter = 0
    o_counter = 0
    for row in board:
        for item in row:
            if item == X:
                x_counter += 1
            elif item == O:
                o_counter += 1
    if x_counter > o_counter:
        return o_counter
    else:
        return x_counter


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves_set.add((i,j))
    return moves_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    to_play = player(board)
    copyboard = copy.deepcopy(board)
    try:
        at_board = copyboard[action[0]][action[1]]
        if at_board != EMPTY:
            raise InvalidAction
        else:
            copyboard[action[0]][action[1]] = to_play
            return copyboard
    except Exception:
        raise InvalidAction


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
