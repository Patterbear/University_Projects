package co1105.cw1.bwtfm1;

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
		return this.holeScores;
	}
	
	double getAdjustedTime() {
		double total = getRawTime();
		for (int i=0; i<holeScores.length; i++) {
			total += holeScores[i];
		}
		return total;
	}
	
	public String toString() {
		return this.name + " (" + this.time + ")     " + Arrays.toString(holeScores).replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(",", " ") + "     (" + this.getAdjustedTime() + ")";
	}
	

}
