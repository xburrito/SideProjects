// Albert Chang

// Importing necessary libraries
import java.util.Random;
import java.util.Scanner;

public class GuessMyNum{
  public static void GuessMyNum(){

    // Method within class initiates
    System.out.println("I am thinking of a number in between 0 - 100.");

    // Initiates imported libraries
    Random num = new Random();
    Scanner input = new Scanner(System.in);

    // Creates the random integer as well as setting boundaries between 0-100
    int low = 0;
    int high = 100;
    int guessMe = num.nextInt(high-low) + low;

    System.out.print("Enter a guess: ");
    int value = input.nextInt();

    // Counter initiates at 1 because first guess is made upon input!
    int counter = 1;

    // We enter this loop that will keep asking user to make guesses if they are wrong...
    while(value != guessMe){
      if (value < guessMe){
      System.out.println("No, my number is higher than " + value);
      }
      else if(value > guessMe){
      System.out.println("Nope! My number is lower than " + value);
      }
      System.out.print("Enter a guess: ");

      // Counter increments for every incorrect guess until the correct one
      counter++;
      value = input.nextInt();
    }

    // End of while loop message (YAY)
    System.out.println();
    System.out.println("Wow! You won in " + counter + " guesses!");

    // Prompts the user if they want to play again or not
    System.out.print("Would you like to play again? Type 'y' for yes or 'n' for no: ");
    char choice = input.next(".").charAt(0);


    // Program will be called again recursively if user wants to play again. Else, it will quit and program ends entirely...
    if(choice == 'y'){
      GuessMyNum();
    }
    else{
      System.out.println();
      System.out.println("Ending program....");
    }
  }
}
