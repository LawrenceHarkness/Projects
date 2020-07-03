print ('Welcom to the calculator ')

Name = input ('please enter your name: ')



num_1 = input('please enter first number: ')

num_2 = input('please enter second number: ')

num_3 = input('please enter third number: ')

num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)
OutputSum = num_1 + num_2

output = str(num_1)+' + ' + str(num_2) + ' = ' + str(OutputSum)



OutputSum2 = num_1 * num_3

output2 = str(num_1)+' x ' + str(num_3) + ' = ' + str(OutputSum2)


OutputSum3 = num_2 / num_3

output3 = str(num_1)+' ÷ ' + str(num_3) + ' = ' + str(OutputSum3)

OutputSum4 = (num_1 * num_3) / (num_2 - num_3)

output4 = '(' + str(num_1)+' x ' + str(num_3) + ')' + '÷' + '( ' + str(num_2) + ' - ' + str(num_3) + ')' + ' = ' + str(OutputSum4)



print ('thank you for using calculator ' + Name )
print ('here are your answers ☟ ')
print (output)
print(output2)
print (output3)
print (output4)