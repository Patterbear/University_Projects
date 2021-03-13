package co1105.week7.buttons;

import co1105.week7.buttonsExceptions.EdgeMoveException;
import co1105.week7.buttonsExceptions.MoveBlockedException;
import co1105.week7.buttonsExceptions.NoButtonException;

/**
 * Board.java
 *
 *
 * Created: Fri Nov  9 16:54:16 2001
 *
 * @author Gilbert Laycock
 * @version $Id: Board.java 300 2021-02-22 16:25:04Z gtl1 $
 */

public class Board  {
  Button board[][];
  
  public Board() {
    board = new Button [8][8];
    // Initialise with correct pattern
    // put on red buttons
    for (int c=0; c<8; c+=2) {
      board[7][c] = new Button(ButtonColour.RED);
      board[6][c+1] = new Button(ButtonColour.RED);
    }

    // put on green buttons
    for (int c=0; c<8; c+=2) {
      board[0][c] = new Button(ButtonColour.GREEN);
      board[1][c+1] = new Button(ButtonColour.GREEN);    
    }
  }

  public boolean move(int r, int c) throws NoButtonException, EdgeMoveException, MoveBlockedException {
    boolean result;
    if (board[r][c] == null)
      throw new NoButtonException();
    else {
      // there is a button
      // work out which way to move:
      int move;
      if (board[r][c].getColour()==ButtonColour.RED)
        move = -1;
      else
        move = 1;
      
      // do we fall off the edge?
      if (r+move>7 || r+move<0)
        throw new EdgeMoveException();
      else 
        // is there a button in the way?
        if (board[r+move][c]!=null)
          throw new MoveBlockedException();
        else {
          // make the move
          board[r+move][c]=board[r][c];
          board[r][c]=null;
          result = true;
        }
    }
    return result;
  }
  
  public char getBoardChar (int r, int c) {
    if (board[r][c]==null)
      if ((r%2==0 && c%2==0) || (r%2==1 && c%2==1))
        return 'X';
      else
        return ' ';
    else
      if ((r%2==0 && c%2==0) || (r%2==1 && c%2==1))
        return Character.toUpperCase(board[r][c].getChar());
      else
        return board[r][c].getChar();
  }

  public void drawBoard () {
    System.out.println("   0 1 2 3 4 5 6 7");
    for (int row=0; row<8; ++row) {
      System.out.print(row+" ");
      for (int col=0; col<8; ++col) 
        System.out.print(" "+getBoardChar(row,col));
      System.out.println();
    }
      
  }
    
} // Board