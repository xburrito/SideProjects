// Albert Chang

class Main {
  public static void main(String[] args) {

    //Initiates the program
    System.out.println("Hello, are you ready to play the hi-lo game?");
    System.out.println();

    // Provides instructions
    System.out.println("INSTRUCTIONS: \nI am thinking of a random number in between 0-100. You make as many guesses as you need get to my number. I will hint at you whether your number inputted is higher or lower than mine.");
    System.out.println();

    // Calls the method from another class
    GuessMyNum game = new GuessMyNum();
    game.GuessMyNum();
  }
}
