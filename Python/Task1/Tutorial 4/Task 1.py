import random
name = input('please input your name: ')
surname = input('please input your surname: ')
value = random.randint(1, 9)
output = 'your radom generated password is {0}{1}{2}'.format(name[0:3].lower(), surname[-3:].upper(),value)
print(output)





