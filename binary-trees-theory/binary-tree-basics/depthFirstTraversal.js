// Test cases:
// 1. Pass valid binary tree
// 2. Pass empty tree
// 3. Pass null

const { binaryTree } = require('./binaryTreeBasics.js');


const depthFirstTraversal = (root) => {
	if (root === null) return []; // Check for passing null

	const result = [];
	const stack = [ root ];

	while (stack.length > 0) {
		const current = stack.pop();
		result.push(current.value);

		if (current.right) stack.push(current.right);
		if (current.left) stack.push(current.left);
	}

	return result;
};


console.log('show the result ', depthFirstTraversal(binaryTree)); // ['a', 'b', 'd', 'e', 'c', 'f']

