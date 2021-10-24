const { binaryNumberTree } = require('../../binary-tree-basics/binaryNumbersTree.js');


const treeSum = (root) => {
	if (root === null) return 0;

	return root.value + treeSum(root.left) + treeSum(root.right);
};


console.log('result: ', treeSum(binaryNumberTree)); // -> 25



