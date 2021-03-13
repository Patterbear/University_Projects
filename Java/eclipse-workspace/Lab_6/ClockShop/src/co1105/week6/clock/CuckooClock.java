package co1105.week6.clock;

public class CuckooClock extends Clock {

	public CuckooClock(int h, int m) {
		super(h, m);
	}
	
	public CuckooClock(Clock c) {
		super(c);
	}
	
	public String toString() {
		if (this.getMinute() == 0) {
			String s = new String("");
			for(int i=0; i<this.getHour();i++) {
				s += "Cuckoo Cuckoo... ";
			}
			return s;
		} else {
			return this.getHour() + ":" + this.getMinute();
		}
	}

}
