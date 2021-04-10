// [REWIND]: Find the code the most simple and understandable author for this task. The only change was done:

/*
	x => 1 - x ---> x => 1 ^ x
*/

// [AUTHOR]: NatalieSalemme3
var flipAndInvertImage = function(A) {
	for(let row in image) {
		image[row] = image[row].reverse();
		image[row] = image[row].map(x => 1 ^ x);
	}

	return image;
};


