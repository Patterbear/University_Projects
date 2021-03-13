package co1105.week8.bwtfm1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.TreeSet;
import java.io.File;
import java.io.FileNotFoundException;
class WordCount {
  
  public static void main (String[] args) throws FileNotFoundException {
    String fname=args[0];
    try (Scanner sc = new Scanner(new File(fname))) {
      while (sc.hasNext()) {
        String word = sc.next();
        //System.out.println(word);
      }
    }
    
    ArrayList<String> al = new ArrayList<String>();
    try (Scanner sc = new Scanner(new File(fname))) {
        while (sc.hasNext()) {
          String word = sc.next();
          al.add(word);
        }
      }
    
    Iterator<String> al_itr = al.iterator();
    while(al_itr.hasNext()) {
    	System.out.println(al_itr.next());
    }

    
    LinkedList<String> ll = new LinkedList<String>();
    try (Scanner sc2 = new Scanner(new File(fname))) {
        while (sc2.hasNext()) {
          String word = sc2.next();
          ll.add(word);
        }
    }
    
    Iterator<String> ll_itr = ll.iterator();
    while(ll_itr.hasNext()) {
    	System.out.println(ll_itr.next());
    }
        
     HashSet<String> hs = new HashSet<String>();
     try (Scanner sc3 = new Scanner(new File(fname))) {
         while (sc3.hasNext()) {
           String word = sc3.next();
           hs.add(word);
         }
    
    }
 
     Iterator<String> hs_itr = hs.iterator();
     while(hs_itr.hasNext()) {
     	System.out.println(hs_itr.next());
     }
     
     TreeSet<String> ts = new TreeSet<String>();
     try (Scanner sc4 = new Scanner(new File(fname))) {
         while (sc4.hasNext()) {
           String word = sc4.next();
           ts.add(word);
         }
    
     }
     Iterator<String> ts_itr = ts.iterator();
     while(ts_itr.hasNext()) {
     	System.out.println(ts_itr.next());
     }
  }

}