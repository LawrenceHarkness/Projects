
list_names = ['ben', 'thabo', 'boitumelo', 'lawrence', 'tabisa']

for name in list_names:
    print(name, end=' ')

# Initialize 2d array
tic_tac_toe = [['o','x','x'],[' x', 'x','o'],['x','o','x']]

# Print value at specific index
print(tic_tac_toe[1][0])
print(tic_tac_toe[2][2])

# Change value @ specific index
tic_tac_toe[1][0] = 'x'

print('  012')
for i in range(3):
    for j in range(3):
        if j== 0 :
            print('{0}:{1}'.format(i, tic_tac_toe[i][j]), end='')

        elif j == 2 :
            print(tic_tac_toe[i][j], end='\n')
        else  :
            print(tic_tac_toe[i][j], end ='')






# Check which player has won by row
for i in tic_tac_toe:
    if i == ['x','x','x']:
        print('Player 1 wins')
    if i == ['o','o','o']:
        print('Player 2 wins')

# TODO Check which player has won by column
for collum in range(3):
    if [tic_tac_toe[collum][0],tic_tac_toe[collum][1],tic_tac_toe[collum][2]] == ['x', 'x', 'x' ]:
        print('Player 1 wins')
    if [tic_tac_toe[collum][0],tic_tac_toe[collum][1],tic_tac_toe[collum][2]] == ['o', 'o', 'o' ]:
        print('Player 2 wins')


# TODO add diagonal wins hint No For loop needed use if statment
if [tic_tac_toe[0][0],tic_tac_toe[1][1],tic_tac_toe[2][2]] == ['x', 'x', 'x' ]:
    print('Player 1 wins')
if [tic_tac_toe[0][0],tic_tac_toe[1][1],tic_tac_toe[2][2]] == ['o', 'o', 'o' ]:
    print('Player 2 wins')
if [tic_tac_toe[0][2],tic_tac_toe[1][1],tic_tac_toe[2][0]] == ['x', 'x', 'x' ]:
    print('Player 1 wins')
if [tic_tac_toe[0][2],tic_tac_toe[1][1],tic_tac_toe[2][0]] == ['o', 'o', 'o' ]:
    print('Player 2 wins')

