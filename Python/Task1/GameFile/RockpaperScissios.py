import random
hand= eval(input('what would you like to do? rock = 0 paper = 1 scissors = 2'))
opponent_hand = random.randint(0, 2)

if opponent_hand == 0:
    if hand == 2:
        print('oppnent wins :(')

elif opponent_hand == 1:
    if hand == 2:
        print('YOU WIN!')
elif opponent_hand == 2:
    if hand == 2:
        # make a function for game and repeat it here
        print('A draw! play again?')

elif opponent_hand == 0:
    if hand == 1:
        print('YOU WIN!')

elif opponent_hand == 1:
    if hand == 1:
        # make a function for game and repeat it here
        print('A draw! play again?')
elif opponent_hand == 2:
    if hand == 1:
        print('oppnent wins :(')
elif opponent_hand == 0:
    if hand == 2:
        print('oppnent wins :(')
elif opponent_hand == 1:
    if hand == 2:
        print('YOU WIN!')
elif opponent_hand == 2:
    if hand == 2:
        # make a function for game and repeat it here
        print('A draw! play again?')