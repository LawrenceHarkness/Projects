import random
yes = input('would you like to play?(y/n): ')
while yes == 'y':
    number = random.randint(1, 10)
    gues = eval(input('gues a number bewtween 1 and 10!: '))
    correct = True
    while correct == True:

        if number == gues:
            print('your right!')
            correct = False
        elif gues > number:
            print('Your gues is too high! Try again? :')

            gues = eval(input('gues a number bewtween 1 and 10!: '))
        elif gues < number:

            print('Your gues is too low! Try again? :')
            gues = eval(input('gues a number bewtween 1 and 10!: '))
    yes = input('would you like to play again?: ')