"""
Tic Tac Toe Player
"""
import copy

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
    x_counter = 0
    o_counter = 0
    for row in board:
        for item in row:
            if item == X:
                x_counter += 1
            elif item == O:
                o_counter += 1
    if x_counter <= o_counter:
        return X
    return O


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
    newboard = copy.deepcopy(board)
    if not (0 <= action[0] < 3) and (0 <= action[1] < 3):
        raise Exception
    if newboard[action[0]][action[1]] is not EMPTY:
        raise Exception
    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal win
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # Vertical win
    for i in range(3):
        xc = 0
        oc = 0
        for row in board:
            if row[i] == X:
                xc += 1
            elif row[i] == O:
                oc += 1
        if xc == 3:
            return X
        elif oc == 3:
            return O
    
    # Diagonal win (Main & Anti)
    dcx = ocx = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if board[i][j] == X:
                    dcx += 1
                elif board[i][j] == O:
                    ocx += 1
    if dcx == 3:
        return X
    elif ocx == 3:
        return O

    dcx = ocx = 0
    for i in range(3): 
        for j in range(3):
            if ((i + j) == (2)): # This condition is for the anti-diagonal, 2 is (3 - 1) or (n - 1)
                if board[i][j] == X:
                    dcx += 1
                elif board[i][j] == O:
                    ocx += 1
    if dcx == 3:
        return X
    elif ocx == 3:
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # We have a winner
    if winner(board) in (X,O):
        return True

    # No moves left
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

    If I am X: I want to MAXIMIZE my outcome from the outcomes my opponent can play

    If I am O: I want to MINIMIZE my outcome from the outcomes my opponent can play

    Supposing opponent is not a dumbass and plays optimally
    """
    current_player = player(board)

    next_action = None
    

    if terminal(board):
        return None
    
    if current_player == X:
        # For every action I can play, I consider my opponents reaction 
        # I am trying to maximize, opponent trying to minimize
        v = float('-inf')
        for action in actions(board):
            opponent_play = minvalue(result(board, action))
            if opponent_play > v: # I am maximizing here
                v = opponent_play
                next_action = action

    elif current_player == O:
        # For every action I can play, I consider my opponents reaction 
        # I am trying to minimize, opponent trying to maximize
        v = float("inf")
        for action in actions(board):
            opponent_play = maxvalue(result(board, action))
            if opponent_play < v: # I am minimising here
                v = opponent_play
                next_action = action

    return next_action
        

def maxvalue(board):
    if terminal(board):
        return utility(board)
    else:
        v = float("-inf")
        for action in actions(board):
            v = max(v, minvalue(result(board, action)))
    return v
    
    

def minvalue(board):
    if terminal(board):
        return utility(board)
    else:
        v = float("inf") 
        for action in actions(board):
            v = min(v, maxvalue(result(board, action)))
        return v
