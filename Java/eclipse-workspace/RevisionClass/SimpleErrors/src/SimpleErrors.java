import java.util.Arrays;

public class SimpleErrors {

  public static void main(String[] args) {
    int[] numbers = {10,100,264,53};

    int max = numbers[0];
    int sum = 0;

    for (int i=0; i<numbers.length; i+=1) {
    	sum += numbers[i];
        if (numbers[i]>max) {
        	max = numbers[i];
        }
    }
    
    double mean = (double) sum / numbers.length;

    System.out.println(Arrays.toString(numbers));
    System.out.println("The largest number was " + Integer.toString(max) + ".");
    System.out.println("The mean was " + Double.toString(mean));

  }
}