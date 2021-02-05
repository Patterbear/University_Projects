package co1105.cw1.bwtfm1;

import java.util.ArrayList;
import java.util.Arrays;

public class ScoreCard {
	private String name;
	private Course course;
	private double time;
	private int[] holeScores;
	
	ScoreCard(String n, Course c, double t, int[] ss)	{
		this.name = n;
		this.course = c;
		this.time = t;
		this.holeScores = ss;
	}
	
	String getName() {
		return this.name;
	}
	
	double getRawTime() {
		return this.time;
	}
	
	int[] getScores() {
		ArrayList<Integer> realScores = new ArrayList<Integer>();
		
		for(int i=0; i<holeScores.length; i++) {
			realScores.add(holeScores[i]-course.getHolePar(i));
		}
		int[] compatScores = realScores.stream().mapToInt(i -> i).toArray();
		return compatScores;
	}
	
	double getAdjustedTime() {
		double total = getRawTime();
		for (int i=0; i<holeScores.length; i++) {
			total += holeScores[i];
		}
		return total;
	}
	
	public String toString() {
		return this.name + " (" + this.time + ")     " + Arrays.toString(this.getScores()).replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(",", " ") + "     (" + this.getAdjustedTime() + ")";
	}
	

}
