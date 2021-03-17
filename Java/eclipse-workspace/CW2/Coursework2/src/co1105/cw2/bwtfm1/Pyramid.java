package co1105.cw2.bwtfm1;

/**
 * Class to represent Pyramid 3D Object
 * @author bwtfm1
 *
 */
public class Pyramid extends Solid {
	
	//Attribute to store base of pyramid
	private int base;
	
	//Attribute to store height of pyramid
	private int height;
	
	//Constructor method (Default)
	//Takes in int 'base' and 'height which are set as the pyramid's base and height attributes
	//Throws InvalidSolidException if given base or height is less than 0
	Pyramid(int base, int height) throws InvalidSolidException {
		if (base < 0 || height < 0) {
			throw new InvalidSolidException("Base and height must be > 0");
		} else {
			this.base = base;
			this.height = height;
		}
	}
	
	//Constructor method (Clone)
	//Clone method, uses other pyramid's 'base' and 'height' attributes to set the new pyramid's ones
	//Throws InvalidSolidException if other base or height is less than 0
	Pyramid(Pyramid other) throws InvalidSolidException {
		if (other.base < 0 || other.height < 0) {
			throw new InvalidSolidException("Base and height must be > 0");
		} else {
			this.base = other.base;
			this.height = other.height;
		}
	}
	
	//'equals' method
	//Takes in 'Object' object, returns 'true' if other object passes certain tests, returns false otherwise
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Pyramid)) return false;
		Pyramid other = (Pyramid) obj;
		return this.base == other.base && this.height == other.height;
	}
	
	//Surface Area Getter method
	//Calculates surface area from base and height and returns it
	@Override
	public double getSurface() {
		return this.base * this.base + 2 * this.base * this.height;
	}

	//Surface Area Getter method
	//Calculates volume from base and height and returns it
	@Override
	public double getVolume() {
		return this.base * this.base * this.height / 3.0;
	}

	//Hash Code method
	//Generates hash code based on object attributes
	@Override
	public int hashCode() {
		int hash=this.height*23;
		 hash = hash + 17*this.base;
		 return hash;
	}
	
	//'toString' method
	//Generates string output displaying object name and attributes
	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": " + this.base + "x" + this.height;
	}

}
