import random
roll = input('roll the dice? (y/n): ')
while roll == 'y':

     dice = random.randint(1,6)
     print(dice)

     roll = input('roll the dice again? (y/n): ')