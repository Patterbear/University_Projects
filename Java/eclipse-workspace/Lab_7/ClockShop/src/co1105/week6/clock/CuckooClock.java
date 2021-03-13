package co1105.week6.clock;

/**
 * Class to represent a Cuckoo Clock at a given time.
 */

class CuckooClock extends Clock {
  public CuckooClock (int h, int m) {
    super(h,m);
  }
  public CuckooClock () {
    super();
  }
  public CuckooClock (CuckooClock other) {
    super(other);
  }

  /**
   * Convert to String format.
   * @return As long as the minutes are not zero, use "HH:MM"
   * format. Exactly 2 digits, using leading zeros if required. If the
   * minutes are zero, instead use return "Cuckoo" as many times as
   * the hour, but using a 12 hour clock. Midnight and midday should
   * both get 12 cuckoos.
   */
  public String toString() {
    if (this.getMinute() != 0)
      return super.toString();

    StringBuilder result = new StringBuilder("Cuckoo");
    for (int c = 1 ; c < (this.getHour()%12==0 ? 12 : this.getHour()%12); ++c)
      result.append(" Cuckoo");
    return result.toString();
  }
  
//  // Alternative version
//  public String toString() {
//    if (this.getMinute()==0) {
//      String res = "Cuckoo";
//      int numOfCuckoos = this.getHour()%12;
//      if (numOfCuckoos==0) { 
//        numOfCuckoos = 12;
//      }
//      for (int i=1; i<numOfCuckoos; ++i) {
//        res += " Cuckoo";
//      }
//      return res;
//    } else {
//      return super.toString();
//    }
//  }
  
}