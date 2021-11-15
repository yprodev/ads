// [AUTHOR]: kabraji001
// [DESCRIPTION]: C++ || DFS (PREORDER TRAVERSAL) || RECURSIVE

/*
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root){
            return 0LL;
        }
        if(root->left && !root->left->left && !root->left->right){
            return root->left->val + sumOfLeftLeaves(root->right);
        }
        else{
            return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
        }
        
    }
};
*/

// ===================================================


// [AUTHOR]: yinchuhui88
// [DESCRIPTION]: javascript

var sumOfLeftLeaves = function(root) {
    return dfs(root)
    
    function dfs(root) {
        if(!root) return 0
        let result = 0
        if(root.left){
            if(!root.left.left && !root.left.right){
                result += root.left.val
            } else{
                result += dfs(root.left)
            }
        }
        result += dfs(root.right)
        return result
    }   
};

// ===================================================


// [AUTHOR]: thoai_huynh
// [DESCRIPTION]: Javascript BFS

var sumOfLeftLeaves = function(root) {
    const queue = [root]
    let sum = 0
    
    while (queue.length > 0) {
        const node = queue.shift()
        
        if (node.left) {
            if (!node.left.left && !node.left.right) {
                sum += node.left.val
            } else {
                queue.push(node.left)
            }
        }
        
        if (node.right) {
            queue.push(node.right)
        }
    }
    
    return sum
};

// ===================================================


// [AUTHOR]: stevemu
// [DESCRIPTION]: JavaScript

var sumOfLeftLeaves = function(root) {
    if (root == null) {
        return 0;
    } else if (root.left && root.left.left == null && root.left.right == null) {
        return root.left.val + sumOfLeftLeaves(root.right);
    } else {
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    }
};

// ===================================================


// [AUTHOR]: rockwell153
// [DESCRIPTION]: Pretty much JavaScript

const sumOfLeftLeaves = ( r, l ) =>
    ! r  ?  0
    : ! r.left && ! r.right && l  ?  r.val
    : sumOfLeftLeaves( root.left, 1 ) + sumOfLeftLeaves( root.right, 0 )



// ===================================================

// [AUTHOR]: ME
// [DESCRIPTION]: Working solution

var sumOfLeftLeaves = function(root, sum) {
    if (!root) return 0;

    if (root.left && !root.left.left && !root.left.right) {
        return root.left.val + sumOfLeftLeaves(root.right);
    } else {
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    }

};

