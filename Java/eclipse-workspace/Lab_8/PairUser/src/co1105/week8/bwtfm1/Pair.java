package co1105.week8.bwtfm1;

public class Pair<Person, Pet> {
	
	final Person person;
	final Pet pet;

	public Pair(Person person, Pet pet) {
		this.person = person;
		this.pet = pet;
	}

	public Person getFirst() {
		return this.person;
	}

	public Pet getSecond() {
		return this.pet;
	}
	
	public String toString() {
		return "<" + this.person + ", " + this.pet + ">";
	}

}
