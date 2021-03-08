

# ===================================================================================

# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: 3-4 lines Python

def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Maybe make it four lines for better readability:
def invertTree(self, root):
    if root:
        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left)
        return root

# And an iterative version using my own stack:
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root

# ===================================================================================

# [AUTHOR]: OldCodingFarmer
# [DESCRIPTION]: Python solutions (recursively, dfs, bfs).

# recursively
def invertTree1(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# BFS
def invertTree2(self, root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

# DFS
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.right, node.left])
    return root


# ===================================================================================

# [AUTHOR]: chammika
# [DESCRIPTION]: Recursive and non-recursive C++ both 4ms

# Recursive (C++)
"""
TreeNode* invertTree(TreeNode* root) {
    if (root) {
        invertTree(root->left);
        invertTree(root->right);
        std::swap(root->left, root->right);
    }
    return root;
}
"""

# Non-Recursive (C++)
"""
TreeNode* invertTree(TreeNode* root) {
    std::stack<TreeNode*> stk;
    stk.push(root);
    
    while (!stk.empty()) {
        TreeNode* p = stk.top();
        stk.pop();
        if (p) {
            stk.push(p->left);
            stk.push(p->right);
            std::swap(p->left, p->right);
        }
    }
    return root;
}
"""

# ===================================================================================

# [AUTHOR]: 
# [DESCRIPTION]: 


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Hard to implement iterative solution from scratch

# Recursive solution
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

# COPIED iterative solution
def invertTree(self, root):

	# Why we need stack?
	# Because we need to track the last element on each iteration
	stack = [root]

	while stack:
		# Why we need .pop()?
		# We need it because we need the last element added to the stack.
		# We can only work with one element at a time.
		node = stack.pop()

		if node:
			node.left, node.right = node.right, node.left
			stack += node.left, node.right

	# Why we return root?
	# Because we re-assign the left and right children
	return root



# COPIED interative BFS solution
def invertTree(self, root):
	queue = collections.deque([(root)])

	while queue:
		node = queue.popleft()

		if node:
			node.left, node.right = node.right, node.left
			queue.append(node.left)
			queue.append(node.right)

	return root



# COPIED interative DFS solution
def invertTree(self, root):
	stack = [root]

	while stack:
		node = stack.pop()

		if node:
			node.left, node.right = node.right, node.left
			stack.extend([node.left, node.right]) # Here the order does not matter

	return root




