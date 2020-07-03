name_index = 0

scores = [3, 1, 2, 3, 2, 1]
names = ['jack', 'Thabo', 'Tom', 'Bob', 'Tiger', 'Lisa' ]



player_name = input('please enter player name')

player_score = eval(input('Please enter {0} \'s new score'.format(player_name)))

name_index = 0

player_found = False

for i in range(len(names)):


    if names[i] == player_name :
        player_found = True
        break
    name_index += 1



scores[name_index] = player_score

print(scores)








