from tictactoe import initial_state, actions, result, winner
X = "X"
O = "O"
EMPTY = None
board =[[X, X, O],
        [X, O, O],
        [O, EMPTY, X]]

print(winner(board))