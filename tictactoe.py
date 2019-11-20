import os

inGameStatus = True
winner = False
countChoose = 0
player1 = ''
player2 = ''
allowed = ['X', 'O', 'x', 'o']
allowedBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
board = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9'
}

def show(board):
    print( board['1'] + ' | ' + board['2'] + ' | ' + board['3'] )
    print( '-' + ' | ' + '-' + ' | ' +'-' )
    print( board['4'] + ' | ' + board['5'] + ' | ' + board['6'] )
    print( '-' + ' | ' + '-' + ' | ' + '-' )
    print( board['7'] + ' | ' + board['8'] + ' | ' + board['9'] )

def searchWinner(board):
    if board['1'] + board['2'] + board['3'] == 'OOO':
        global winner
        global inGameStatus
        if player1 == 'O':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['1'] + board['2'] + board['3'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['4'] + board['5'] + board['6'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['4'] + board['5'] + board['6'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['7'] + board['8'] + board['9'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['7'] + board['8'] + board['9'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['1'] + board['4'] + board['7'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['1'] + board['4'] + board['7'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['2'] + board['5'] + board['8'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['2'] + board['5'] + board['8'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['3'] + board['6'] + board['9'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['3'] + board['6'] + board['9'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['1'] + board['5'] + board['9'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['1'] + board['5'] + board['9'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif board['3'] + board['5'] + board['7'] == 'OOO':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    elif  board['3'] + board['5'] + board['7'] == 'XXX':
        if player1 == 'X':
            winner = 'Player1'
        else:
            winner = 'Player2'
        inGameStatus = False
    else:
        return False

# print(board)
# logic game
while inGameStatus or countChoose != 9:
    while player1 not in allowed:
        player1 = input('Player1 Please choose between X OR O:')
        if player1 in ['x', 'X']:
            player1 = 'X'
            player2 = 'O'
        if player1 in ['o', 'O']:
            player1 = 'O'
            player2 = 'X'

    show(board)
    player1Choose = input('Player1 please select number on the board ( '+player1+' ) :')
    while player1Choose not in allowedBoard:
        show(board)
        print('selected number board not found')
        player1Choose = input('Player1 please select number on the board ( '+player1+' ):')
    board[player1Choose] = player1
    searchWinner(board)
    countChoose += 1
    if inGameStatus == False or countChoose == 9:
        break
    # begin player 2 turn
    show(board)
    player2Choose = input('Player2 please select number on the board( '+player2+' ):')
    while player2Choose not in allowedBoard:
        show(board)
        print('Selected number board not found')
        player2Choose = input('Player2 please select number on the board( '+player1+' ):')
    board[player2Choose] = player2
    searchWinner(board)
    countChoose += 1

clear = lambda:os.system('cls')
clear()
show(board)
if( winner == False ):
    print('Game ended')
else:
    print('The game winner is:' + winner)
# end logic game