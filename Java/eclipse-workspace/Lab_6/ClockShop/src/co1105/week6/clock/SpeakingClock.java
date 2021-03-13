package co1105.week6.clock;

public class SpeakingClock extends Clock {

	public SpeakingClock(int h, int m) {
		super(h, m);
	}
	
	public SpeakingClock(Clock c) {
		super(c);
	}
	
	public String toString() {
		return "At the third stroke the time will be " + this.getHour() + ":" + this.getMinute();
	}

}
