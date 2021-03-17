package co1105.cw2.bwtfm1;

import java.util.Arrays;

/**
 * Class to represent Cuboid 3D Object
 * @author bwtfm1
 *
 */
public class Cuboid extends Solid {
	
	//Attribute to represent the three dimensions of the cuboid (height/width/length) in a primitive int array
	private int [] dimensions = {0, 0, 0};
	
	//Constructor method (Default)
	//Takes in three parameters and puts them into an array called 'dimensions' which is then sorted (ascending)
	//Throws InvalidSolidException if any of the dimensions are less than 0
	Cuboid(int height, int width, int length) throws InvalidSolidException {
		if (height < 0 || width < 0 || length < 0) {
			throw new InvalidSolidException("All dimensions must be > 0");
		} else {
			this.dimensions[0] = height;
			this.dimensions[1] = width;
			this.dimensions[2] = length;
			
			Arrays.sort(this.dimensions);
		}
	}
	
	//Constructor method (Clone)
	//Clone method, uses other cuboid's 'dimension' array to set the new cuboid's dimensions
	//Throws InvalidSolidException if any of the values in 'dimensions' are less than 0
	Cuboid(Cuboid other) throws InvalidSolidException {
		if (other.dimensions[0] < 0 || other.dimensions[1] < 0 || other.dimensions[2] < 0) {
			throw new InvalidSolidException("All dimensions must be > 0");
		}
		this.dimensions = other.dimensions;
	}
	
	//'equals' method
	//Takes in 'Object' object, returns 'true' if other object passes certain tests, returns false otherwise
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Cuboid)) return false;
		Cuboid other = (Cuboid) obj;
		return this.dimensions == other.dimensions;
	}

	//Surface Area Getter method
	//Calculates the surface area from the values in 'dimensions' and returns it
	@Override
	public double getSurface() {
		return this.dimensions[0] * this.dimensions[1] * 2 + this.dimensions[0] * this.dimensions[2] * 2 + this.dimensions[1] * this.dimensions[2] * 2;
	}
	
	//Volume Getter method
	//Calculates the volume from the values in 'dimensions' and returns it
	@Override
	public double getVolume() {
		return this.dimensions[0] * this.dimensions[1] * this.dimensions[2];
	}

	//Hash Code method
	//Generates hash code based on object attributes
	@Override
	public int hashCode() {
		int hash=dimensions[0]*23;
		 hash = hash + 17*dimensions[1];
		 hash = hash + 17*dimensions[2];
		 return hash;
	}
	
	//'toString' method
	//Generates string output displaying object name and attributes
	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": " + this.dimensions[0] + "x" + this.dimensions[1] + "x" + this.dimensions[2];
	}

}
