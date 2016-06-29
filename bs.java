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

    //untested!
    public static String vmmt(String text) {
	String vowelMovement = "";
	String test = "[aeiouy]";
	String[] vowel = {"a","e","i","o","u","y"};
	for (int i=0; i<text.length(); i++) {
	  if (text.charAt(i).matches(test) != -1) {
	    vowelMovement += vowel[(int)Math.floor(Math.random()*vowel.length())];
	  } else {
	    vowelMovement += text.charAt(i);
	  }
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
