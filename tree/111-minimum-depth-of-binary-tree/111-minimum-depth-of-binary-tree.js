// [AUTHOR]: suhailakhtar039
// [DESCRIPTION]: C++ simple recursive

/*

class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root)return 0;
        if(!root->left and !root->right)return 1;
        int l=INT_MAX,r=INT_MAX;
        if(root->left)
            l=minDepth(root->left);
        if(root->right)
            r=minDepth(root->right);
        return min(l,r)+1;
    }
};

*/

// ===================================================


// [AUTHOR]: loia5tqd001
// [DESCRIPTION]: Javascript clear solution

var minDepth = function(root) {
    if (root === null) return 0;
    if (root.left === null) return minDepth(root.right) + 1;
    if (root.right === null) return minDepth(root.left) + 1;
    return Math.min( minDepth(root.left), minDepth(root.right) ) + 1;
};

// ===================================================


// [AUTHOR]: devmaleeq
// [DESCRIPTION]: Javascript Solution

var minDepth = function(root) {
    if(!root) return 0;
    
    else if(root.left && root.right) return 1 + Math.min(minDepth(root.left), minDepth(root.right));
    else if(root.left) return 1 + minDepth(root.left);
    else if(root.right) return 1 + minDepth(root.right);
    return 1;

};

// ===================================================


// [AUTHOR]: 
// [DESCRIPTION]: 

// ===================================================

// [AUTHOR]: ME
// [DESCRIPTION]: NOT WORKING


var minDepth = function(root) {
    return traversal(root, 1);
};

var traversal = function(root, counter) {
    if (!root || (!root && counter > 1)) return counter;
    
    if (!root.left && !root.right) return counter;
    
    return Math.min(traversal(root.left, counter + 1), traversal(root.right, counter + 1)); 
};

