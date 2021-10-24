const { binaryNumberWithMinTree } = require('../../binary-tree-basics/binaryNumbersWithMinTree');


const treeMinValue = (root) => {
	if (root === null) return Infinity;

	const leftMin = treeMinValue(root.left);
	const rightMin = treeMinValue(root.right);

	return Math.min(root.value, leftMin, rightMin);
};


console.log('result: ', treeMinValue(binaryNumberWithMinTree)); // -> 3
