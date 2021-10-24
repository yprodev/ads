const { binaryNumberWithMinTree } = require('../../binary-tree-basics/binaryNumbersWithMinTree');


const treeMinValue = (root) => {
	if (root === null) return Infinity;

	let minimum = Infinity;
	const stack = [ root ];

	while (stack.length > 0) {
		const current = stack.pop();

		if (minimum > current.value) {
			minimum = current.value;
		}

		if (current.left) stack.push(current.left);
		if (current.right) stack.push(current.right);
	}

	return minimum;
};


console.log('result: ', treeMinValue(binaryNumberWithMinTree)); // -> 3
