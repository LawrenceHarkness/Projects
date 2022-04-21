import time
import keyboard
import random
off = 0
i = 0
time.sleep(3)
while i < 89:
    keyboard.press('e')
    time.sleep(0.15)
    keyboard.release('e')

    time.sleep(random.randint(11,12))

    i = i + 1
    print(i)

