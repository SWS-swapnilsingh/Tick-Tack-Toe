# Tic Tac Toe Game in Python

This is a simple Tic Tac Toe game implemented in Python. It allows two players (X and O) to take turns making moves on a 3x3 grid until one player wins or the game ends in a draw.

## How to Play

1. Run the Python script.
2. Follow the prompts to enter your moves as either X or O.
3. The board will be displayed after each move.
4. The game will announce the winner or declare a draw when appropriate.
5. You can choose to play again or exit after each game.

## Code Explanation

The code consists of several functions and a main game loop:

- `sum(a, b, c)`: Calculates the sum of three numbers.
- `printBoard(xState, zState)`: Prints the Tic Tac Toe board based on the current state of X and O moves.
- `checkWin(xState, zState)`: Checks if there's a winner based on the current state of X and O moves.

The game starts by initializing the board and alternating turns between X and O. After each move, it checks for a winner or a draw. Players can choose to play again or exit after each game.


