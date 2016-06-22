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
	    vowelMovement += vowel[Math.floor(Math.random()*vowel.length)];
	} else {
	    vowelMovement += string[i];
	}
    }
    return vowelMovement;
}


//basically works, but don't know why it doesn't recognize the 'u' in jumps.
function kansKnot(string) {

    var inconsonance = '',

	test = /[(bl)(br)(pl)(pr)(tr)(dr)(cl)(cr)(gl)(gr)(fl)(fr)(th)(thr)(ch)(sh)(shr)(scr)(sch)(sc)(sk)(sl)(sm)(sn)(sp)(spl)(spr)(sph)(st)(str)(sw)(tw)(dw)(squ)(qu)(gw)(wh)(wr)(ft)(ct)(lt)(ld)(lk)(lp)(lb)(lfs)(lf)(lv)(lch)(lg)(lm)(ls)(mp)(mph)(nt)(nd)(nch)(ng)(ns)(nk)(pps)(ps)(pt)(xts)(xt)(ts)(nks)(rks)(ks)(bs)(ds)(gg)(ggs)(gs)(ffs)(fs)(ghs)(ght)(gh)(ths)(ppl)(ttl)(tl)(thm)pbtdkgfvszjwhlrmncqx]/i,

	conB = [ 'bl', 'br', 'pl', 'pr', 'tr', 'dr', 'cl', 'cr', 'gl', 'gr',
		 'fl', 'fr', 'th', 'thr', 'ch', 'sh', 'shr', 'scr', 'sch',
		 'sc', 'sk', 'sl', 'sm', 'sn', 'sp', 'spl', 'spr', 'sph',
		 'st', 'str', 'sw', 'tw', 'dw', 'squ', 'qu', 'gw', 'wh',
		 'wr',  'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 's', 'z',
		 'j', 'w', 'h', 'l', 'r', 'm', 'n', 'c', 'q' ]

	conE = [ 'ft', 'ct', 'lt', 'ld', 'lk', 'lp', 'lb', 'lf', 'lv', 
		 'lch', 'lg', 'lm', 'mp', 'mph', 'nt', 'nd', 'nch', 'ng',
		 'ns', 'nk', 'pt', 'xt', 'ts', 'rk', 'ght', 'gh', 'ppl',
		 'tl', 'thm', 'sk', 'sp', 'st', 'sh', 'th', 'ch', 'p', 'b',
		 't', 'd', 'k', 'g', 'f', 'v', 's', 'z', 'j', 'h', 'l', 'r',
		 'm', 'n' ]

    for ( i=0; i<string.length; i++ ) {
	if (string[i].search(test) !== -1) {
	    if (string[i+1].search(test) !== -1) { //do nothing 
	    } else if ((string[i+1].search(/\W/) !== -1)){
		inconsonance += conE[Math.floor(Math.random()*conE.length)];
	    } else { 
		inconsonance += conB[Math.floor(Math.random()*conB.length)];
	    }
	} else {
	    inconsonance += string[i];
	}
    }
    return inconsonance;
}

console.log(rvrsKnot('boogers'));
console.log(rPalKnot('racecar'));
console.log(rPalKnot('lacecar'));
console.log(vmmtKnot('I\'m having a vowel movement!'));
console.log(kansKnot('I\'m feeling quite inconsonant at the moment.'));
console.log(kansKnot('The quick brown fox jumps over the lazy dog?'));
console.log(kansKnot('Should be judging where its chances are more shrewd.'));
