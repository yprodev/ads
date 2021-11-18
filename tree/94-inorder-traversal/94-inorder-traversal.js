// [AUTHOR]: jenish_k
// [DESCRIPTION]: C++ || Brute = > Better = > Optimal || Easy to Understand

/*

1. Brute Force using Recursion
Time Complexity : O ( n )
Space Complexity : O ( n ) [ Recursive Stack Space ]

class Solution {
public:
    vector<int>res;
    void Inorder(TreeNode *root)
    {
        if(root==nullptr)
            return;
        
        
        Inorder(root->left);
        res.push_back(root->val);
        Inorder(root->right);
        
    }
    vector<int> inorderTraversal(TreeNode* root) {
        Inorder(root);
        return res;
    }
};


2. Iterative Approach
Time Complexity : O ( n )
Space Complexity : O ( n )


class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>ve;
        TreeNode *curr=root;
        stack<TreeNode *>s1;
        
        while(curr!=nullptr ||!s1.empty())
        {
            while(curr!=nullptr)
            {
                s1.push(curr);
                curr=curr->left;
            }
            curr=s1.top();
            ve.push_back(curr->val);
            s1.pop();
            curr=curr->right;
        }
         return ve;
    }
   
};



3. Optimal Approach using Morris Traversal ( Threaded Binary Tree )
Time Complexity : O ( n )
Space Complexity : O ( 1 )


class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>ans;
        TreeNode *curr=root;
        while(curr!=NULL)
        {
            if(curr->left==NULL)
            {
                ans.push_back(curr->val);
                curr=curr->right;
                
            }
            else
            {
                TreeNode *prev=curr->left;
                while(prev->right!=NULL and prev->right!=curr)
                {
                    prev=prev->right;
                }
                if(prev->right==NULL)
                {
                    prev->right=curr;
                    curr=curr->left;
                }
                else
                {
                    prev->right=NULL;
                    ans.push_back(curr->val);
                    curr=curr->right;
                }
            }
        }
          return ans;
    }
  
};

*/


// ===================================================


// [AUTHOR]: linfongi
// [DESCRIPTION]: JavaScript solution with iteration

function inorderTraversal(root) {
  const stack = [];
  const res = [];

  while (root || stack.length) {
    if (root) {
      stack.push(root);
      root = root.left;
    } else {
      root = stack.pop();
      res.push(root.val);
      root = root.right;
    }
  }

  return res;
}

// ===================================================


// [AUTHOR]: roy_glez
// [DESCRIPTION]: Javascript solution

var inorderTraversal = function(root) {
    var stack = [],
        res = [];
    
    while(true){
        if(root !== null){
            stack.push(root);
            root = root.left;
        }else{
            if(stack.length === 0) break;
            root = stack.pop();
            res.push(root.val);
            root = root.right;
        }
    }
    
    return res;
};

// ===================================================


// [AUTHOR]: EugeneTeu
// [DESCRIPTION]: Simple Javascript solution (Recursive)

var inorderTraversal = function(root) {
    if (!root) {
      return [];
    }

    let left = inorderTraversal(root.left);
    let mid = root.val;
    let right = inorderTraversal(root.right);

    return [...left, mid, ...right];
};

// ===================================================

// [AUTHOR]: ME
// [DESCRIPTION]: first working result

var inorderTraversal = function(root) {
    const result = [];
    
    const traversal = function(root) {
        if (!root) return result;
        
        traversal(root.left);
        result.push(root.val);
        traversal(root.right);
    }
    
    traversal(root);
    
    return result;
    
};

// READ: https://www.educative.io/edpresso/what-is-morris-traversal

