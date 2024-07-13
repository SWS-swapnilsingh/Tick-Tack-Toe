# Function to calculate sum of three numbers
def sum(a, b, c):
    return a + b + c

# Function to print the Tic Tac Toe board
def printBoard(xState, zState):
    # Determine what to print based on the state arrays
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    # Print the Tic Tac Toe board
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

# Function to check if there's a winner
def checkWin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        # Check if X has won
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print('X won the match')
            return 1
        # Check if O has won
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print('O won the match')
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # X's state on the board
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # O's state on the board
    turn = 1  # 1 for X's turn, 0 for O's turn
    
    print("Welcome to Tic Tac Toe")
    
    while True:
        printBoard(xState, zState)  # Display the current board
        
        if turn == 1:
            print("X's Chance")
        else:
            print("O's Chance")
        
        # Get input from the user for their move
        value = int(input("Please enter a value (0-8): "))
        
        # Assign the move to X or O based on whose turn it is
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1
        
        # Check for a winner
        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break
        # Check for a draw
        elif sum(xState) + sum(zState) == 9:
            print("Match Draw")
            break
        
        turn = 1 - turn  # Switch turns between X and O
    
    # Ask the user if they want to play again
    x = int(input("If you want to play again, enter 1. Otherwise, enter 0: "))
    if x == 1:
        continue  # Restart the game
    else:
        print("Thanks for playing")
        break  # Exit the game

