package co1105.tutorial2.bwtfm1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class TutorialWeek3Worksheet {

	public static void main(String[] args) {
		
	//Question 1
		String [][] types = {
				{"boolean", "true/false"},
				{"byte", "-128-127"},
				{"char", "unicode characters"},
				{"short", "-32768-32767 "},
				{"int", "+/- 2 billion"},
				{"float", "24 bits of precision"},
				{"long", "+/- 9 quintillion"},
				{"double", "54 bits of precision"}
		};
		
		System.out.println(Arrays.deepToString(types));
		
		//Question 2
		int i1=10, i2=0, i3=0b11011, i4=0111, i5=0xFF;
		long l1=0L, l2=0xFF4689L, l3=-i5;
		float f1=341.987f, f2=-26e-14F;
		double d1=f1, d2=0.00006;
		char c1='ö', c2='\u26C8';
		
		byte b1=(byte) 0177, b2=(byte) 230;
		short s1=(short) -521;
		
		System.out.println(i1);
		System.out.println(i2);
		System.out.println(i3);
		System.out.println(i4);
		
		System.out.println(l1);
		System.out.println(l2);
		System.out.println(l3);
		
		System.out.println(f1);
		System.out.println(f2);
		
		System.out.println(d1);
		System.out.println(d2);
		
		System.out.println(c1);
		System.out.println(c2);
		
		System.out.println(b1);
		System.out.println(b2);
		
		System.out.println(s1);
		
		//Question 3
		//int i1='a'; - Character cannot be assigned to an integer variable
	    //int i2=0L; - Cannot convert from 'long' to 'int'
	    //short  s1=(short) true; - A boolean value cannot be cast to a 'short'
	    //short  s2=-46; - No error
	    //int i3=-46; short s3=i3; - 'int' and 'short' are incompatible
	    //long 2power10=1024L; - Variable name cannot begin with a number
		
		//Question 4
		int[] numbers = new int[5];
		double[] morenums = new double[5];
		char[] chars = new char[5];
		boolean[] bools = new boolean[5];
		
		System.out.println(Arrays.toString(numbers));
		System.out.println(Arrays.toString(morenums));
		System.out.println(Arrays.toString(chars));
		System.out.println(Arrays.toString(bools));
		
		//Question 5
		String str1="The quick brown fox jumps over the lazy dog";
		//String str2=str1[0:5]; - Error, Java does not support this type of string slicing
		String[] strs1=str1.split(" ");
		int len=strs1.length;
		String str3=strs1[2].substring(1, 4);
		
		System.out.println(str1);
		//System.out.println(str2); - Error, str2 is not defined as its assignment is invalid
		System.out.println(Arrays.toString(strs1));
		System.out.println(len);
		System.out.println(str3);
		
		//Question 6
		Scanner grade_in = new Scanner(System.in);
		char ch= grade_in.nextLine().charAt(0);
		grade_in.close();
		String feedback;
		
		if (ch=='A') {
			feedback="Perfect";
		} else if (ch=='B') {
			feedback="Very good";
		} else if (ch=='C') {
			feedback="OK";
		} else if ((ch=='D') || (ch=='E')) {
			feedback="Room for improvement";
		} else {
			feedback="Fail";
		}
		
		System.out.println(ch);
		System.out.println(feedback);
		
		switch(ch) {
		case 'A':
			feedback = "Perfect";
			break;
		case 'B':
			feedback = "Very good";
			break;
		case 'C':
			feedback="OK";
			break;
		case 'D': case 'E':
			feedback="Room for improvement";
			break;
		default:
			feedback="Fail";
		}
		
		System.out.println(ch);
		System.out.println(feedback);
		
		//Question 7	
		//My answer:
		for (int i=100; i>=0; i--) {
			   System.out.println(i);
			 }
		
		//Solution (Doesn't count down to 0, so is incorrect):
		 for (int i=100; i>-0; --i) {
			   System.out.println(i);
			 }
		 
		 //Question 8
		 for (int i=0, d=1; i<=50; i+=d, d*=2) {
			 System.out.println(i);
		 }
		 
		 //Question 9
		 String str="The quick brown fox jumps over the lazy dog";
		 String[] strs=str.split("\\s");
		 for (String w : strs) {
		   System.out.println(w);
		 }
		 
		 //Question 10
		 //My solution:
		 ArrayList<Character> temp = new ArrayList<Character>();
		 for (int i=0; i <= strs.length-1; i++) {
			// System.out.println(strs[i]);
			 for(int j=1; j < strs[i].length(); j+=2) {
				 //System.out.println(strs[i].charAt(j));
				 temp.add(strs[i].charAt(j));
			 }
		 }
		 
		 Object[] oddChars = temp.toArray();
		 System.out.println(Arrays.toString(oddChars));
		 
		 //Solution (Includes spaces, so not correct)
		 char[] oddCharsS = new char[str.length()/2];
		 for (int i=0; i<str.length()/2; ++i) {
		   oddCharsS[i] = str.charAt(1+i*2);
		 }
		 System.out.println(Arrays.toString(oddCharsS));
		 
		 //Question 11
		 //Doesn't function as c is independent of the loop, changing its value does nothing.
		 char[] chs=new char[10];
		 for (char c : chs) {
		   c='x';
		 }
		 
		 
	}
		

}
