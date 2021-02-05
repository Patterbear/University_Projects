package co1105.tutorial3.bwtfm1;

public class Fraction {
	public int numerator;
	public int denomenator;
	
	public Fraction(int n, int d) {
		this.numerator = n;
		this.denomenator = d;
	}
	
	public String toString() {
		return this.numerator + "/" + this.denomenator;
	}
	
	public Fraction add(Fraction f) {

		int d = this.denomenator*f.denomenator;
		int n = (this.numerator*f.denomenator) + (f.numerator*this.denomenator);
		
		return new Fraction(n, d).simplify();
		
	}
	
	public Fraction add(int a) {
		int d = this.denomenator*1;
		int n = (this.numerator*1) + (a*this.denomenator);
		
		return new Fraction(n, d).simplify();
	}
	
	public Fraction sub(Fraction f) {
		int d = this.denomenator*f.denomenator;
		int n = (this.numerator*f.denomenator) - (f.numerator*this.denomenator);
		
		return new Fraction(n, d).simplify();
	}
	
	public Fraction mult(Fraction f) {
		int d = this.denomenator * f.denomenator;
		int n = this.numerator * f.numerator;
		
		return new Fraction(n, d).simplify();
	}
	
	public Fraction div(Fraction f) {
		int d = this.denomenator * f.numerator;
		int n = this.numerator * f.denomenator;
		
		return new Fraction(n, d).simplify();
	}
	
	public Fraction simplify() {
		int gcd = gcd(this.numerator, this.denomenator);
	    return new Fraction((this.numerator / gcd), (this.denomenator / gcd));
	}
	
	public int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a % b);
	}
	
	public Boolean equals(Fraction f) {
		if (this.simplify().denomenator == f.simplify().denomenator && this.simplify().numerator == f.simplify().numerator) {
			return true;
		} else {
			return false;
		}
	}
	
	
}




