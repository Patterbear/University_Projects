package co1105.cw2.bwtfm1;

public class Sphere extends Solid {
	
	private int radius;
	
	Sphere(int r) throws InvalidSolidException {
		if (r < 0) {
			throw new InvalidSolidException("Radius must be > 0");
		}
		else {
				this.radius = r;
		}
	}
	
	Sphere(Sphere other) throws InvalidSolidException {
		if(other.radius < 0) {
			throw new InvalidSolidException("Radius must be > 0");
		} else {
			this.radius = other.radius;
		}
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (! (obj instanceof Sphere)) return false;
		Sphere other = (Sphere) obj;
		return this.radius == other.radius;
	}
	
	public double getRadius() {
		return this.radius;
	}

	@Override
	public double getSurface() {
		return 4.0 * Math.PI * (this.radius*this.radius);
	}

	@Override
	public double getVolume() {
		return (4.0/3) * Math.PI * (this.radius*this.radius*this.radius);
	}

	@Override
	public int hashCode() {
		int hash=this.radius*23;
		 return hash;
	}

	@Override
	public String toString() {
		return this.getClass().getSimpleName() + " " + this.getID() + ": r=" + Integer.toString((int)this.getRadius());
	}

}
