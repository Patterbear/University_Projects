package co1105.week8.bwtfm1;

import java.time.LocalDate;

public class Person {
  private String name;
  private LocalDate dateOfBirth;
  private double weight;
  
  public Person (String name, LocalDate dob, double w) {
    this.name = name;
    dateOfBirth = dob;
    weight = w;
  }
  
  public String getName() {
    return name;
  }
  
  public LocalDate getDateOfBirth () {
    return dateOfBirth;
  }
  
  public int getAgeOn (LocalDate d) {
    return (int) java.time.temporal.ChronoUnit.YEARS.between(dateOfBirth, d);
  }
  
  public double getWeight () {
    return weight;
  }
  
  public String toString () {
    return name+" ("+getAgeOn(LocalDate.now())+") "+weight;
  }
}