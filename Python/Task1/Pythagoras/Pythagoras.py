import time
import math


Asquard = eval(input('Please enter your first value'))


bsquard = eval(input('please Enter your second value'))


AAcSquard = Asquard * Asquard
bAcSquard = bsquard * bsquard
step1 = AAcSquard + bAcSquard
Answer = math.sqrt(step1)


print('a² + b² = c²')
time.sleep(1)
print('{0}² + {1}² = c²'.format(Asquard, bsquard))
time.sleep(1)
print('{0} = c²'.format(step1))
time.sleep(1)
print('{0} = c'.format(Answer))