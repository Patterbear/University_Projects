package co1105.week6.clock;

/**
 * Class to represent a clock at a given time
 * @author Benjamin McGregor
 */

public class Clock {
	
	/**
	 * Hour. Invariant condition is that this is between 0 and 23 inclusive.
	 */
	private int hour;
	/**
	 * Minute. Invariant condition is that this is between 0 and 59 inclusive.
	 */
	private int minute;

	/**
	 * Construct a clock instance
	 * @param hour the hour to set the clock to; must be between 0 and 23 inclusive.
	 * @param minute the minute to set the clock to; must be between 0 and 59 inclusive
	 */
	public Clock(int hour, int minute) {
		this.hour = hour;
		this.minute = minute;
	}
	
	public Clock(Clock c) {
		this.hour = c.hour;
		this.minute = c.minute;
	}
	
	public int getHour() {
		return hour;
	}
	/**
	 * Getter method for the minute
	 * @return the current minute
	 */
	public int getMinute() {
		return minute;
	}
	
	public void advanceTime() {
		advanceTime(1);
	}
	
	public void advanceTime(int mins) {
		minute += mins;
		hour +=  minute/60;
		minute %= 60;
		hour %= 24;
	}
		
	@Override
	public int hashCode() {
		return(47*(hour*23+minute));
	}
	
	@Override
	public boolean equals(Object obj) {
		if(this==obj) {
			return true;
		}
		if(obj==null) {
			return false;
		}
		if (getClass() != obj.getClass()) {
			return false;
		}
		Clock other = (Clock) obj;
		return hour == other.hour && minute == other.minute;
	}
	
	
	
	/**
	 * Advance the time by a certain number of minutes
	 * <p>
	 * The resulting time will satisfy the data invariants If the
	 * minute goes beyond 59, it should roll over to 0; but also
	 * increment the hour. If the hour goes beyond 23, it should roll
	 * over to 0.
	 * @param mins a POSITIVE number of minutes to advance the hour by.
	 */
	public String toString() {
		return this.hour + ":" + this.minute;
	}
	
	/**
	 * @param other Clock to compare with
	 */
	
	public int compareTo(Clock other) {
		return Integer.compare(this.hour*60+this.minute, other.hour*60+other.minute);
	}

}
