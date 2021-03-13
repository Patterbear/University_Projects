package co1105.week8.bwtfm1;

public class Cat extends Pet {

  public Cat(String n) {
    super(n);
  }

  public String speak() {
    return "Meow - "+super.speak();
  }
};