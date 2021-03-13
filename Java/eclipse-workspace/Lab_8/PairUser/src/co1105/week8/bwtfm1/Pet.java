package co1105.week8.bwtfm1;

public class Pet implements Comparable<Pet> {
  private final String name;
  public Pet(String n) {
    name = n;
  }
  public String getName() {
    return name;
  }
  public String speak() {
    return "I'm "+name;
  }
  public int compareTo(Pet other) {
    return this.name.compareTo(other.name);
  }
  public String toString() {
    return speak();
  }
}