import java.util.Random;
import java.util.Scanner;

public class RPSLSGame {
    public static void main(String[] args) {
        
        boolean exit = false;
        int wins = 0;
        int loses = 0;
        int draws = 0;
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        while (!exit) {
            int compchoice = random.nextInt(5); // 0-4
            String compchoiceopt = new String();
            switch (compchoice){
                case 0: compchoiceopt = "Scissors"; break;
                case 1: compchoiceopt = "Rock"; break;
                case 2: compchoiceopt = "Paper"; break;
                case 3: compchoiceopt = "Lizard"; break;
                case 4: compchoiceopt = "Spock"; break;
            }
            System.out.println("0 is scissors, 1 is rock, 2 is paper, 3 is lizard, 4 is spock ");
            int choice;
            String choiceopt = new String();

            
            try {
                System.out.print("Select a number 0-4: ");
                choice = Integer.parseInt(scanner.nextLine());
                switch (choice){
                case 0: choiceopt = "Scissors"; break;
                case 1: choiceopt = "Rock"; break;
                case 2: choiceopt = "Paper"; break;
                case 3: choiceopt = "Lizard"; break;
                case 4: choiceopt = "Spock"; break;
                }
            } catch (Exception e) {
                continue;
            }

            

            int winner = 0;
            // 1 = player win, 2 = comp win, 3 = draw
            if (choice == 0) {
                if (compchoice == 2 || compchoice == 3) {
                    winner = 1;
                } else if (compchoice == 1 || compchoice == 4) {
                    winner = 2;
                } else {
                    winner = 3;
                }
            } else if (choice == 1) {
                if (compchoice == 3 || compchoice == 0) {
                    winner = 1;
                } else if (compchoice == 4 || compchoice == 2) {
                    winner = 2;
                } else {
                    winner = 3;
                }
            } else if (choice == 2) {
                if (compchoice == 1 || compchoice == 4) {
                    winner = 1;
                } else if (compchoice == 3 || compchoice == 0) {
                    winner = 2;
                } else {
                    winner = 3;
                }
            } else if (choice == 3) {
                if (compchoice == 2 || compchoice == 4) {
                    winner = 1;
                } else if (compchoice == 0 || compchoice == 1) {
                    winner = 2;
                } else {
                    winner = 3;
                }
            } else if (choice == 4) {
                if (compchoice == 1 || compchoice == 0) {
                    winner = 1;
                } else if (compchoice == 2 || compchoice == 3) {
                    winner = 2;
                } else {
                    winner = 3;
                }
            }

            if (winner == 3) {
                System.out.println("Draw " + compchoiceopt + " vs " + choiceopt);
                draws++;
            } else if (winner == 2) {
                System.out.println("Computer wins " + compchoiceopt + " vs " + choiceopt);
                loses++;
            } else if (winner == 1) {
                System.out.println("You win! " + compchoiceopt + " vs " + choiceopt);
                wins++;
            } else {
                System.out.println("You lose, you can't seem to type...");
            }

            System.out.print("Would you like to exit? (y/n) ");
            String response = scanner.nextLine();
            if (response.equals("y")) {
                exit = true;
            } else {
                exit = false;
            }
        }
        scanner.close();
        System.out.println("\nWins : " + wins);
        System.out.println("Loses: " + loses);
        System.out.println("Draws: " + draws);
    }
}
