import keyboard
import time

time.sleep(5)

events = keyboard.record(until='escape', suppress=False, trigger_on_release=False)
keyboard.play(events, speed_factor=2.0)
