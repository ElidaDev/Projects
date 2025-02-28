import random
print('''
#Scissors beats

paper, lizard

#Paper beats

Rock, Spock

#Rock beats

Lizard, Scissors

#Lizard beats

Paper, Spock

#Spock beats

Rock, Scissors
'''
)
exit = False
wins = 0
loses = 0
draws = 0
while(not exit):
    compchoice = random.randint(0,4)
    print("0 is scissors, 1 is rock, 2 is paper, 3 is lizard, 4 is spock ")
    try:    
        choice = int(input("Select a number 0-4: "))
    except:
        continue
    winner = 0
    # 1 = player win, 2 = comp win, 3 = draw
    if choice == 0:
        if compchoice == 2 or compchoice == 3:
            winner = 1
        elif compchoice == 1 or compchoice == 4:
            winner = 2
        else:
            winner = 3
    elif choice == 1:
        if compchoice == 3 or compchoice == 0:
            winner = 1
        elif compchoice == 4 or compchoice == 2:
            winner = 2
        else:
            winner = 3
    elif choice == 2:
        if compchoice == 1 or compchoice == 4:
            winner = 1
        elif compchoice == 3 or compchoice == 0:
            winner = 2
        else:
            winner = 3
    elif choice == 3:
        if compchoice == 2 or compchoice == 4:
            winner = 1
        elif compchoice == 0 or compchoice == 1:
            winner = 2
        else:
            winner = 3
    elif choice == 4:
        if compchoice == 1 or compchoice == 0:
            winner = 1
        elif compchoice == 2 or compchoice == 3:
            winner = 2
        else:
            winner = 3
    if winner == 3:
        print(f"Draw {compchoice} vs {choice}")
        draws += 1
    elif winner == 2:
        print(f"Computer wins {compchoice} vs {choice}" )
        loses += 1
    elif winner == 1:
        print(f"You win! {compchoice} vs {choice}")
        wins += 1
    else:
        print(f"You lose, you can't seem to type...")
    
    exit = input("Would you like to exit? (y/n) ")
    if exit == "y":
        exit = True
    else: 
        exit = False
print(f'''
Wins : {wins}
Loses: {loses}
Draws: {draws}
''')