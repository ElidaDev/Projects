import pyautogui as pag
import time 
import keyboard

nummin = int(input("Start at number: "))
nummax = int(input("Stop at number: "))

time.sleep(5)
for number in range(nummin, nummax+1):
    if keyboard.is_pressed('q'):
        break
    pag.write(str(number))
    pag.press('enter')
