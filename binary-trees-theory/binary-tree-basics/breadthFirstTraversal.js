const { binaryTree } = require('./binaryTreeBasics.js');

const breadthFirstTraversal = (root) => {
	if (root === null) return [];

	const result = [];
	const queue = [ root ];

	while (queue.length > 0) {
		const current = queue.shift();
		result.push(current.value);

		if (current.left !== null) queue.push(current.left);
		if (current.right !== null) queue.push(current.right);
	}

	return result;
};

console.log('show the result ', breadthFirstTraversal(binaryTree)); // ['a', 'b', 'c', 'd', 'e', 'f']
