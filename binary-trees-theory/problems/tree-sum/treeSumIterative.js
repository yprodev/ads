const { binaryNumberTree } = require('../../binary-tree-basics/binaryNumbersTree.js');


const treeSum = (root) => {
	if (root === null) return 0;

	let totalSum = 0;
	const queue = [ root ];

	while (queue.length > 0) {
		const current = queue.shift();
		totalSum += current.value;

		if (current.left) queue.push(current.left);
		if (current.right) queue.push(current.right);
	}

	return totalSum;
};


console.log('result: ', treeSum(binaryNumberTree)); // -> 25



