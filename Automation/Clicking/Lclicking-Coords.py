import pyautogui
import keyboard
import time

clicktype = input("Left, Right or Middle click: ")
t = float(input("Wait time between clicks: "))  
m = float(input("Move to time: "))
loops = int(input("Times to go through the loop: "))
a = int(input("Amount of times to click each spot: "))
xs = []
ys = []

while True:
    print("put Done when done with positions")
    x = input("X of location: ")
    if x == "Done" :
        break
    else:
        xs.append(int(x))
        ys.append(int(input("Y of location: ")))

for i in range(loops):
    print ("Clicking...")
    n = len(xs)+1
    while n > 0:
        print(xs[n-1], ys[n-1])
        pyautogui.moveTo(xs[n-1], ys[n-1], duration=m)
        for i in range(a):
            time.sleep(t)
            if clicktype == "Left":
                pyautogui.leftClick
            elif clicktype == "Middle":
                pyautogui.middleClick
            elif clicktype == "Right":
                pyautogui.rightClick
            if keyboard.is_pressed('esc'):
                break
        n -= 1
        if keyboard.is_pressed('esc'):
            break