import time
import keyboard


def countdown(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        if keyboard.is_pressed('esc'):
            break

t = int(input("Length in time in seconds: "))

countdown(int(t)) 