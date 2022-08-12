// [AUTHOR] StefanPochmann
// [DESCRIPTION] Python BFS
// [LINK] https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99000/Python-BFS


/*

def findValueMostElement(self, root):
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes


*/



// ==========================================================================


// [AUTHOR] achitJ
// [DESCRIPTION] [C++] easy to understand o(n) DFS
// [LINK] https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/1318704/C%2B%2B-easy-to-understand-o(n)-DFS


/*


class Solution {
public:
    

    Approach:
    We traverse the tree in preorder and update the answer vector according to
    the largest value in the current depth.

    
    void updateAns(TreeNode *root, vector<int> &ans, int currIndex)
    {
        if(!root) return;
        
        if(currIndex == ans.size())
        {
            ans.push_back(root->val);
        }
        
        if(root->val > ans[currIndex])
        {
            ans[currIndex] = root->val;
        }
        
        updateAns(root->left, ans, currIndex + 1);
        updateAns(root->right, ans, currIndex + 1);
    }
    
    vector<int> largestValues(TreeNode* root) 
    {
        vector<int> ans;
        
        if(!root) return ans;
        
        updateAns(root, ans, 0);
        
        return ans;
    }
};


*/


// ==========================================================================


// [AUTHOR] LinearEnter
// [DESCRIPTION] JavaScript solution
// [LINK] https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/1724054/JavaScript-solution

var largestValues = function(root) {
    if (!root) return []
    const stack = [root]
    const result = []
    while(stack.length > 0) {
        let maxVal = stack[0]?.val
        const size = stack.length
        for(let i = 0; i < size; i++) {
            const cur = stack.shift()
            if (maxVal < cur.val) {
                maxVal = cur.val
            }
            cur.left && stack.push(cur.left)
            cur.right && stack.push(cur.right)
        }
        result.push(maxVal);
    }
    return result
};

// ==========================================================================


// [AUTHOR] rdx11
// [DESCRIPTION] Javascript - BFS - O(n)
// [LINK] https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/541856/Javascript-BFS-O(n)

var largestValues = function(root) {
    if(!root) return [];

    let queue = [{node:root,level:0}];
    let resultArr = [];

    while(queue.length>0) {
        let {node,level}=queue.shift();
        if(resultArr[level] || resultArr[level] === 0){
            resultArr[level] = (resultArr[level] < node.val) ? node.val : resultArr[level];
        } else {
            resultArr[level] = node.val;
        }
        if(node.left) {
            queue.push({node: node.left, level: level+1});
        }
        if(node.right) {
            queue.push({node: node.right, level: level+1});
        }
    }

    return resultArr;
};

// ==========================================================================


// [AUTHOR] OsidAbu-Alrub
// [DESCRIPTION] Typescript | Javascript solution
// [LINK] https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/2313921/Typescript-or-Javascript-solution

function largestValues(root: TreeNode | null): number[] {
    let currentLevel = [root];
    let nextLevel = [];
    let currentMaxValue = Number.MIN_SAFE_INTEGER;
    const ans = [];
    while(currentLevel.length && root){
        const node = currentLevel.shift();
        
        if(node.val > currentMaxValue) currentMaxValue = node.val;
        if(node.left) nextLevel.push(node.left);
        if(node.right) nextLevel.push(node.right);
        
        if(!currentLevel.length){
            ans.push(currentMaxValue);
            currentMaxValue = Number.MIN_SAFE_INTEGER;
            [currentLevel, nextLevel] = [nextLevel, currentLevel];
        }
    }
    return ans;
};

// ==========================================================================


// MINE SOLUTION

/*
	Did the start of the solution, however mix togetner nodes and node values
	in the queue for breadth first search. Also, have some complexity with 
	moving from one node to the second node. Mix iterative way and recursive.
*/

var largestValues = function(root) {
  const queue = [root.val],
        answers = [];
  let lastLevelIdx = 0;
  
  
  for (let i = 0; i < queue.length; i++) {
    let currentNode = queue[i];
    answers = Math.max(...queue)
    
    queue = queue.slice(queue.length);
    queue.push(currentNode.left.val);
    queue.push(currentNode.right.val);
    
    lastLevelIdx = queue.length - 1;
  }

  
  
  
    
};