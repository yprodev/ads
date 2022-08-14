// [AUTHOR] archit91
// [DESCRIPTION] [C++/Python] Recursive & Iterative DFS + BFS + Morris Traversal O(1) | Beats 100%
// [LINK] https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1556417/C%2B%2BPython-Recursive-and-Iterative-DFS-%2B-BFS-%2B-Morris-Traversal-O(1)-or-Beats-100

// BETTER TO CHECK THE LINK

// ==========================================================================

// [AUTHOR] sahibpratap
// [DESCRIPTION] [C++]Recursive and Iterative Simple explanation | 100% faster | O(N)
// [LINK] https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1555932/C%2B%2BRecursive-and-Iterative-Simple-explanation-or-100-faster-or-O(N)


// ==========================================================================

// [AUTHOR] TovAm
// [DESCRIPTION] C++ simple recursive solution
// [LINK] https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1508493/C%2B%2B-simple-recursive-solution

/*
    C++

int sumNumbersHelper(TreeNode* root, int sum)
{
    if(!root)
        return 0;

    sum = sum * 10 + root -> val;

    if(!root -> left && !root -> right)
        return sum;

    return sumNumbersHelper(root -> left, sum) + sumNumbersHelper(root -> right, sum);
}

int sumNumbers(TreeNode* root) {
    return sumNumbersHelper(root, 0);
}

*/

// ==========================================================================

// [AUTHOR] YehudisK
// [DESCRIPTION] C++ Simple and Clean Recursive Solution, Explained
// [LINK] https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1555854/C%2B%2B-Simple-and-Clean-Recursive-Solution-Explained

/*

Explanation:
We are using typical preorder traversal on a tree.
In each node we visit, first we concatenate the value to the current number.
If we are in a leaf, we add curr to the result.
Otherwise, we continue recursion with curr.

Time Complexity: O(n), we visit each node exactly once.
Space Complexity: O(1) if we don't consider recursion stack. With recursion call stack it's O(height-of-tree).

class Solution {
public:
    int res = 0;
    void rec(TreeNode* node, int curr) {
        if (!node) return;
        
        curr = curr * 10 + node->val;
        
        if (!node->left && !node->right) {
            res += curr;
            return;
        }
        
        rec(node->left, curr);
        rec(node->right, curr);
    }
    
    int sumNumbers(TreeNode* root) {
        rec(root, 0);
        return res;
    }
};


*/

// ==========================================================================

