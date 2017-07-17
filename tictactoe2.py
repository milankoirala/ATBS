# Tic-tac-toe board piece

import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# printBoard(theBoard)

turn = 'X' # player X gets the first move thus initializing [turn = X]

for i in range(9):  # range 9 because there are nine spaces in TTC board
    printBoard(theBoard) # print the initial empty board
    print('Turn for ' + turn + '. Move on which space?') # asking for location to move on board
    move = input() # user specifies the location top, mid, low, L-M-R
    theBoard[move] = turn # 'move' is the location on 'theBoard' which value be 'turn value'

    if turn == 'X': # switching players from 'X' to 'O' or vice-versa
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

