// [AUTHOR]: ybmlk
// [DESCRIPTION]: JavaScript Simple DFS

var binaryTreePaths = function(root) {
    
    const output = [];
    
    function callDFS(node, path) {
        if(!node) return;
        
        if(!node.left && !node.right) {
            output.push([...path, node.val]);
            return;
        }
        callDFS(node.left, [...path, node.val]);
        callDFS(node.right, [...path, node.val])
    }
    
    callDFS(root, [])
    return output.map(row => row.join('->'))
};

// ===================================================


// [AUTHOR]: omarzoghayyer
// [DESCRIPTION]: JavaScript Solution

var binaryTreePaths = function(root) {
    let result = [];
    traverse(root, "");
    
    function traverse(node, path) {
        if (!node) return;
 
        if (!node.left  && !node.right) {
            result.push(path + node.val);
            return;
        }

        traverse(node.left, path + node.val + "->");
        traverse(node.right, path + node.val + "->");
    }

    return result;
};

// ===================================================


// [AUTHOR]: StefanPochmann
// [DESCRIPTION]: 5 lines recursive Python

/*

def binaryTreePaths(self, root):
    if not root:
        return []
    return [str(root.val) + '->' + path
            for kid in (root.left, root.right) if kid
            for path in self.binaryTreePaths(kid)] or [str(root.val)]

*/

// ===================================================


// [AUTHOR]: hbjORbj
// [DESCRIPTION]: DFS JS Solution

// Using String:
var binaryTreePaths = function(root) {
    let paths = [];
    
    function dfsTraversal(root, cur) {
        if (!root) return;
        if (!root.left && !root.right) {
            paths.push(cur + root.val);
            return;
        }
        dfsTraversal(root.left, cur + root.val + "->");
        dfsTraversal(root.right, cur + root.val + "->");
    }
    
    dfsTraversal(root, "");
    return paths;
    // Time Complexity: O(N), we always visit all nodes
    // Space Complexity: O(H) or O(N), height can be at most N (in case of a skewed tree)
};


// Using Array:
const binaryTreePaths = (root) => {
  let paths = [];
  function dfsTraversal(curPath, root) {
    if (root === null) {
      return;
    }
    if (root.left === null && root.right === null) {
      paths.push([...curPath, root.val]);
      return;
    }
    dfsTraversal([...curPath, root.val], root.left);
    dfsTraversal([...curPath, root.val], root.right);
  }
  dfsTraversal([], root);
  return paths.map(path => path.join("->"));
};


// Using only one array:
var binaryTreePaths = function(root) {
  let paths = [];
  function dfsTraversal(curPath, root) {
    if (!root) return;
    curPath.push(root.val);
    if (root.left === null && root.right === null) {
      paths.push(curPath.join("->"));
    }
    dfsTraversal(curPath, root.left);
    dfsTraversal(curPath, root.right);
    curPath.pop();
  }
  dfsTraversal([], root);
  return paths;
  // T.C: O(N)
  // S.C: O(H)
};

// ===================================================

// [AUTHOR]: 
// [DESCRIPTION]: 

