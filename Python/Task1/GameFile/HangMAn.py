y = 0
import random
import GameScore

scores = []

names = []



words = ['bean','king','good','pat','car','cat','light','painting']

def HangMan():

    name = input('please enter your user name!')

    score = 0

    rand = random.randint(0, 5)

    lives = 10

    while lives > 0:

        lg = 0

        word = words[rand]

        gues = input('Guess a word ')

        for i in word:

            if i in gues:

                print(i)

                lg = lg + 1

            else:

                print('_')

                lives = lives - 1

        print('you have {0} lives'.format(lives))

        if lg == len(word):

            print('congratulations you won!')

            score = lives

            names.append(name)

            scores.append(score)

            break





def main():
    while True:
        yes = input('would ypu like to play agian? (y/n)')
        while yes == 'y':
            HangMan()
            GameScore.PrintScore(names, scores)
            yes = input('would ypu like to play agian? (y/n)')
        sec_scores = input('Would you like to see the score board? (y/n)')
        if sec_scores == 'y':
            GameScore.ScoreBoard(names, scores)

main()



