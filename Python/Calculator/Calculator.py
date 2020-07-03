print ('Welcom the Calculator ')

Name = input ('please enter your name: ')



num_1 = input('please enter first number: ')

num_2 = input('please enterr second number: ')



num_1 = int(num_1)
num_2 = int(num_2)

OutputSum = num_1 * num_2

output = str(num_1)+' x ' + str(num_2) + ' = ' + str(OutputSum)



OutputSum2 = num_1 + num_2

output2 = str(num_1)+' + ' + str(num_2) + ' = ' + str(OutputSum2)


OutputSum3 = num_1 - num_2

output3 = str(num_1)+' - ' + str(num_2) + ' = ' + str(OutputSum3)

OutputSum4 = num_1 / num_2

output4 = str(num_1)+' ÷ ' + str(num_2) + ' = ' + str(OutputSum4)



print ('thank you for using calculator ' + Name )
print ('here are your answers')
print(output2)
print (output)
print (output3)
print (output4)