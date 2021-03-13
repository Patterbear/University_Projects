package co1105.cw2.bwtfm1;

import java.lang.Comparable;

/**
 * Abstract class to represent Solids.
 */
abstract class Solid implements Comparable<Solid> {
	
	private static int solidCount = 0;
	private final int solidID;
	
	public Solid() {
		this.solidID = Solid.solidCount;
		Solid.solidCount += 1;
		
	}
	
	public int getID() {
		return Solid.solidCount;
	}
  abstract public double getSurface();
  abstract public double getVolume();
  abstract public boolean equals (Object other);
  abstract public int hashCode();
  abstract public String toString();

  public int compareTo (Solid other) {
	  if (this.getSurface() > other.getSurface()) {
		  return (int) (this.getSurface() - other.getSurface());
	  } else if (this.getSurface() < other.getSurface()) {
		  return (int) (other.getSurface() - this.getSurface());
	  } else {
		  return 0;
	  }
  }
}
