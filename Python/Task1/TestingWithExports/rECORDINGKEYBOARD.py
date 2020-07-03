import threading
import mouse
import keyboard

mouse_events = []

keyboard.wait("esc")

mouse.hook(mouse_events.append)
keyboard.start_recording()

keyboard.wait("esc")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()

#Keyboard threadings:

k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))


#Mouse threadings:

m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))


#Start threads
k_thread.start()
m_thread.start()

#waiting for both threadings to be completed

k_thread.join()
m_thread.join()