
public class Track {
	
	public String title;
	public String artist;
	public int length;

	public Track(String title, String artist, int length) {
		this.title = title;
		this.artist = artist;
		this.length = length;
	}
	
	public String getTitle() {
		return this.title;
	}
	
	public String getArtist() {
		return this.artist;
	}
	
	public int getLength() {
		return this.length;
	}
	
	public String toString() {
		return this.title + " - " + this.artist;
	}
	

}
