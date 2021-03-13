package co1105.week7.buttons;


/**
 * Button.java
 *
 *
 * Created: Fri Nov  9 16:39:43 2001
 *
 * @author Gilbert Laycock
 * @version $Id: Button.java 300 2021-02-22 16:25:04Z gtl1 $
 */

public class Button  {

  private ButtonColour colour;
  
  public Button(ButtonColour c) {
    colour = c;
  }

  public ButtonColour getColour () {
    return colour;
  }
  
  public String toString (){
    switch (colour) {
    case RED : return "red";
    case GREEN : return "green";
    default : return "unknown";
    }
  }

  public char getChar (){
    switch (colour) {
    case RED : return 'r';
    case GREEN : return 'g';
    default : return '#';
    }
  }
  
} // Button