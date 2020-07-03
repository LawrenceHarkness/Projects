tempreture = eval(input('Please enter the temperature you want to convert: '))
unit = input ('Please enter the units of measurement for entered tempreture: ')
if unit == 'C' or unit == 'c':
    output_temp = (9 * tempreture +(32 * 5)) / 5
    print(output_temp)

elif unit == 'F' or unit == 'f':
    output_temp = (5 * (tempreture - 32))/ 9
    print(output_temp)
else:
    print ('you have entered an invalid input')