package co1105.cw2.bwtfm1;

/**
 * Class to represent Sphere 3D Object
 * @author bwtfm1
 *
 */
public class Sphere extends Solid {
	
	//Attribute to store radius of sphere object
	private int radius;
	
	//Constructor method (Default)
	//Takes in int 'r' which is set as sphere's radius attribute
	//Throws InvalidSolidException if given radius is less than 0
	Sphere(int r) throws InvalidSolidException {
		if (r < 0) {
			throw new InvalidSolidException("Radius must be > 0");
		}
		else {
				this.radius = r;
		}
	}
	
	//Constructor method (Clone)
	//Clone method, uses other sphere's 'radius' attribute to set the new sphere's one
	//Throws InvalidSolidException if other radius is less than 0
	Sphere(Sphere other) throws InvalidSolidException {
		if(other.radius < 0) {
			throw new InvalidSolidException("Radius must be > 0");
		} else {
			this.radius = other.radius;
		}
	}
	
	//'equals' method
	//Takes in 'Object' object, returns 'true' if other object passes certain tests, returns false otherwise
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Sphere)) return false;
		Sphere other = (Sphere) obj;
		return this.radius == other.radius;
	}
	
	//Radius Getter method
	public double getRadius() {
		return this.radius;
	}
	
	//Surface Area Getter method
	//Calculates surface area using radius and pi and returns it
	@Override
	public double getSurface() {
		return 4.0 * Math.PI * (this.radius*this.radius);
	}
	
	//Volume Getter method
	//Calculates volume using radius and pi and returns it
	@Override
	public double getVolume() {
		return (4.0/3) * Math.PI * (this.radius*this.radius*this.radius);
	}

	//Hash Code method
	//Generates hash code based on object attributes
	@Override
	public int hashCode() {
		int hash=this.radius*23;
		 return hash;
	}
	
	//'toString' method
	//Generates string output displaying object name and attributes
	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": r=" + Integer.toString((int)this.getRadius());
	}

}
