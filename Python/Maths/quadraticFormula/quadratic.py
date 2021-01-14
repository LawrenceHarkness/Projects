import math

decimalPoint = int(input('enter decimal point'))

A = int(input('enter A'))
B = int(input('enter B'))
C = int(input('enter C'))

print(A,B,C)

x1 = (-B + math.sqrt((B*B) -4*(A)*(C))) / (2*A)
x2 = (-B - math.sqrt((B*B) -4*(A)*(C)))/(2*A)

x1 = round(x1,decimalPoint)
x2 = round(x2,decimalPoint)

print(x1,x2)
