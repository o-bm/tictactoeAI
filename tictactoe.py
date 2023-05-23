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
    # horizontal win
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # vertical win
    x_count = 0
    o_count = 0
    for i in range(3):
        for row in board:
            if row[i] == X:
                x_count += 1
            elif row[i] == O:
                o_count += 1
    if x_count == 3:
        return X
    elif o_count == 3:
        return O
        
    # there are only 2 possible diagonal wins
    if board[1][1] == X:
        if (board[0][0] == X and board[2][2] == X) or (board[0][2] == X and board[2][0] == X):
            return X
    elif board[1][1] == O:
        if (board[0][0] == O and board[2][2] == O) or (board[0][2] == O and board[2][0] == O):
            return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # winner - game ended
    if winner(board) in (X,O):
        return True

    # no moves - game ended
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    If I'm the maximizing player, I want to choose from my actions, the one that will 
    lead to the MAXIMUM possible outcome, from the outcomes my opponent has offered me. 
    And, of course, my opponent has tried to minimize the outcome to offer me.

    On the contrary, if it's the the minimizing player's turn, now I'm in the shoes of my opponent.
    In this case, as per my point of view, he/she is trying to minimize my outcome. Then I need to 
    choose from his/her actions, the one that will lead to the MINIMUM possible outcome 
    which is what he/she would do. 

    Of course, this supposes that your opponent is playing optimally.
    """
    raise NotImplementedError
