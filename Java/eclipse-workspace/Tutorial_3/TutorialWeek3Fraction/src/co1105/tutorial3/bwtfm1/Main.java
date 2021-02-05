package co1105.tutorial3.bwtfm1;

public class Main {

	public static void main(String[] args) {
		Fraction f = new Fraction(2, 4);
		System.out.println(f);
		System.out.println(f.add(new Fraction(1, 4)));
		System.out.println(f.mult(new Fraction(1, 2)));
		System.out.println(f.div(new Fraction(1, 2)));
		System.out.println(f.sub(new Fraction(1, 4)));
		System.out.println(f.equals(new Fraction(1, 2)));
		System.out.println(f.equals(new Fraction(4, 5)));
		System.out.println(f.add(10));

	}

}
