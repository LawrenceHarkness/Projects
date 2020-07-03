name_index = 0
names = []
scores = []

def ScoreBoard(game_names,game_scores):
    names = game_names
    scores = game_scores
    while True:
        Option = eval(input('What would you like to do?\n add a new player score = 1\n Update player score = 2 \ndisplay '
                            'player scores = 3\n view high score = 4 \n view average score = 5\n Exit scoreboard = 6 \n please enter here  : '))

        if Option == 1:
            names , scores = AddNewPlayerScore(names, scores)


        if Option == 2:
            names, scores = UpDatePlayerScore(names, scores)      # next time

        if Option == 3:
            PrintScore(names, scores)
        if Option == 4:
            value_HighScore, person_highscore =HighScore(names, scores)
            print('{1} obtained a highscore of {0}'.format(value_HighScore, person_highscore))

        if Option == 5:
            print('The Average Score is {0}'.format(AverageScore(scores)))
        if Option == 6:
            break




def UpDatePlayerScore(names, scores):
    name_index = 0

    player_name = input('please enter player name')

    player_score = eval(input('Please enter {0} \'s new score'.format(player_name)))

    name_index = 0

    player_found = False

    for i in range(len(names)):

        if names[i] == player_name:
            player_found = True
            break
        name_index += 1





    if player_found == False:
        print (' your username was not found make a new one!')
        names, scores = AddNewPlayerScore(names, scores)


    else :
        scores[name_index] = player_score
        print('your score had been changed to {0}'.format(player_score))
    return names, scores
def WelcolmMessage():
    print('<Welcolm to ScoreBoard>')

scores = []

names = []

def PrintScore(names, scores):

    print('Name\tScore ')

    for i in range(len(names)):

        print('{0}   {1}'.format(names[i], scores[i]))
def AddNewPlayerScore(names, scores):

    new_name = input('Please enter name of player ')


    new_score = eval(input('please enter the score {0} '.format(new_name)))

    scores.append(new_score)

    names.append(new_name)
    return names, scores
def AverageScore(scores):
    AverageScore = 0
    total = 0
    count  = 0

    for b in range(len(scores)):
        total += scores[b]
        count += 1

    AverageScore = total/count


    return AverageScore
def HighScore(names, scores):
    HighScore = scores[0]

    person_highscore = names[0]

    for i in range(len(scores)):

        if HighScore < scores[i]:
            HighScore = scores[i]
            person_highscore = names[i]
    return HighScore , person_highscore

def main() :
    name_index = 0
    while True:

        WelcolmMessage()






