// [AUTHOR] jelouta
// [DESCRIPTION] [Python 3] DFS (in-order) extraction & balanced tree-building
// [LINK] https://leetcode.com/problems/balance-a-binary-search-tree/discuss/551956/Python-3-DFS-(in-order)-extraction-and-balanced-tree-building

/*

Steps
    1. We use DFS (in-order) to extract node values while preserving the order.
    2. We build the balanced tree by recursively taking the middle element of the ordered list as root.
Note: we use indices (l:left, r:right) instead of slicing to preserve space.

class Solution:
    def balanceBST(self, root):
        
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ns = dfs(root)
        
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m + 1, r)
            return root
        
        return build(0, len(ns) - 1)


*/


// ==========================================================================


// [AUTHOR] votrubac
// [DESCRIPTION] C++/Java with picture, DSW O(n)|O(1)
// [LINK] https://leetcode.com/problems/balance-a-binary-search-tree/discuss/541785/C%2B%2BJava-with-picture-DSW-O(n)orO(1)

/*

BETTER TO READ AN ARTICLE

*/

// ==========================================================================


// [AUTHOR] control_the_narrative
// [DESCRIPTION] JavaScript Simple Solution Using Tree Reconstruction
// [LINK] https://leetcode.com/problems/balance-a-binary-search-tree/discuss/621291/JavaScript-Simple-Solution-Using-Tree-Reconstruction

/*

Steps:

Use inorder traversal to create a sorted array
Construct a balance tree using the sorted array

*/

var balanceBST = function(root) {
    function inOrder(myRoot) {
        if(!myRoot) return [];
        return [...inOrder(myRoot.left), myRoot.val, ...inOrder(myRoot.right)]
    }
    const sortedArr = inOrder(root)
    
    function constructTree(arr) {
        if(!arr.length) return null;
        
        const mid = Math.floor(arr.length / 2);
        const node = new TreeNode(arr[mid])
        node.left = constructTree(arr.slice(0, mid));
        node.right = constructTree(arr.slice(mid+1));
        
        return node;
    }
    return constructTree(sortedArr);
};

// ==========================================================================


// [AUTHOR] 
// [DESCRIPTION] C++ BST Using Rotation
// [LINK] 

/*

Solving using recursion. Basically, at each node, we assume that the left and right sub-trees are balanced. Now we have to merge the 2 sub-trees with the node. There are 5 conditions that can occur during the balancing.
Condition for balanced tree is that abs(left_height - right_height)) <= 1

    1. Root node is already balanced -> Do Nothing.
    2. Root node is unbalanced leaning on the left and the left sub-tree also has a height of or more -> (LL configuration) -> To balance this, simply do a right rotation.
    3. LR configuration -> Do 2 swaps. First left rotate the left sub-tree root to make it a LL configuration, then right rotate the root.
    4. RR configuration -> Do a left rotation on the root
    5. RL configuration -> First right rotate the right sub-tree root to make it a RR config. Then left rotate the root.

Whenever we rotate, we need to make sure the swapped nodes, form a balanced sub-tree too!

*/

int getHeight(TreeNode *root){
    if(root == NULL) return -1;
    return max(getHeight(root->left), getHeight(root->right))+1;
}
int isBalanced(TreeNode *root){
    return getHeight(root->left) - getHeight(root->right);
}

TreeNode* leftRotate(TreeNode* root){
    TreeNode* x = root->right;
    root->right = x->left;
    x->left = getRotation(root);
    return getRotation(x);
}

TreeNode* rightRotate(TreeNode* root){ // O(1)
   TreeNode* x = root->left;
    root->left = x->right;
    x->right = getRotation(root);
    return getRotation(x);
}

TreeNode* getRotation(TreeNode *root){
    int bal = isBalanced(root);
    // cout<<"Root: "<<root->val<<" Bal: "<<bal<<endl;
    if(bal >=2){ //Left height  > right height -> LL, LR
        if(isBalanced(root->left) >= 1){ // LL
            // cout<<"LL case: RightRotate("<<root->val<<")"<<endl;
            return rightRotate(root);
        }
        else{ //LR
            // auto tmp = (root->left==NULL)?INT_MAX:root->left->val;
            // cout<<"LR case: leftRotate("<<tmp<<")"<<endl;
            root->left = leftRotate(root->left);
            // cout<<"LR case: RightRotate("<<root->val<<")"<<endl;
            return rightRotate(root);
        }
    }
    else if(bal <= -2){ //RR , RL
        if(isBalanced(root->right) <= -1){ // RR
            // cout<<"RR case: LeftRotate("<<root->val<<")"<<endl;
            return leftRotate(root);
        }
        else{ //RL
            // auto tmp = (root->right==NULL)?INT_MAX:root->right->val; 
            // cout<<"RL case: RightRotate("<<tmp<<")"<<endl;
            root->right = rightRotate(root->right);
            // cout<<"RL case: LeftRotate("<<root->val<<")"<<endl;
            return leftRotate(root);
        }        
    }
    return root;
}

TreeNode* balanceBST(TreeNode* root) {
    if(root == NULL) return NULL;
    // cout<<"balanceBST("<<root->val<<")"<<endl;
    root->left = balanceBST(root->left);
    // int tmp = (root->left)?root->left->val: INT_MAX;
    // cout<<root->val<<"->left = "<<tmp<<endl;
    root->right = balanceBST(root->right);
    // tmp = (root->right)?root->right->val: INT_MAX;
    // cout<<root->val<<"->right = "<<tmp<<endl;
    return getRotation(root);
    
}

// ==========================================================================


// [AUTHOR] simplekind
// [DESCRIPTION] [C++] Easy Solution using AVL Trees Concept
// [LINK] https://leetcode.com/problems/balance-a-binary-search-tree/discuss/1858403/C%2B%2B-Easy-Solution-using-AVL-Trees-Concept

/*

Only Prerequiste is to know about concept for AVL Trees root insertion, as code is almost similar.


 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 
#define null nullptr
#define l left
#define r right
class Solution {
public:
    TreeNode* rrot (TreeNode* root){
        if(root==null) return null;
        TreeNode* x = root->l;
        root->l=x->r;
        x->r=root;
        root=x;
        return root;
    }
    
    TreeNode* lrot (TreeNode* root){
        if(root==null) return null;
        TreeNode* x = root->r;
        root->r=x->l;
        x->l=root;
        root=x;
        return root;
    }
    
    int height (TreeNode* root){
        if(root==null) return -1;
        return 1 + max(height(root->l),height(root->r));
    }
    
    TreeNode* helper (TreeNode* root){
        if (root==null) return null;
        root->l=helper(root->l);
        root->r=helper(root->r);
        int l = height(root->l), r = height(root->r);
        int bf = l -r ;
        if(bf > 1){
            if (height(root->l->l)<height(root->l->r)){
                root->l=lrot(root->l);
            }
            return helper(rrot(root));
        }else if (bf<-1){
            if (height(root->r->r)<height(root->r->l)){
                root->r=rrot(root->r);
            }
            return helper(lrot(root));
        }
        return root;
    }
    
    TreeNode* balanceBST(TreeNode* root) {
        if(root==null) return root;
        return helper(root);
    }
};

*/


// ==========================================================================

