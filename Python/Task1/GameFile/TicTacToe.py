

import GameScore

won = 0
scores = []
names = []

won = scores








def Print_Tic_Tac_Toe(tic_tac_toe):

        print(' |0|1|2|')
        for i in range(3):
            for j in range(3):
                if j == 0:
                    print('{0}|{1}'.format(i, tic_tac_toe[i][j]), end='|')

                elif j == 2:
                    print(tic_tac_toe[i][j], end='|\n')
                else:
                    print(tic_tac_toe[i][j], end='|')

def CheckWinner(tic_tac_toe):
    winner_found = False
    for i in tic_tac_toe:
        if i == ['x', 'x', 'x']:
            print('{} wins'.format(player_1))
            winner_found = True
            won =+ 1
            return winner_found

        if i == ['o', 'o', 'o']:
            print('{} wins'.format(player_2))
            winner_found = True
            won =+ 1
            return winner_found


    for collum in range(3):
        if [tic_tac_toe[collum][0], tic_tac_toe[collum][1], tic_tac_toe[collum][2]] == ['x', 'x', 'x']:
            print('{} wins'.format(player_1))
            winner_found = True
            won = + 1
            return winner_found

        if [tic_tac_toe[collum][0], tic_tac_toe[collum][1], tic_tac_toe[collum][2]] == ['o', 'o', 'o']:
            print('{} wins'.format(player_2))
            winner_found = True
            won = + 1
            return winner_found
    if [tic_tac_toe[0][0], tic_tac_toe[1][1], tic_tac_toe[2][2]] == ['x', 'x', 'x']:
        print('{} wins'.format(player_1))
        winner_found = True
        won = + 1
        return winner_found
    if [tic_tac_toe[0][0], tic_tac_toe[1][1], tic_tac_toe[2][2]] == ['o', 'o', 'o']:
        print('{} wins'.format(player_2))
        winner_found = True
        won = + 1
        return winner_found
    if [tic_tac_toe[0][2], tic_tac_toe[1][1], tic_tac_toe[2][0]] == ['x', 'x', 'x']:
        print('{} wins'.format(player_1))
        winner_found = True
        return winner_found
    if [tic_tac_toe[0][2], tic_tac_toe[1][1], tic_tac_toe[2][0]] == ['o', 'o', 'o']:
        print('{} wins'.format(player_2))
        winner_found = True
        winner = False
        won = + 1
        return winner_found

    return winner_found


player_1 = input('Player 1 Please Enter Your Name Here ->')

player_2 = input('Player 2 Please Enter Your Name Here ->')

tic_tac_toe = [[' ',' ',' '],[' ', ' ',' '],[' ',' ',' ']]
# --------------------------------------------------------------
winner = False

while True:

    Print_Tic_Tac_Toe(tic_tac_toe)
    if winner is True:
        break
    x_move1 = eval(input('{0} please enter where your x coordinate'.format(player_1)))

    y_move1 = eval(input('{0} please enter where your y coordinate'.format(player_1)))

    tic_tac_toe[y_move1][x_move1] = 'x'

    Print_Tic_Tac_Toe(tic_tac_toe)
    winner = CheckWinner(tic_tac_toe)
    if winner is True:
        break
    x_move2 = eval(input('{0} please enter your x coordinate'.format(player_2)))

    y_move2 = eval(input('{0} please enter your y coordinate'.format(player_2)))

    tic_tac_toe[y_move2][x_move2] = '0'

    #TODO add gamescore as we did in hang ma n

