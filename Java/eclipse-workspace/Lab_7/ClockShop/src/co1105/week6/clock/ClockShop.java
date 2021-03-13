package co1105.week6.clock;

class ClockShop {
  public static void main(String[] args) {

    Clock[] clocks = new Clock[3];
    clocks[0] = new Clock(11,58);
    clocks[1] = new SpeakingClock(23,58);
    clocks[2] = new CuckooClock(14,58);

    for (Clock c : clocks) {
      System.out.println(c);
      c.advanceTime(2);
      System.out.println(c+"\n");
    }
  }
}