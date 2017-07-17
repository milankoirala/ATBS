# Implementation of simple TIC-TAC-TOE game

#! Python 3

import random

# Printing the board on the screen

def drawBoard(board):
    # This function prints out the board is was passed.
    #
    # 'board' is a list of 10 strings representing the TTC board (ignoring the index 0)

    print(' |  |')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print(' |  |')
    print('----------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print(' |  |')
    print('----------')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print(' |  |')

# Ask the player be X or O
def inputPlayerLetter():
    # Let the player type which letter they want to be
    # Returns a list with player's letter as first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
    # the first element in the list is player's letter, the second is the computer's letter
    if letter = 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function return True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startwith('y')   # True as long as player types anything staring with letter 'y'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and player's letter this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7]) == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # across the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # across the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # across the right side
    (bo[9] == le and bo[5] == le and bo[1] == le) or # across the diagonal
    (bo[7] == le and bo[5] == le and bo[3] == le))# across the second diagonal

def getBoardCopy(board):
    # Make a duplicate copy of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    
    return dupeBoard

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ''

def getPlayerMove(board):
    # Let the player type in their move.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return.random.choice(possibleMoves)
    else:
        return None



