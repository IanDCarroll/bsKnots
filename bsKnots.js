function rvrsKnot(string) {
    var rvrs = ''
    for ( i=string.length-1; i>=0; i-- ) {
	rvrs += string[i];
    }
    return rvrs;
}

function rPalKnot(string) {
    var message = 'Hey... ' + string + 
	' isn\'t a palendrome. How am I supposed to reverse that?!';
    if (string === rvrsKnot(string)) {
	return string;
    } else {
	return message;
    }
}

function vmmtKnot(string) {
    var vowelMovement = '',
	test = /[aeiouy]/,
	vowel = [ 'a', 'e', 'i', 'o', 'u', 'y' ];
    for ( i=0; i<string.length; i++ ) {
	if (string[i].search(test) !== -1) {
	    //replace it with a random vowel
	    vowelMovement += vowel[Math.floor(Math.random()*vowel.length)];
	} else {
	    vowelMovement += string[i];
	}
    }
    return vowelMovement;
}

console.log(rvrsKnot('boogers'));
console.log(rPalKnot('racecar'));
console.log(rPalKnot('lacecar'));
console.log(vmmtKnot('I\'m having a vowel movement!'));
