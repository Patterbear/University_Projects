
public class Playlist {
	
	private final String name;
	private final Track[] tracks;

	public Playlist(String name, Track[] tracks) {
		this.name = name;
		this.tracks = tracks;
	}
	
	public String getName() {
		return this.name;
	}
	
	public Track getTrack(int n) {
		return this.tracks[n];
	}
	
	public Track[] getAllTracks() {
		return tracks;
	}
	
	public int getTotalLength() {
		int total = 0;
		for (int i=0; i<tracks.length; i++) {
			total += tracks[i].length;
		}
		return total;
	}


	public String getTotalLengthString() {
		return String.format("%d:%2d", (this.getTotalLength()/60), (this.getTotalLength()%60));
	}
	
	public String toString() {
		String output = "";
		output += this.name + "\n";
		for(int i=0; i<this.tracks.length; i++) {
			output += Integer.toString(i+1) + ": " + tracks[i].toString() + "\n";
		}
		return output;
	}

}
