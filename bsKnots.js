function rvrs(string) {
    var rvrs = ''
    for ( i=string.length-1; i>=0; i-- ) {
	rvrs += string[i];
    }
    return rvrs;
}

console.log(rvrs('boogers'));
