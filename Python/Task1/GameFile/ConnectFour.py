
field = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
field_size = 6


def WinDiagonals():
    winner_found = False
    if '{0}{1}{2}{3}'.format(field[1-1][3-1], field[2-1][4-1], field[3-1][5-1], field[4-1][6-1]).__contains__('xxxxx'):
        winner_found = True
        print('player_2 has won')
    if '{0}{1}{2}{3}'.format(field[6-1][3-1], field[5-1][4-1], field[4-1][5-1], field[3-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}'.format(field[6-1][2-1], field[5-1][3-1], field[4-1][4-1], field[3-1][5-1], field[2-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}{5}'.format(field[6-1][1-1], field[5-1][2-1], field[4-1][3-1], field[3-1][4-1], field[2-1][5-1],field[1-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}'.format(field[5-1][1-1], field[4-1][2-1], field[3-1][3-1], field[2-1][4-1], field[1-1][5-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}'.format(field[4-1][1-1], field[3-1][2-1], field[2-1][3-1], field[1-1][4-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}'.format(field[3-1][1-1], field[4-1][2-1], field[5-1][3-1], field[6-1][4-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}'.format(field[2-1][1-1], field[3-1][2-1], field[4-1][3-1], field[5-1][4-1], field[6-1][5-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}'.format(field[1-1][1-1], field[2-1][2-1], field[3-1][3-1], field[4-1][4-1], field[5-1][5-1],field[6-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}{4}'.format(field[1-1][2-1], field[2-1][3-1], field[3-1][4-1], field[4-1][5-1], field[5-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')

    if '{0}{1}{2}{3}'.format(field[1-1][3-1], field[2-1][4-1], field[3-1][5-1], field[4-1][6-1]).__contains__('OOOO'):
        winner_found = True
        print('player_1 has won')
    if '{0}{1}{2}{3}'.format(field[1 - 1][3 - 1], field[2 - 1][4 - 1], field[3 - 1][5 - 1],
                             field[4 - 1][6 - 1]).__contains__('xxxxx'):
        winner_found = True
        print('player_2 has won')
    if '{0}{1}{2}{3}'.format(field[6 - 1][3 - 1], field[5 - 1][4 - 1], field[4 - 1][5 - 1],
                             field[3 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}'.format(field[6 - 1][2 - 1], field[5 - 1][3 - 1], field[4 - 1][4 - 1], field[3 - 1][5 - 1],
                                field[2 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}{5}'.format(field[6 - 1][1 - 1], field[5 - 1][2 - 1], field[4 - 1][3 - 1], field[3 - 1][4 - 1],
                                   field[2 - 1][5 - 1], field[1 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}'.format(field[5 - 1][1 - 1], field[4 - 1][2 - 1], field[3 - 1][3 - 1], field[2 - 1][4 - 1],
                                field[1 - 1][5 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}'.format(field[4 - 1][1 - 1], field[3 - 1][2 - 1], field[2 - 1][3 - 1],
                             field[1 - 1][4 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}'.format(field[3 - 1][1 - 1], field[4 - 1][2 - 1], field[5 - 1][3 - 1],
                             field[6 - 1][4 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}'.format(field[2 - 1][1 - 1], field[3 - 1][2 - 1], field[4 - 1][3 - 1], field[5 - 1][4 - 1],
                                field[6 - 1][5 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}'.format(field[1 - 1][1 - 1], field[2 - 1][2 - 1], field[3 - 1][3 - 1], field[4 - 1][4 - 1],
                                field[5 - 1][5 - 1], field[6 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}{4}'.format(field[1 - 1][2 - 1], field[2 - 1][3 - 1], field[3 - 1][4 - 1], field[4 - 1][5 - 1],
                                field[5 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

    if '{0}{1}{2}{3}'.format(field[1 - 1][3 - 1], field[2 - 1][4 - 1], field[3 - 1][5 - 1],
                             field[4 - 1][6 - 1]).__contains__('xxxx'):
        winner_found = True
        print('player_2 has won')

def print_field(list_display):

        print(' ',end='|')
        for b in range(field_size):
            if b == field_size - 1:
                print(('{0}'.format(b)), end='|\n')
            else:

                print(('{0}'.format(b)), end='|')

        for i in range(field_size):
            for j in range(field_size):
                if j == 0:
                    print('{0}|{1}'.format(i, list_display[i][j]), end='|')

                elif j == field_size - 1:
                    print(list_display[i][j], end='|\n')

                else:
                    print(list_display[i][j], end='|')
print_field(field)


def move(symbol, collumn):
    found = False

    counter = 5
    while not found:
        if field[counter][collumn] == ' ':
            field[counter][collumn] = symbol
            found = True
        else:
            counter = counter - 1


def WinOnCollumn():
    winner_found = False
    # Checks column for winner
    for column in range(6):

        if '{0}{1}{2}{3}{4}{5}'.format(field[0][column],field[1][column],field[2][column],field[3][column],field[4][column],field[5][column])\
                .__contains__('OOOO'):
            print('Player 1 wins')
            winner_found = True
            break
        elif '{0}{1}{2}{3}{4}{5}'.format(field[0][column],field[1][column],field[2][column],field[3][column],field[4][column],field[5][column])\
                .__contains__('xxxxx'):
            print('Player 2 wins')
            winner_found = True
            break
    return winner_found



def WinOnRow():
#Check rows for winners
    winner_found = False
    for row in range(6):
        if '{0}{1}{2}{3}{4}{5}'.format(field[row][0],field[row][1],field[row][2],field[row][3],
                                       field[row][4],field[row][5]).__contains__('OOOO'):
            print('Player 1 wins')
            winner_found = True
            break
        elif '{0}{1}{2}{3}{4}{5}'.format(field[row][0],field[row][1],field[row][2],field[row][3],
                                         field[row][4],field[row][5]).__contains__('xxxx'):
            print('Player 2 wins')
            winner_found = True
            break
    return winner_found

while True:

    IsTheraWinner= False
    while IsTheraWinner == False:
        player1move = eval(input('Player 1 please enter which column you would like to pace your O  '))
        move('O',player1move)
        print_field(field)
        IsTheraWinner = WinOnCollumn()
        IsTheraWinner = WinOnRow()
        IsTheraWinner = WinDiagonals()


        player2move = eval(input('Player 2 please enter which column you would like to pace your X  '))
        move('x', player2move)
        print_field(field)
        IsTheraWinner = WinOnCollumn()
        IsTheraWinner = WinOnRow()
        IsTheraWinner = WinDiagonals()


    playagain = input('Would you like to play again? y/n')
    if playagain == 'n':
        IsTheraWinner = True
    if playagain == 'y':
        IsTheraWinner = False

#TODO make sure that player 2 can move aswell! and look at collums that if anyone is winning


# TODO add diagonal wins hint No For loop needed use if statment




