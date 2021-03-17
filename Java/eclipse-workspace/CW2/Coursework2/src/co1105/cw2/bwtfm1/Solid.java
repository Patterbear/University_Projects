package co1105.cw2.bwtfm1;

import java.lang.Comparable;

/**
 * Abstract class to represent Solids.
 */
abstract class Solid implements Comparable<Solid> {
	
	//Stores the number of solid objects created
	private static int solidCount = 0;
	
	//Gives unique ID to new Solids created
	private final int solidID;
	
	//Constructor(No Parameters)
	//Assigns 'solidID' field based on solidCount attributes, then increments it by 1.
	public Solid() {
		this.solidID = Solid.solidCount;
		Solid.solidCount += 1;
		
	}
	
	//ID Getter method
	//Returns the 'solidCount' field
	public int getID() {
		return Solid.solidCount;
	}
	
	//Surface Area Getter method
  abstract public double getSurface();
  
//Volume Getter method
  abstract public double getVolume();
  
  //Equals method
  //Takes in type 'Object'
  abstract public boolean equals (Object other);
  
  //Hash Code Method
  abstract public int hashCode();
  
  //toString method
  abstract public String toString();

  //Comparison method
  //Takes in 'Solid' object
  //Returns the (positive) difference between the surface areas of two 'Solid' objects.
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
