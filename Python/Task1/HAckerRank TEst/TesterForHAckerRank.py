hieght = eval(input('please enter hieght'))
Width = eval(input('Please enter width'))

counter = int((Width - 3) / 2 )

for i in range(1, hieght, 2):
    print( '-' * counter  + '.|.' * i + '-' * counter )
    counter = counter - 3
counter = 3
print('{0}WELCOME{0}'.format( '-' * hieght))
for i in range(1, hieght, 2):
    alien = (hieght-i-1)
    print( '-' * counter  + '.|.' * (alien)  + '-' * counter )
    counter = counter + 3



# 7 x 21
#print('_' * 9 + '.|.'*1 + '_' * 9)
#print('_' * 6 + '.|.'*3 + '_' * 6)
#print('_' * 3 + '.|.'*5 + '_' * 3)
#print('{0}WELCOME{0}'.format( '_' * hieght))
#print('_' * 3 + '.|.'*5 + '_' * 3)
#print('_' * 6 + '.|.'*3 + '_' * 6)
#print('_' * 9 + '.|.'*1 + '_' * 9)
# 11 x 33
#print('_' * 15 + '.|.'*1 + '_' * 15)
#print('_' * 12 + '.|.'*3 + '_' * 12)
#print('_' * 9 + '.|.'*5 + '_' * 9)
#print('{0}WELCOME{0}'.format( '_' * hieght))
#print('_' * 3 + '.|.'*5 + '_' * 3)
#print('_' * 6 + '.|.'*3 + '_' * 6)
#print('_' * 9 + '.|.'*1 + '_' * 9)













ranger = eval(input(''))


for i in range(ranger):
    print((i * 2) * '*')

for j in range(ranger - 3, ranger + 1):
    print((j * 3) * 'q')

for l in range(ranger - 3, ranger + 1):
    print((l * 4) * 'o')

for k in range(ranger - 2):
   print('$' * (ranger - 2))