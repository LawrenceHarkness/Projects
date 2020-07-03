import random
num_1 = eval(input('please input a number'))
num_rand = random.randint(10, 100)
if  num_1 == num_rand:
    print('you guesed the number correctly')
else:
     print (' you have guessed the number incorrect the number is {}'.format(num_rand))