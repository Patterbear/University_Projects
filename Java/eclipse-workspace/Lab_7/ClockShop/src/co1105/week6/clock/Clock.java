package co1105.week6.clock;

/**
 * Class to represent a Clock at a given time.
 */

class Clock {
  /**
   * Hour. Invariant condition is that this is between 0 and 23 inclusive
   */
  private int hour;
  /**
   * Minute. Invariant condition is that this is between 0 and 59 inclusive
   */
  private int minute;

  /**
   * Construct a clock instance
   * @param h the hour to set the clock to; must be between 0 and 23 inclusive
   * @param m the minute to set the clock to; must be between 0 and 59 inclusive
   */
  public Clock(int h, int m) {
    hour = h;
    minute = m;
  }
  
  /**
   * Construct a clock instance set to midnight
   * 
   */
  public Clock() {
    this(0,0);
  }
  /** 
   * Copy a clock instance
   */ 
  public Clock(Clock other) {
    hour = other.hour;
    minute = other.minute;
  }
  /**
   * Getter method for the hour
   * @return the current hour
   */
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
  /**
   * Advance the time by a certain number of minutes
   * <p>
   * The resulting time will satisfy the data invariants. If the
   * minute goes beyond 59, it should roll over to 0; but also
   * increment the hour. If the hour goes beyond 23, if should roll
   * over to 0.
   * @param mins a POSITIVE number of minutes to advance the hour by.
   */
  public void advanceTime(int mins) {
    minute += mins;
    hour += minute/60;
    minute %=60;
    hour %=24;
  }
  
  /**
   * Advance the time by one minutes
   * <p>
   * The resulting time will satisfy the data invariants. If the minute goes
   * beyond 59, it should roll over to 0; but also increment the hour. If the hour
   * goes beyond 23, if should roll over to 0.
   * 
   */
  public void advanceTime() {
    this.advanceTime(1);
  }
  /**
   * Convert to String format.
   * @return Use "HH:MM" format. Exactly 2 digits, using leading zeros
   * if required.
   */
  public String toString() {
    return String.format("%02d:%02d",hour,minute);
  }
}