class Knots {
    public static String rvrs(String text) {
	String rvrs = "";
	for (int i=text.length()-1;i>=0;i--) {
	    rvrs += text.charAt(i);
	}
	return rvrs;
    }

    public static String rPal(String text) {
	String message = "Hey... " + text + " isn\'t a palendrome. How am I supposed to reverse that?!";
	//If statement always returns else...
	//in java, == doesn't mean equivalent, 
	//it means "points to same object in memory space"
	if (text.equals(rvrs(text))) {
	    return text;
	} else {
	    return message;
	}
    }
}

public class bs {
    public static void main(String [] args) {
	System.out.println(Knots.rvrs("majestic unicorn"));
	System.out.println(Knots.rPal("racecar"));
	System.out.println(Knots.rPal("lacecar"));
    }
}
