import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class LabWeek2Guesser {
  public static void main(String[] args) {
    final int MAX=100;
    final Random rand=new Random();
    final int target=rand.nextInt(MAX)+1; //We want a number up to AND including 100

    int count=0, guess=MAX+1;
    try (Scanner stdin=new Scanner(System.in)) {
      for ( ; guess!=target; ++count) { //No iterator declared, it has been previously
        System.out.print("Enter a guess: ");
        try {
          guess = stdin.nextInt();
          if (guess<1 || guess>MAX) {
	    throw new InputMismatchException();
	  }
        } catch (InputMismatchException e) {
          System.out.printf("You must only enter integers between 1 and %d%n",MAX);
	  stdin.nextLine();
	  continue;
	}
	if (guess>target) {
	  System.out.println("Guess was too big");
	} else if (guess<target) {
	  System.out.println("Guess was too small");
	}
      }
    }
    System.out.printf("Well done! You took %d guesses.",count);
  }
}