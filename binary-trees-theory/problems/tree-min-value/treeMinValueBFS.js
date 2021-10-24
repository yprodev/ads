const { binaryNumberWithMinTree } = require('../../binary-tree-basics/binaryNumbersWithMinTree');


const treeMinValue = (root) => {
	if (root === null) return Infinity;

	let minimum = Infinity;
	const queue = [ root ];

	while (queue.length > 0) {
		const current = queue.shift();

		if (minimum > current.value) {
			minimum = current.value;
		}

		if (current.left) queue.push(current.left);
		if (current.right) queue.push(current.right);
	}

	return minimum;
};


console.log('result: ', treeMinValue(binaryNumberWithMinTree)); // -> 3
