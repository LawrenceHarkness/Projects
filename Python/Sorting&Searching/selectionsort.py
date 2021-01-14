import random

i = 0
list = []

while i <= random.randint(1,10):
    list.append(random.randint(1,10))
    i = i + 1

print(list)

for i in range(len(list)):
    min_idx = i
    for j in range(i + 1, len(list)):
        if list[min_idx] > list[j]:
            min_idx = j


    list[i], list[min_idx] = list[min_idx], list[i]

print("Sorted array")
for i in range(len(list)):
    print(list[i])