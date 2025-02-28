import pyautogui
import time
import keyboard

c = input("Left Middle or Right click?")
x = int(input("X-Coordinate: "))
y = int(input("Y-Coordinate: "))
t = int(input("Amount of clicks: "))
s = float(input("Wait in seconds: "))

pyautogui.moveTo(x, y, duration=5)
if c == "Left":
    for z in range(t):
        time.sleep(s)
        pyautogui.leftClick(x, y)
        if keyboard.is_pressed('esc'):
            break
elif c == "Right":
    for z in range(t):
        time.sleep(s)
        pyautogui.rightClick(x, y)
        if keyboard.is_pressed('esc'):
            break
elif c == "Middle":
    for z in range(t):
        time.sleep(s)
        pyautogui.middleClick(x, y)
        if keyboard.is_pressed('esc'):
            break
else: 
    print("Incorrect input")