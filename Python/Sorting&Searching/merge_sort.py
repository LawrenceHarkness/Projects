import random
import sys
sys.setrecursionlimit(1500000)

def merge(arr:list,l:int,m:int,r:int):

    #Find sizes of two subarrays to be merged
    n1 = m - l + 1
    n2 = r - m

    #Create temp arraysCreate temp arrays
    L = [n1]
    R = [n2]

    #Copy data to temp arrays

    #i = 0
    #while i < n1:
    #   i = i + 1

    for i in range(0,int(n1),1):

        L.append(arr[l + i])

    for j in range(0,n2,1):
        R[j] = arr[m + 1 + j]

    #Merge the temp arrays
    #Initial indexes of first and second subarrays
    i = 0
    j = 0

    #Initial index of merged subarry array
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i +1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1

    #Copy remaining elements of L[] if any
    while i < n1:
        arr[k] = L[i]
        i = i + 1
        k = k + 1

    #Copy remaining elements of R[] if any
    while j < n2:
        arr[k] = L[j]
        j = j + 1
        k = k + 1

#Main function that sorts arr[l..r] using merge()
def sort(arr:list,l,r):
    if l < r:

        #Find the middle point
        m = (l + r) / 2

        #Sort first and second halves
        arr = sort(arr, l, m)
        arr = sort(arr, m + 1, r)

        #merge the sorted halves
        arr = merge(arr,l ,m, r)

def main():
    i = 0
    arr = []

    while i <= random.randint(1, 10):
        arr.append(random.randint(1, 10))
        i = i + 1

    print(arr)
    arr = sort(arr, 0, len(arr)-1)
    print(arr)

main()







