package co1105.week8.bwtfm1;

import java.time.LocalDate;

public class PairUser {

  public static void main(String[] args) {
    Pair<Person,Pet> pr1 =
      new Pair<Person,Pet>(
        new Person("Bob",LocalDate.of(1998, 2, 12), 70.0),
        new Cat("Fluffy")
      );

    System.out.println(pr1.getFirst());
    System.out.println(pr1.getSecond().getName());
    System.out.println(pr1);
  }
}
          
