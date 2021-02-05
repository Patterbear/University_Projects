package co1105.cw1.bwtfm1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Course {
	
	private String name;
	private int[] holes;
	private int coursePar;
	
	Course(String name, int[] holes) {
		this.name = name;
		this.holes = holes;
		this.coursePar = this.getCoursePar();
	}
	
	String getCourseName() {
		return this.name;
	}
	
	int getHolePar(int h) {
		return holes[h];
	}
	
	int getCoursePar() { //All hole pars added
		int total = 0;
		for (int i=0; i<holes.length; i++) {
			total += holes[i];
		}
		return total;
	}
	
	public String toString() {
		return this.name + "          " + Arrays.toString(holes).replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(",", " ") + "    Par: " + Integer.toString(getCoursePar()) + "\n";
	}

}
