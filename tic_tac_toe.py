"""
Tic Tac Toe Game
================

Instructions:
1. Enter a number (1-9) to place your mark on the corresponding position on the board.
2. The game continues until there's a winner or the board is full (tie game).

Enjoy playing!
"""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theBoard_numbers = {1: 'top-L', 2: 'top-M', 3: 'top-R', 4: 'mid-L', 5: 'mid-M', 6: 'mid-R', 7: 'low-L', 8: 'low-M', 9: 'low-R'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check_winner(board, player):
    win_conditions = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L']
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

turn = 'X'
print("\n********** Tic-Tac-Toe Game **********\n")
print("Enter a number in the range of 1-9 for your move. Each number corresponds to a position on the Tic Tac Toe board.\n1: 'top-L', 2: 'top-M', 3: 'top-R', 4: 'mid-L', 5: 'mid-M', 6: 'mid-R', 7: 'low-L', 8: 'low-M', 9: 'low-R'\n\n")

for i in range(9):
    printBoard(theBoard)
    print('\nTurn for ' + turn + '. Move on which space?')
    move = input()
    print("\n")
    if move.isdigit():
        move = int(move)
        if move in theBoard_numbers:
            move_key = theBoard_numbers[move]
            if theBoard[move_key] == ' ':
                theBoard[move_key] = turn
            else:
                print("The cell is already occupied. Choose another.")
                continue
        else:
            print("Invalid move. Enter a number between 1-9.")
            continue
    else:
        print("Invalid input. Enter a number between 1-9.")
        continue

    if check_winner(theBoard, turn):
        printBoard(theBoard)
        print(f'Player {turn} wins!\n')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printBoard(theBoard)
    print("It's a tie!\n")

print("Game over!")
