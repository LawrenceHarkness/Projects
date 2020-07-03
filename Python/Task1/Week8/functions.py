
def WelcomMessage():
    print('Welcom to the calculator app')
def SubFunc(c, d):
    ans2 = c - d
    return ans2
def SumFunc1(a, b):
    ans1 = a + b
    return ans1
def DivFunc(e, f):
    ans3 = e / f
    return ans3
def MulFunc(g, h):
    ans4 = g * h
    return ans4
WelcomMessage()
option = eval(input('select whitch funtion you want to use (addition = 1 , subtration = 2 , division = 3 . multiplication = 4) :'))
num_1 = eval(input('please enter num_1:  '))
num_2 = eval(input('please enter num_2:  '))
if option == 1:
    num_3 = SumFunc1(num_1, num_2)
    print('The Answer to {0} + {1} is {2}'.format(num_1, num_2, num_3))
if option == 2:
    num_3 = SubFunc(num_1, num_2)
    print('The Answer to {0} - {1} is {2}'.format(num_1, num_2, num_3))
if option == 3:
    num_3 = DivFunc(num_1, num_2)
    print('The Answer to {0} ÷ {1} is {2}'.format(num_1, num_2, num_3))
if option == 4:
    num_3 = MulFunc(num_1, num_2)
    print('The Answer to {0} x {1} is {2}'.format(num_1, num_2, num_3))