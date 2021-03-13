package co1105.week6.clock;

/**
 * Class to represent a Speaking Clock at a given time.
 */
class SpeakingClock extends Clock  {
  public SpeakingClock(int h, int m) {
    super(h,m);
  }
  public SpeakingClock()  {
    super();
  }
  public SpeakingClock(SpeakingClock other) {
    super(other);
  }
  /**
   * Convert to String format.
   * @return Use "At the third stroke the time will be HH:MM
   * precisely" format. Exactly 2 digits, using leading zeros if
   * required.
   */
  public String toString() {
    return String.format("At the third stroke the time will be %s precisely",
                         super.toString());
  }
}