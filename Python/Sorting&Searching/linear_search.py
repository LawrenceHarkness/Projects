import time


def BinarySearch(Array,NS):
    Array.sort()
    High = len(Array) - 1
    Low = 0
    Mid = 0
    while Low <= High:
        Mid = (High + Low) // 2
        if Array[Mid] < NS:
            Low = Mid + 1
        elif Array[Mid] > NS:
            High = Mid - 1
        else:
        #elif Array[Mid] == NS:
            print("Found")
            return(Array)
    Array.append(NS)
    print("Value Not Found")
    return(Array)
def linearSearch(Array,NS):

    NSF = False


    for i in Array:
        if i == NS:
            print("found")
            NSF = True
    if NSF == False:
        print("Not found adding name")
        Array.append(NS)
    return(Array)



def writeN(Array,FN):
    with open(FN,mode='w') as f:
        f.write('\n'.join(Array))



def file_read(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line.replace('\n',''))


    return content_array

Array = file_read('list.txt')
NS = input("Enter name")
start_time = time.time()
Array = linearSearch(Array,NS)
print("--- Linear %s seconds ---" % (time.time() - start_time))

start_time = time.time()
Array = BinarySearch(Array,NS)
print("--- Binary %s seconds ---" % (time.time() - start_time))

writeN(Array,"list.txt")

