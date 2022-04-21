import os
import shutil

b = 2
g = 1

print('starting')



def movingB():
    ## move origin.file to destination.file
    shutil.copy("blue/image.png", "activeDuty")
def movingG():
    ## move origin.file to destination.file
    shutil.copy("green\image.png", "activeDuty")

def deleting():
    filepath = "activeDuty/image.png"
    try:
        os.remove(filepath)
    except OSError as error:
        print(error)
        print('error')

out = eval(input('green or blue(1 or 2)'))

if b == out:
    deleting()
    movingB()
    print('active duty is now blue')

else:
    deleting()
    movingG()
    print('active duty is now green')



print('ended')