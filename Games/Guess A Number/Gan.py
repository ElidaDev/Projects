import random

guesses = 5
secretNumber = random.randint(1,10)    
loop = True
x = 0
while x != secretNumber:
    while loop:
        try:
            print(f"You have {guesses} guesses left.")
            x = int(input("Number: "))
            loop = False
        except ValueError:
            print("Please insert an integer")
    if guesses >= 1:
        guesses -= 1
        if x > secretNumber:
            print("The number you guessed is bigger than the correct number!")
            loop = True
        elif x < secretNumber:
            print("The number you guessed is less than the correct number!")
            loop = True
        else:
            print("You got the number!")
    else:
        print("You ran out of guesses!")
        x = secretNumber
