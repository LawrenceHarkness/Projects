import random
import sys

def insertionSort(arr:list):
    n = len(arr)
    for i in range(1,n,1):
        key = arr[i]
        j = i - 1

        #Move elements of arr[0..i-1], that are
        #greater than key, to one position ahead
        #of their current position

        while j >= 0 & arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return(arr)

    #driver method
def main():

    i = 0
    arr = []
    while i <= random.randint(1, 10):
        arr.append(random.randint(1, 10))
        i = i + 1
    print(arr)
    arr = insertionSort(arr)
    print(arr)

main()
