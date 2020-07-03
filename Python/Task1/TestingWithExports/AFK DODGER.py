import keyboard
import time
time.sleep(10)


def circle():
    keyboard.press('w')
    time.sleep(5)
    keyboard.release('w')
    keyboard.press('a')
    time.sleep(5)
    keyboard.release('a')
    keyboard.press('s')
    time.sleep(5)
    keyboard.release('s')
    keyboard.press('d')
    time.sleep(5)
    keyboard.release('d')
def striaght():
    keyboard.press('w')
    time.sleep(10)
    keyboard.release('w')








while True:
    circle()
    time.sleep(5)


