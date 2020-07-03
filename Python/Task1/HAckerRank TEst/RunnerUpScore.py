if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    MaxValue = 0
    print(arr)
    for i in range(n):
        if MaxValue < arr[i]:
            MaxValue = arr[i]

    for i in range(n):
        if MaxValue in arr:
            arr.remove(MaxValue)
            n = n-1

    MaxValue = 0
    for i in range(n):
        if MaxValue < arr[i]:
            MaxValue = arr[i]





    print(arr)
    print(MaxValue)