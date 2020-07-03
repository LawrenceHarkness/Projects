scores = [3, 1, 2, 3, 2, 1]

names = ['jack', 'Thabo', 'Tom', 'Bob', 'Tiger', 'Lisa' ]

highscore = scores[0]

person_highscore = names[2]

for i in range(len(scores)):


    if highscore < scores[i] :

         highscore = scores[i]
         person_highscore = names[i]

print('{1} obtained a highscore of {0}'.format(highscore,person_highscore))







