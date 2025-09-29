
import java.util.Random;
import java.util.Scanner;

public class ganv3 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int guess = -1;
        int lives = 3;
        int secret = random.nextInt(0,10);
        while (guess != secret){ 
            if (lives <= 0){
                System.out.println("You lose...");
                break;
            }
            System.out.println("Guess a number: ");
            guess = scanner.nextInt();
            lives -= 1;
            if (guess == secret){
                System.out.println("You win!");
            }
            else if (guess > secret){
                System.out.println("The number is lower than "+ guess);
            }
            else{
                System.out.println("The number is higher than "+ guess);
            }
        }
        scanner.close();
    }    
}
