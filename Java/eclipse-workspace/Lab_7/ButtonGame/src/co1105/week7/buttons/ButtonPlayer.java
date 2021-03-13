package co1105.week7.buttons;

import java.util.Scanner;
/**
 * ButtonPlayer.java
 *
 */

public class ButtonPlayer {
    
  public static void main(String[] args) {
    Board board = new Board();
    Scanner stdin = new Scanner(System.in);

    board.drawBoard();
    try {
      while (true) {
        System.out.print("Enter piece to move (row col): ");
        int row; int col;
        boolean ok;
        do {
        	try {
        		row=stdin.nextInt();
        		col=stdin.nextInt();
        		if (row<0 || row>7 || col<0 || col>7) {
        			throw new MoveOutOfRangeException("Move location out of range");
        		}
        		board.move(row, col);
        	}
        	catch(MoveOutOfRangeException || EdgeMoveException || MoveBlockedException || NoButtonException e) {
        		System.out.println(e);
        		System.out.print("Enter piece to move (row col): ");
        		continue;
        	}
        	
        } ok=true;
        } while (!ok);
        board.drawBoard();
      }
    }
    catch (Exception e) {
      System.out.println("Thanks for playing.");
    }
  }
    
} // PlayButtons