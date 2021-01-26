// From 02 Java syntax
import javax.swing.JOptionPane;
public class LabWeek2Prog2 {
  public static void main (String[] args) {
    ;
    String word = JOptionPane.showInputDialog(null,"Type some text: ");
    String countStr = JOptionPane.showInputDialog(null,"How many times? ");
    int count = Integer.parseInt(countStr);
    StringBuilder output = new StringBuilder();
    for (int i=0; i<count; ++i) {
      output.append((i+1)+" "+word+"\n");
    }
    JOptionPane.showMessageDialog(null,output);

  }
}