# [AUTHOR] lee215
# [DESCRIPTION] [C++/Java/Python] Self-Explained, 5-line, O(N)
"""
Intuition
	Don't need the condition of BST, just in-order output the whole tree.

	Straight forward idea here:
	result = inorder(root.left) + root + inorder(root.right)


Explanation
	Recursively call function increasingBST(TreeNode root, TreeNode tail)
	tail is its next node in inorder,
	（the word next may be easier to understand, but it’s a keyword in python)

	If root == null, the head will be tail, so we return tail directly.

	we recursively call increasingBST(root.left, root),
	change left subtree into the linked list + current node.

	we recursively call increasingBST(root.right, tail),
	change right subtree into the linked list + tail.

	Now the result will be in a format of linked list, with right child is next node.
	Since it's single linked list, so we set root.left = null.
	Otherwise it will be TLE for Leetcode judgment to traverse over your tree.

	The result now is increasingBST(root.left) + root + increasingBST(root.right).

	One tip here, we should arrange the old tree, not create a new tree.
	The leetcode judgment comparer only the values,
	so it won't take it as wrong answer if you return a new tree,
	but it is wrong.


Complexity
	O(N) time traversal of all nodes
	O(height) space
"""

# C++
"""
TreeNode* increasingBST(TreeNode* root, TreeNode* tail = NULL) {
    if (!root) return tail;
    TreeNode* res = increasingBST(root->left, root);
    root->left = NULL;
    root->right = increasingBST(root->right, tail);
    return res;
}
"""


# Java
"""
public TreeNode increasingBST(TreeNode root) {
    return increasingBST(root, null);
}

public TreeNode increasingBST(TreeNode root, TreeNode tail) {
    if (root == null) return tail;
    TreeNode res = increasingBST(root.left, root);
    root.left = null;
    root.right = increasingBST(root.right, tail);
    return res;
}
"""


# Python:
def increasingBST(self, root, tail = None):
    if not root: return tail
    res = self.increasingBST(root.left, root)
    root.left = None
    root.right = self.increasingBST(root.right, tail)
    return res

# ===================================================================================
# [AUTHOR] jeff4elee
# [DESCRIPTION] COMMENT on [C++/Java/Python] Self-Explained, 5-line, O(N)
# [NOTES]
"""
The most important thing to notice is that when we traverse left, the root is passed in, but when we traverse right, the tail is passed in.
In other words, traversing left passes in the current node to the next iteration, while traversing right passes in the current node's parent.
"""
def increasingBST(self, root, tail = None):
        
    # if this null node was a left child, tail is its parent
    # if this null node was a right child, tail is its parent's parent
    if not root: return tail

    # recursive call, traversing left while passing in the current node as tail
    res = self.increasingBST(root.left, root)

    # we don't want the current node to have a left child, only a single right child
    root.left = None

    # we set the current node's right child to be tail
    # what is tail? this part is important
    # if the current node is a left child, tail will be its parent
    # else if the current node is a right child, tail will be its parent's parent
    root.right = self.increasingBST(root.right, tail)

    # throughout the whole algorithm, res is the leaf of the leftmost path in the original tree
    # its the smallest node and thus will be the root of the modified tree
    return res

# ===================================================================================
# [AUTHOR] pvlkmrv
# [DESCRIPTION] COMMENT on [C++/Java/Python] Self-Explained, 5-line, O(N)
class Solution(object):
    # returns the root of an in-ordered tree
    # nxt points to the next-greatest thing so far explored, the next item in the in-order
    # traversal that has been seen so far. It starts off unknown, becomes the root.
    def increasingBST(self, root, nxt=None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Base case: If we run all the way down to None, then we can stop and just look at the
        # nxt node, because there are no longer any other nodes in the way.
        if not root: return nxt
        # If you go left nxt is the last node you were at. So at leaves, if you look at the left
        # None-child, you just get the leaf back as res.
        res = self.increasingBST(root.left, root)
        # If you go right, nxt is somewhere in the parentage of whatever you were just at, and
        # it shouldn't need to change. So at leaves, if you look at the right None-child, you
        # get back the thing that should appear after the leaf, and you can set it as the leaf's
        # .right.
        root.right = self.increasingBST(root.right, nxt)
        # The whole subtrees rooted at root.left and root.right have now been put in order, and
        # the left one references this (root) node, and this node references the smallest node
        # in the right in-order tree. So we are clear to remove the left reference from this node.
        root.left = None
        # res will hold the smallest-value node reached below this frame. Return it both so we
        # can properly assign root.right above and so that the initial call to this function gets
        # back the new root.
        return res

# ===================================================================================
# [AUTHOR] ZitaoWang
# [DESCRIPTION] Python solution
"""
Inorder traversal iterative:
"""
class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        trav = root
        prev = None
        stack = []
        while trav or stack:
            if trav:
                stack.append(trav)
                trav = trav.left
            else:
                u = stack.pop()
                if not prev: 
                    head = TreeNode(u.val)
                    head.left = None
                    prev = head
                else:
                    nex = TreeNode(u.val)
                    prev.right = nex
                    prev.left = None
                    prev = nex
                trav = u.right
        return head


# ===================================================================================
# [AUTHOR] noobie12
# [DESCRIPTION] Python -3 Approaches
# [NOTES]
# IDEA 1: Do in-order traversal & then construct tree from the output OR do both simultaneously
# IDEA 2: Recursion based Implementation

# Appraoch 1: First doing in-order and then constructing the tree

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.inorder(root)
        head = TreeNode(result[0])
        current = head
        for i in range(1, len(result)):
            current.right = TreeNode(result[i])
            current = current.right
        return head
        
    def inorder(self, root: TreeNode) -> List:
        result, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result

# Approach 2: Do it simultaneously (iteratively)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        stack = []
        head, current = None, None
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            if head is None:
                head = TreeNode(node.val)
                current = head
            else:
                current.right = TreeNode(node.val)
                current = current.right
            if node.right:
                stack.append(node.right)
                node = node.right
                while node.left:
                    stack.append(node.left)
                    node = node.left
        return head

# Approach 3: Recursive
class Solution:
	def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
		if not root: 
			return tail
		result = self.increasingBST(root.left, root)
		root.left = None
		root.right = self.increasingBST(root.right, tail)
		return result

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] Re-used already existing solution
# Issues:
#	Really hard to understand how to do asymetric tree recursively...
#   We definitely need to use Inorder traversal to got to left side
#   first and set Left to None.
#   While we are setting the root.left to None, we need to assign
#   the next step to each root.right to have ability to move through
#   the rigth side of the Tree.
#   We need to get the previous node while traversing. So, we use tail
#   argument to store it on each execution stack frame. We need to manage
#   base case where we actually handle the previous node.
#   Need to set a default value for the tail on the arguments level,
#   because at some point we need to assign value None to root.left.

class Solution:
    def increasingBST(self, root: TreeNode, tail: TreeNode = None) -> TreeNode:
        if not root:
            return tail
        
        result = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        
        return result