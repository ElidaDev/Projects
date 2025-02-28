import java.util.Scanner;
class gan{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int secret = 7;
        int guess = scanner.nextInt();
        if (guess == secret){
            System.out.println("You win!");
        }
        else if (guess > secret){
            System.out.println("The number is lower than "+ guess);
        }
        else{
            System.out.println("The number is higher than "+ guess);
        }
        scanner.close();
    }
}