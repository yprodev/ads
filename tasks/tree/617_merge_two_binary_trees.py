# [617] Merge Two binary 

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if t1 is None:
			return t2
		
		if t2 is None:
			return t1
		
		if t1 and t2 is None:
			return

		return TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))
# m - number of nodes

# Time complexity: O(m)
# Space complexity: O(m), possible O(log m)
