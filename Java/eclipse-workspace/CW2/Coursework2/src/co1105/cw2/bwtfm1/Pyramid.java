package co1105.cw2.bwtfm1;

public class Pyramid extends Solid {
	
	private int base;
	private int height;
	
	Pyramid(int base, int height) throws InvalidSolidException {
		if (base < 0 || height < 0) {
			throw new InvalidSolidException("Base and height must be > 0");
		} else {
			this.base = base;
			this.height = height;
		}
	}
	
	Pyramid(Pyramid other) throws InvalidSolidException {
		if (other.base < 0 || other.height < 0) {
			throw new InvalidSolidException("Base and height must be > 0");
		} else {
			this.base = other.base;
			this.height = other.height;
		}
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Pyramid)) return false;
		Pyramid other = (Pyramid) obj;
		return this.base == other.base && this.height == other.height;
	}
	
	@Override
	public double getSurface() {
		return this.base * this.base + 2 * this.base * this.height;
	}

	@Override
	public double getVolume() {
		return this.base * this.base * this.height / 3.0;
	}

	@Override
	public int hashCode() {
		int hash=this.height*23;
		 hash = hash + 17*this.base;
		 return hash;
	}

	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": " + this.base + "x" + this.height;
	}

}
