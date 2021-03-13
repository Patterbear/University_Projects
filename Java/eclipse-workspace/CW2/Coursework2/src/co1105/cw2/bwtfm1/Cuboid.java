package co1105.cw2.bwtfm1;

import java.util.Arrays;

public class Cuboid extends Solid {
	
	private int [] dimensions = {0, 0, 0};
	
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
	
	Cuboid(Cuboid other) throws InvalidSolidException {
		if (other.dimensions[0] < 0 || other.dimensions[1] < 0 || other.dimensions[2] < 0) {
			throw new InvalidSolidException("All dimensions must be > 0");
		}
		this.dimensions = other.dimensions;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Cuboid)) return false;
		Cuboid other = (Cuboid) obj;
		return this.dimensions == other.dimensions;
	}

	@Override
	public double getSurface() {
	
		return this.dimensions[0] * this.dimensions[1] * 2 + this.dimensions[0] * this.dimensions[2] * 2 + this.dimensions[1] * this.dimensions[2] * 2;
	}

	@Override
	public double getVolume() {
		return this.dimensions[0] * this.dimensions[1] * this.dimensions[2];
	}

	@Override
	public int hashCode() {
		int hash=dimensions[0]*23;
		 hash = hash + 17*dimensions[1];
		 hash = hash + 17*dimensions[2];
		 return hash;
	}

	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": " + this.dimensions[0] + "x" + this.dimensions[1] + "x" + this.dimensions[2];
	}

}
