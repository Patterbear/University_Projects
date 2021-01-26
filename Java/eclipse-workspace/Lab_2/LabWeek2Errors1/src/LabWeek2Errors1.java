import java.util.InputMismatchException;
import java.util.Scanner;

public class LabWeek2Errors1 {
  public static void main (String[] args) {
    Scanner stdin = new Scanner(System.in);
    System.out.print("Enter some text: ");
    String text = stdin.nextLine();
    System.out.print("How many times? ");
    try {
      byte count = (byte) stdin.nextInt();
      for (int i=0; i<count; ++i) {
        System.out.println((i+1)+" "+text);
      }
    } catch (InputMismatchException e) {
      System.err.println("Error: Must be a number.");
      System.exit(1);
    }
    stdin.close();
  }
}