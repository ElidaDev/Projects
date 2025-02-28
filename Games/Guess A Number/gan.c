#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    srand(time(NULL));
    int r = rand() % 9;
    int secretNumber = r+1;
    int guess;
    int guesses = 5;
    int loop = 1;
    while(loop == 1){
        printf("\nYou have %d", guesses);
        printf(" guesses left!\n");
        printf("Enter a number between 1 and 10: ");
        scanf("%d", &guess);
        guesses -= 1;
        if(guesses > 0){
            if (guess == secretNumber){printf("You guessed the number!"); loop = 0;}
            else if (guess < secretNumber){printf("The number is higher than %d\n", guess);}
            else{printf("The number is lower than %d\n", guess);}
        }
        else{
            if (guess == secretNumber){printf("You guessed the number on your final guess! %d\n", secretNumber); loop = 0;}
            else{printf("You lose!");loop = 0;}
        }
    }
    return 0;
}