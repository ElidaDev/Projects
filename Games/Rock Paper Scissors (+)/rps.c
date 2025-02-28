#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char selection(){
    srand(time(0));
    int computer = rand() % 3;
    switch (computer){
        case 0:
            computer = 'r';
            break;
        case 1:
            computer = 'p';
            break;
        case 2:
            computer = 's';
            break;
        default:
            printf("There was an error while selecting the computer's choice... ");
            return 1;
    }
    return computer;
}

const char* checkWinner(char user, char computerSelection){
    printf("The computer chose %c!\n", computerSelection);
    if (computerSelection != user){
        if (computerSelection == 'r'){
            if (user == 's'){return("Loss");}
            else{return("Win");}
        }
        else if (computerSelection == 'p'){
            if (user == 'r'){return("Loss");}
            else{return("Win");}
        }
        else{
            if (user == 'p'){return("Loss");}
            else{return("Win");}
        }
    }
    else{
        return("Draw");
    }
}
int main(){
    char computerSelection = selection(); 
    char user;
    printf("Please enter your choice: (r/p/s) ");
    scanf("%c",&user);
    printf("%s",checkWinner(user, computerSelection));
    return 0;
}