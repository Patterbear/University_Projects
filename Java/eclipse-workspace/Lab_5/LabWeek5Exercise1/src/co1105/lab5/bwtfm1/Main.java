package co1105.lab5.bwtfm1;

public class Main {

	public static void main(String[] args) {
	    int[] numbers = {10, 15, 12, 10};
	    int totalBefore=sum(numbers);
	    System.out.println(totalBefore);
	    doubleMe(numbers);
	    int totalAfter=sum(numbers);
	    System.out.println(totalAfter);
	    doubleMeBroken(numbers);
	    totalAfter=sum(numbers);
	    System.out.println(totalAfter);
		

	}
	
	static void doubleMe (int[] vals) {
	      for (int i=0; i<vals.length; ++i) {
	        vals[i]*=2;
	      }
	      return;
	    }
	
	static void doubleMeBroken (int[] vals) {
		for (int v : vals) {
			v*=2;
	    }
		return;
	}

	static int sum (int[] numbers) {
		int sum = 0;
		for (int i=0; i<numbers.length;i++) {
			sum += numbers[i];
		}
		return sum;
		
	}


}
