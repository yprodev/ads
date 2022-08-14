// [AUTHOR] qwl5004
// [DESCRIPTION] No Fancy Algorithm, just Simple and Powerful In-Order Traversal
// [LINK] https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal

/*


This question appeared difficult to me but it is really just a simple in-order traversal! I got really frustrated when other people are showing off Morris Traversal which is totally not necessary here.

Let's start by writing the in order traversal:

private void traverse (TreeNode root) {
   if (root == null)
      return;
   traverse(root.left);
   // Do some business
   traverse(root.right);
}


So when we need to print the node values in order, we insert System.out.println(root.val) in the place of "Do some business".

What is the business we are doing here?
We need to find the first and second elements that are not in order right?

How do we find these two elements? For example, we have the following tree that is printed as in order traversal:

6, 3, 4, 5, 2

We compare each node with its next one and we can find out that 6 is the first element to swap because 6 > 3 and 2 is the second element to swap because 2 < 5.

Really, what we are comparing is the current node and its previous node in the "in order traversal".

Let us define three variables, firstElement, secondElement, and prevElement. Now we just need to build the "do some business" logic as finding the two elements. See the code below:

public class Solution {
    
    TreeNode firstElement = null;
    TreeNode secondElement = null;
    // The reason for this initialization is to avoid null pointer exception in the first comparison when prevElement has not been initialized
    TreeNode prevElement = new TreeNode(Integer.MIN_VALUE);
    
    public void recoverTree(TreeNode root) {
        
        // In order traversal to find the two elements
        traverse(root);
        
        // Swap the values of the two nodes
        int temp = firstElement.val;
        firstElement.val = secondElement.val;
        secondElement.val = temp;
    }
    
    private void traverse(TreeNode root) {
        
        if (root == null)
            return;
            
        traverse(root.left);
        
        // Start of "do some business", 
        // If first element has not been found, assign it to prevElement (refer to 6 in the example above)
        if (firstElement == null && prevElement.val >= root.val) {
            firstElement = prevElement;
        }
    
        // If first element is found, assign the second element to the root (refer to 2 in the example above)
        if (firstElement != null && prevElement.val >= root.val) {
            secondElement = root;
        }        
        prevElement = root;

        // End of "do some business"

        traverse(root.right);
}


*/


// ==========================================================================

// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] O(n)/O(1) Morris traversal, explained
// [LINK] https://leetcode.com/problems/recover-binary-search-tree/discuss/917430/Python-O(n)O(1)-Morris-traversal-explained

/*

If we want to traverse our tree and do not use any additional memory, than as far as I know, Morris traversal is the only way how to do it.

For more details about Morris traversal, you can look at oficial solution of problem 94: Binary Tree Inorder Traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/solution/.

Also, here we need to use variation of traversal, which keep the original structure of tree.

Let us use this traversal and use node is current node we are in and cands are candidates for our swapped nodes. We will look at oddities in inorder traversal: in BST all numbers will always increase. So, if in inorder traversal some value is less than previous, we need to keep and eye on this node. There can be two main cases:

    1. We have 1, 2, 3, 4, 5 and swapped nodes are adjacent, for example 1, 2, 4, 3, 5. In this case, we have only one oddity: 4 and 3: and we save them to our cands list. And we need to change values for the first and for the last nodes in our cands.
    2. We have 1, 2, 3, 4, 5 and swapped nodes are not adjacent, for example 1, 2, 5, 4, 3. In this case we have two oddities: 5 and 4; 4 and 3. In this case we again need to swap the first and the last nodes.

So, in both cases it is enough to run cands[0].val, cands[-1].val = cands[-1].val, cands[0].val to swap our nodes.

Complexity: time complexity is O(n): because we basically do Morris traverasal plus some additional O(n) operations. Space complexity is O(1), becauswe we again do Morris traversal and also we have node and cands, where cands can have maximum size 4.

class Solution:
    def recoverTree(self, root):
        cur, node, cands = root, TreeNode(-float("inf")), []
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if cur.val < node.val:
                        cands += [node, cur]
                    node = cur
                    cur = cur.right
            else:
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right
            
        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val

*/

// ==========================================================================

// [AUTHOR] leetcodegrindtt
// [DESCRIPTION] [C++] Clear Solution (with Explanation)
// [LINK] https://leetcode.com/problems/recover-binary-search-tree/discuss/423225/C%2B%2B-Clear-Solution-(with-Explanation)


/*

In an inorder traversal, nodes should go from smallest to largest, if not we know there is an issue.
For instance, if we have nodes 10 11 1 6 7 20 27, the inorder traversal should be
1 6 7 10 11 20 27. If it is anything else, you know two numbers are swapped. For instance, you could have:
1 7 6 10 11 20 27 (SITUATION 1), where two nodes sie by side are swapped, or 1 6 20 10 11 7 27 (SITUATION 2), where two nodes somewhere in the tree are flipped. We need to maintain a pointer to four locations:

The previous node. (prev)
The current node (root)
Our first flipped node (start)
Our second flipped node (end)
As we hit the first node in the inorder traversal, we mark it with prev (point prev to it). We then move onto the next node. This is when we want to start makiing the comparison. We then compare the previous node's value to the current node's value. So we'd compare 1 to 6. Since 6 is greater than 1, we continue. We compare 6 to 20. Since 20 is greater than 6, we continue. Then we get to 10, and 10 is less than 20, so we move our pointer to point to 20 as our first target. We set our second pointer (end) to the current node, since it may be the situation where the two flipped nodes are side by side (SITUATION 1). If that is NOT the case, our loop will be triggered again, and since our first pointer (start) is already occupied, our second pointer will now change to the second poorly placed node (SITUATION 2's 7)

class Solution {
private:
    
    void markTree(TreeNode* root, TreeNode*& prev, TreeNode*& first, TreeNode*& end) {
        if (!root) return;
        markTree(root->left, prev, first, end);
        if (prev) {
            if (root->val < prev->val) {
                if (!first) {
                    first = prev;
                }
                end = root;
            }
        }
        prev = root;
        markTree(root->right, prev, first, end);
    }
    
    
public:
    void recoverTree(TreeNode* root) {
        TreeNode *prev = nullptr, *first = nullptr, *end = nullptr;
        markTree(root, prev, first, end);
        swap(first->val, end->val);
        return;
    }
};

*/

// ==========================================================================

// [AUTHOR] 6996
// [DESCRIPTION] C++ || Easy to understand
// [LINK] https://leetcode.com/problems/recover-binary-search-tree/discuss/1962281/C%2B%2B-oror-Easy-to-understand


/*


If u use inorder traveral, problem will be find 2 mistakes in acending array and swap them
For example array: 1 2 3 4 5 6 7
-> swap random two elments -> 1 2 6 4 5 3 7 (swap 3 and 6)
-> Question is how can know 2 elements is 3 and 6?
-> First: find the first number have index i satisfy arr[i - 1] > arr[i] => first mistake have index i - 1 (in the exam, first mistake is 6)
-> Second: continue but don't change first mistake, if arr[i - 1] > arr[i] and u had found the first mistake => second mistake is i;
in the example second mistake in the first time is 4 change to 3

In the tree question, to keep compare, u need a variable is previous root.
By @LemonHerbs :
if we encounter a tree looking like this:

   5
  /   \
6     8
     /
     4

firstMistake will be assigned to 6, and in the same recursive call, secondMistake will be assigned to 5.
Then in the next recursive call, firstMistake will NOT be changed since it is not a null pointer, while secondMistake will be
updated to 4. Then in the following recursions the 2 mistake nodes remain unchanged.
When inorder() returns to the main function recoverTree(), the 2 mistakes swap values and hence the correct BST.


   5
  /   \
4     8
     /
     6


Code:


class Solution {
public:
    TreeNode* firstMistake, *secondMistake, *pre;
    void recoverTree(TreeNode* root) {
        pre = new TreeNode(INT_MIN);
        inorder(root);
        swap(firstMistake->val, secondMistake->val);
    }

    void inorder(TreeNode* root) {
        if(root == nullptr) 
            return;

        inorder(root->left);

        if(firstMistake == nullptr && root->val < pre->val)
            firstMistake = pre;
        if(firstMistake != nullptr && root->val < pre->val)
            secondMistake = root;
        pre = root;

        inorder(root->right);
    }
};

*/


// ==========================================================================

// [AUTHOR] akshit0699
// [DESCRIPTION] On paper explanantion,Well commented, easy understand
// [LINK] https://leetcode.com/problems/recover-binary-search-tree/discuss/671363/On-paper-explanantionWell-commented-easy-understand

// BETTER TO CHECK THE LINK

/*

CASE 1:
4, 15, 7, 10, 14, 5, 17
We reach 7, prev.val(15) >root.val(7) VIOLATION! Hence, found first.
first = 15(prev) and second = 7(root)
We go to 7,10,14... all obey the sorted order.
We reach 5, prev.val(14) > root.val(5) VIOLATION! Hence, found second.
second = 5 (root)
Everything else in the array is fine.
Swap first and second. Done!

Case 2:
4,5, 7, 10, 15, 14, 17
Reaches upto 15 safely.
Comes to 14, VIOLATION. Found first.
first = 15(prev) and second = 14(root)
Everything else works fine.
Swap first and second. Done!

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prevNode = None, None, None # Create three nodes.
        self.inOrder(root) # Calling the function
        self.first.val, self.second.val = self.second.val, self.first.val 
        # Swapping the two elements needed to be swapped
        
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        
        if self.prevNode: # To handle the case of first node, because we make it prev to begin with
            if self.prevNode.val > root.val: # Check property violation
                if not self.first: 
                    self.first = self.prevNode # Found first pair
                self.second = root # If the second pair is found then simply assign the smaller element of the   pair as the second guy, it works for single pair easily, as it wont get             updated again in that case.
                
        self.prevNode = root
        
        self.inOrder(root.right)

*/


