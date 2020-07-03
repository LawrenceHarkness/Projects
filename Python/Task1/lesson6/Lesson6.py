height = eval(input('input height: '))

total_height = height
num_input = 1
while height != -1:
    height = eval(input('input height: '))
    total_height += height
    num_input += 1
average = total_height / num_input
print(average)