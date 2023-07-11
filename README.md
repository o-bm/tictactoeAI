# Tic-Tac-Toe AI

Tic-Tac-Toe AI is an implementation of the classic game using the Pygame library. It features an unbeatable AI player that utilizes the minimax algorithm. The minimax algorithm is a widely used technique in game playing, enabling the AI to make optimal moves in a turn-based game.

## Features

- Pygame-based graphical interface for an interactive Tic-Tac-Toe game.
- Single-player mode against an AI opponent that employs the minimax algorithm.
- Unbeatable AI that selects the optimal move to maximize its chances of winning or at least achieving a draw.
- User-friendly interface with intuitive controls.

## How the Minimax Algorithm Works

The minimax algorithm is a decision-making algorithm commonly used in game playing. It works by exploring all possible moves and evaluating the potential outcomes for each move. The algorithm assigns scores to different game states and selects the move that leads to the best possible outcome.

In the case of Tic-Tac-Toe, the minimax algorithm analyzes the game tree to determine the optimal move at each step. It assumes that both players play perfectly, and it recursively explores all possible moves until it reaches the terminal game states (win, lose, or draw). By assigning scores to these terminal states, the algorithm backtracks and selects the move with the highest score for the AI player, while assuming the opponent will also make optimal moves.

The implementation of the minimax algorithm in Tic-Tac-Toe AI ensures that the AI player is challenging to beat, providing an engaging and strategic gaming experience.

## Requirements

- Python 3.x
- Pygame library

## Installation

Clone the repository:
```bash
git clone https://github.com/o-bm/tic-tac-toe-ai.git
```
Install the required Python libraries:
```bash
pip install -r requirements.txt
```
Run the game
```python
python runner.py
```

## Looking forward: Alpha-Beta Pruning

Alpha-beta pruning is an optimization technique used in conjunction with the minimax algorithm to reduce the number of nodes that need to be evaluated. It prunes branches of the game tree that are guaranteed to be irrelevant for the final decision, thus significantly reducing the search space.

By maintaining two values, alpha and beta, the algorithm avoids evaluating moves that are less likely to be chosen. Alpha represents the best score that the maximizing player (AI) can achieve so far, while beta represents the best score that the minimizing player (opponent) can achieve. The algorithm prunes branches when it finds a move that makes the current player worse off than a previously examined move.

Alpha-beta pruning enhances the efficiency of the minimax algorithm, allowing the AI to search deeper into the game tree and make decisions more quickly.




This project was part of Harvard's CS50AI course.
