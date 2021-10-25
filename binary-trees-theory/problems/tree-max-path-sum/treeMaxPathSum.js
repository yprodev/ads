const { binaryNumberWithMinTree } = require('../../binary-tree-basics/binaryNumbersWithMinTree');


const maxPathSum = (root) => {
	if (root === null) return -Infinity;
	if (root.left === null && root.right === null) return root.value;

	const leftValue = maxPathSum(root.left);
	const rightValue = maxPathSum(root.right);

	return root.value + Math.max(leftValue, rightValue);
};


console.log('result: ', maxPathSum(binaryNumberWithMinTree)); // -> 31
