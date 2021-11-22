// [AUTHOR]: hzhu007
// [DESCRIPTION]: Python iterative and recursive solution with explanation 

/*

Recursion is easy to implement and understand by definition https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN).

def postorder(self, root):
	"""
	:type root: Node
	:rtype: List[int]
	"""
	res = []
	if root == None: return res

	def recursion(root, res):
	    for child in root.children:
	        recursion(child, res)
	    res.append(root.val)

	recursion(root, res)
	return res


Iteration is basically pre-order traversal but rather than go left, go right first then reverse its result.

def postorder(self, root):
    res = []
    if root == None: return res

    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        stack.extend(curr.children)

    return res[::-1]

*/

// ===================================================


// [AUTHOR]: Ajna
// [DESCRIPTION]: [C++] DFS Iterative vs. Recursive Solutions Compared and Explained, ~99% Time, ~99% Space

/*

The normal iterative approach for a DFS algorithm presumes that you have a stack and progressively add the children as you go down a branch, while doing some operation (in our case extracting val), as you go with the current top of the stack that you will pop.

Once you have nothing more to add, it means no more children there - you reached a leaf and so, keeping popping out of the stack, you will backtrack to some previous node.

It is a convenient approach, with the sole caveat that it will give you results in a top-down fashion (you start from the top and then proceed adding its children down); also, if you were to look for a specific order (say, left branches first), you would have to push them into the stack so that the ones you want parsed first (left, in our example) are pushed last.

That said, this problem requires us to extact the postorder traversal, so, in order to make it work, we will have to reverse the order of our result before returning it.

Now, the way I did it: first of all we get rid of a possible edge case - an empty tree, in which case we return an empty vector.

If we are still in the function, then we declare a bunch of support variable, this time (almost) all of a different kind:

	our usual accumulator variable res, initially an empty vector of integers;
	
	pos, an int that will help us move through our "stack";

	stackArray, which, as the name implies, is not really a stack, but just an array of pointers used as a stack, with an initial size of 1000 (you might set it to the maximum number of nodes which is 10x, but that would be necessary if they were all on a line and with a bit of experimentation, you will see the rarely you need more than that to pass all the tests);

not strictly needed, but just for convenience I also declared curr, that we will use to store the value of the currently parsed node.
We will proceed to put root into stackArray increasing pos, then, as described, we will pop and extract curr out by reducing pos, the value val of curr into res and finally keep pushing the children of the current node curr into stackArray.

Once we are done, we reverse res and can return it :)

The iterative code:

class Solution {
public:
    vector<int> postorder(Node* root) {
        // edge case out of the way
        if (!root) return {};
        // support variables
        vector<int> res;
        int pos = 0;
        Node *stackArray[1000], *curr;
        stackArray[pos++] = root;
        // DFS - iteration on!
        while (pos) {
            curr = stackArray[--pos];
            res.push_back(curr->val);
            for (Node *n: curr->children) stackArray[pos++] = n;
        }
        reverse(begin(res), end(res));
        return res;
    }
};


Now, for the other, canonical approach, we just have a simpler structure: we declare res as a class variable, then in our main function we just call the helper function dfs (provided root != NULL, so we have to check for it only once) and return res when the helper is done running.

But does dfs do?

pretty simple as well: it calls itself recursively on all the children (if any) of the current root and then pushed its value val into res - notice that order matters and you will want to push only after calling all the recursive calls, so that it acts as a sort of backtracking trick.

The recursive code, which seems to be a bit faster and a bit more memory consuming:

class Solution {
public:
    vector<int> res;
    void dfs(Node *root) {
        for (int i = 0, len = root->children.size(); i < len; i++) dfs(root->children[i]);
        res.push_back(root->val);
    }
    vector<int> postorder(Node *root) {
        if (root) dfs(root);
        return res;
    }
};

*/


// ===================================================


// [AUTHOR]: hon9g
// [DESCRIPTION]: JavaScript Iterative & Recursive

/*

Iteravtive Post-order Traverse
Time Complexity: O(N)
Space Complexity: O(N)

*/
var postorder = function(root) {
    const res = [], stack = [root];
    while (stack.length) {
        const curr = stack.pop();
        if (!curr) continue;
        res.push(curr.val);
        stack.push(...curr.children);
    }
    return res.reverse();
};

/*

Iteravtive Post-order Traverse
Time Complexity: O(N)
Space Complexity: O(N)

*/

var postorder = function(root) {
    const res = [];
    traverse(root);
    return res;
    
    function traverse(node) {
        if (!node) return;
        for(child of node.children) {
            traverse(child);
        }
        res.push(node.val);
    } 
};

// ===================================================


// [AUTHOR]: shimphillip
// [DESCRIPTION]: Clean JavaScript Solution

// dfs
// time O(n) space O(n)
var postorder = function(root, result = []) {
    if(!root) {
        return result
    }

    for (const child of root.children) {
        postorder(child, result)
    }
    
    result.push(root.val)
    
    return result
};

// time O(n) space O(n)
var postorder = function (root) {
    const result = []
    
    if(!root) {
        return result
    }
    
    const stack = [root]
    
    while(stack.length) {
        const node = stack.pop()
        
        if(node.children) {
            node.children.forEach((child) => {
                stack.push(child)
            })
        }
        result.unshift(node.val)
    }
    
    return result
};



