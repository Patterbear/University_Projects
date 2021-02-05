package co1105.cw1.bwtfm1;

import java.util.ArrayList;

public class Tournament {
	private Course course;
	private ScoreCard[] scores;
	
	public Tournament(Course c, ScoreCard[] theScores) {
		this.course = c;
		this.scores = theScores;
		
	}
	
	public String toString() {
		ArrayList <String> scoreList = new ArrayList<String>();
		for (int i=0; i<scores.length; i++) {
			scoreList.add((scores[i].toString()));
		}
		return scoreList.toString().replaceAll(",", "\n").replaceAll("\\]", "").replaceAll("\\[", "")+"\n";
	}
	
	public String declareWinner() {
		return "winner";
	}

}
