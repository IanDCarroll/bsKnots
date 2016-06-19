class Knots {
    public static String rvrs(String text) {
	String rvrs = "";
	for (int i=text.length()-1;i>=0;i--) {
	    rvrs += text.charAt(i);
	}
	return rvrs;
    }
}

public class bs {
    public static void main(String [] args) {
	System.out.println(Knots.rvrs("majestic unicorn"));
    }
}
