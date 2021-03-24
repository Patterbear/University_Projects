public class TunePlayer {

  public static void main(String[] args) {
    Track t1 = new Track("Manta Ray","The Pixies",134);
    Track t2 = new Track("Transmission","Joy Division",216);
    Track t3 = new Track("Woe Is Meee","Ghostpoet",247);

    Track[] trs = {t1,t2,t3};

    Playlist list1 = new Playlist("Glum 1",trs);

    System.out.println(list1);
    System.out.println("Total length is: "+list1.getTotalLengthString());
  }
}