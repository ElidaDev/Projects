
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class GuessANumber {
    /*
     * 
     * Problem 3: Guess the Number Game
This is a classic programming challenge that combines loops, conditionals, and a bit of randomness to create a fun and interactive game.
Objective: Write a program where the user first chooses one of two modes:
Computer Guesses: The user thinks of a number between 1 and 100, and the computer must guess it. The computer MUST use a binary search algorithm to find the number in the fewest guesses possible.

Algorithm Idea:

For Computer Guesses:
Prompt the user to think of a number between 1 and 100.
Set up a range with a low value (1) and a high value (100).
Use a while loop that continues until the number is found.
Inside the loop, the computer's guess is the midpoint of the current range by calling the computerGuess(low, high) method.
Ask the user if the guess is "correct," "too high," or "too low."
Based on the user's feedback, adjust the low or high value to narrow the search range. For example, if the guess was "too low," set low to the guess plus one.
Keep a counter to track the number of computer guesses.
Once the computer guesses correctly, congratulate the computer and show the total guesses.


     */
    //Contains all the logic for the player guessing mode.
    public static void main(String[] args) {
        computerGuessesTheNumber();
    }
    public static void playerGuessesTheNumber() {
        ArrayList<Integer> prevGuesses = new ArrayList<Integer>();
        Random rand = new Random();
        int secret = rand.nextInt(1,100);
        int guess = Integer.MIN_VALUE;
        int guesses = 0;
        while (guess != secret) { 
            guess = userGuess(prevGuesses, secret, secret);
            guesses++;
            if (guess == secret){
                System.out.println("Previous guesses: ");
                for (int i = 0; i < prevGuesses.size(); i++) {
                    System.out.println((int) prevGuesses.get(i));
                }
                System.out.printf("YOU WON! The number was %d, you guessed it in %d guesses", secret,guesses);
            } else if (guess > secret){
                System.out.printf("The secret number is less than %d\n",guess);
            }else{
                System.out.printf("The secret number is greater than %d\n",guess);
            }
        }
        

    }

    //Contains all the logic for the computer guessing mode.
    public static void computerGuessesTheNumber() {
        //ask user to think of a number and input the high and low range  
        Scanner ui = new Scanner(System.in);
        int guesses = 0;
        System.out.println("Input the minimum number in the range");
        int rangeLow = Integer.parseInt(ui.nextLine());
        System.out.println("Input the maximum number in the range");
        int rangeHigh = Integer.parseInt(ui.nextLine());
        System.out.println("Think of a number between the given range...");
        boolean isCorrect = false;
        while(!isCorrect){
            int guess = computerGuess(rangeLow, rangeHigh);
            guesses++;
            System.out.printf("Hmmm.... I guess %d is that right?", guess);
            String userInput = new String();
            while (!(userInput.equalsIgnoreCase("Low") || userInput.equalsIgnoreCase("High") || userInput.equalsIgnoreCase("Correct"))){
                System.out.println("Please enter Low,High, or Correct: ");
                userInput = ui.nextLine();
                if (userInput.equalsIgnoreCase("Low")){
                    rangeLow = guess + 1;
                    System.out.println("Ok, so if it's higher than that...");
                }else if (userInput.equalsIgnoreCase("High")){
                    System.out.println("Ok, so if it's lower than that...");
                    rangeHigh = guess - 1;
                }else if (userInput.equalsIgnoreCase("Correct")){
                    System.out.printf("I WIN! In %d guesses",guesses);
                    isCorrect = true;
                }
            }
        }    
    }
        //Performs a single step of the binary search, returning the next guess.
    public static int computerGuess(int low, int high){
        // if we only have one option use it
        if (low == high){
            return low;
        }
        double midpoint = (low+high)/2;
        midpoint = Math.round(midpoint);

        return (int) midpoint;
    }
    //Prompts the user for a guess and validates that the input is an integer before returning it.
    public static int userGuess(ArrayList<Integer> prevGuesses,int rangeHigh, int rangeLow){
        Scanner ui = new Scanner(System.in);
        int guess = Integer.MIN_VALUE;
        boolean isValid = false;
        while(!isValid){
            System.out.printf("\nPlease enter a guess from %d-%d:",rangeLow,rangeHigh);
            guess = Integer.parseInt(ui.nextLine());
            // check if guess is in range
            if (!((guess > rangeHigh) && (guess < rangeLow))){
                if (!prevGuesses.contains(guess)){
                    isValid = true;
                }else{
                    System.out.printf("You have guessed %d before...", guess);
                }
            }else{
                System.out.printf("You have guessed %d the range is %d to %d", guess,rangeLow,rangeHigh);
            }
        }
        prevGuesses.add(guess);
        return guess;
    }



}
