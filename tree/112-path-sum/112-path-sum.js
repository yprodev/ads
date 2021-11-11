// [AUTHOR]: poppinlp
// [DESCRIPTION]: [JavaScript] Easy to understand - DFS

/*

Since we need to sum the values from root to leaf, it's straightforward to think about DFS. So, the process could be:

	Traverse the tree via DFS
	Check whether current node is leaf
		check the target value
		continue recursion

Here's the code:

*/

const hasPathSum = (node, target) => {
  if (!node) return false;
  if (!node.left && !node.right) return target === node.val;
  return (
    hasPathSum(node.left, target - node.val) ||
    hasPathSum(node.right, target - node.val)
  );
};

// ===================================================


// [AUTHOR]: ybmlk
// [DESCRIPTION]: JavaScript 4-Liner

var hasPathSum = function(root, targetSum) {

    function run(node, sum) {
        if(!node) return false;
        if(!node.left && !node.right) return sum+node.val === targetSum
        return run(node.left, sum+node.val) || run(node.right, sum+node.val);
    }
    return run(root, 0);
};

// ===================================================


// [AUTHOR]: user7656w
// [DESCRIPTION]: Javascript

var hasPathSum = function(root, sum) {
    if(!root)
        return false
    
    if(root.left === null && root.right === null)
        return sum === root.val
    
    var left_path = hasPathSum(root.left, sum - root.val)
    var right_path = hasPathSum(root.right, sum - root.val)
    
    return left_path || right_path
};


// ===================================================

// [AUTHOR]: ME
// [DESCRIPTION]: Working variant

var hasPathSum = function(root, targetSum) {    
    return traverse(root, 0, targetSum);
};


var traverse = function(root, sum, targetSum) {
    if (!root) return false;
    
    sum += root.val;
    
    let leafNode = !root.left && !root.right,
        match = sum === targetSum;
    
    if (leafNode && match) return true;
        
    return traverse(root.left, sum, targetSum) || traverse(root.right, sum, targetSum);
};

