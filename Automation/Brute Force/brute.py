import pyautogui as pag
import keyboard as kbrd
import time
import itertools

passw = "0000"
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = int(input("How many digits are in the code? "))
entryMethod = "Type" # Type or Test
maxValue = int("9" * digits)

#pos = [pag.locateCenterOnScreen('0.jpg'), pag.locateCenterOnScreen('1.jpg'), pag.locateCenterOnScreen('2.jpg'), pag.locateCenterOnScreen('3.jpg'), pag.locateCenterOnScreen('4.jpg'), pag.locateCenterOnScreen('5.jpg'), pag.locateCenterOnScreen('6.jpg'), pag.locateCenterOnScreen('7.jpg'), pag.locateCenterOnScreen('8.jpg'), pag.locateCenterOnScreen('9.jpg')]
enterneeded = True
#ex, ey = pag.locateCenterOnScreen('enter.jpg')
time.sleep(5)
typingSpeed = 0.01

def simulate_typing(code):
    print("Typed: ", code)
    return code == passw

if entryMethod == "Typef":
    for i in range(maxValue + 1): 
        if kbrd.is_pressed('q'):
            break
        code = str(i).zfill(digits)
        print("Typed: ", code)
        for digit in code:
            if kbrd.is_pressed('q'):
                break
            kbrd.press(digit)
            if entryMethod == "Typef":
                time.sleep(0.00001)
            else:
                time.sleep(typingSpeed)
            kbrd.release(digit)
        kbrd.press_and_release('enter')


# if entry_method == "Click":
#     combinations = list(itertools.permutations(pos))
#     for combo in combinations:
#         if kbrd.is_pressed('q'):
#             break
#         for position in combo:
#             if kbrd.is_pressed('q'):
#                 break
#             x, y = position
#             pag.click(x, y)
#         if enterneeded == True:
#             pag.click(ex, ey)

if entryMethod == "Test":
    start_time = time.time()
    for i in range(maxValue + 1):
        if kbrd.is_pressed('q'):
            break
        code = str(i).zfill(digits)
        if simulate_typing(code):
            end_time = time.time()
            elapsed_time = end_time - start_time
            if code == passw:
                print(f"Guessed the correct password in {elapsed_time:.2f} seconds.")
            break