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

console.log(rvrsKnot('boogers'));
console.log(rPalKnot('racecar'));
console.log(rPalKnot('lacecar'));
