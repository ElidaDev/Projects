import pyautogui
import time
import keyboard

p = input("Phrase: ")
t = int(input("Amount of times to repeat."))
w = float(input("Wait between typing: "))

time.sleep(10)
for i in range(t):
    pyautogui.write(p)
    time.sleep(w)
    if keyboard.is_pressed('esc'):
        break
