const { binaryTree } = require('../../binary-tree-basics/binaryTreeBasics.js');

const treeIncludes = (root, target) => {
	if (root === null) return false;
	if (root.value === target) return true;

	const left = treeIncludes(root.left, target);
	const right = treeIncludes(root.right, target);

	return left || right;
};


console.log('result: ', treeIncludes(binaryTree, 'e')); // -> true


