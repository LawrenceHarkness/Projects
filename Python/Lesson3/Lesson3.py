print('string lesson')
name = 'Lawrence'
surname = 'Harkness'
num_jump = 10
output = 'hi {0} {1} thanks for using our program. today is {2}. \n{0} {1} could you please jump {3} times for me?  '.format(name,surname, 'Tuesday',num_jump)
print(output)
#indexing
Name = sentence = 'the fat cat sat on a mat and jumped inside a hat!'
print(sentence[21])
print(sentence[0:3]) # substring
print(sentence[28:48])
print(len(sentence)) # get length of string
print (sentence.lower()) #lower case of the string
print (sentence.upper()) #lower case of the string
print(sentence.replace('cat', 'rat'))
print(sentence*1)