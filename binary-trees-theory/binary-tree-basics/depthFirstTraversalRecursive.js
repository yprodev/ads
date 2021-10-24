// Test cases:
// 1. Pass valid binary tree
// 2. Pass empty tree
// 3. Pass null

const { binaryTree } = require('./binaryTreeBasics.js');


const depthFirstTraversal = (root) => {
	if (root === null) return []; // Check for passing null

	const leftValues = depthFirstTraversal(root.left); // [b, d, e]
	const rightValues = depthFirstTraversal(root.right); // [c, f]

	return [ root.value, ...leftValues, ...rightValues ];
};


console.log('show the result ', depthFirstTraversal(binaryTree)); // ['a', 'b', 'd', 'e', 'c', 'f']

