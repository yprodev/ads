#!/usr/bin/env python3

# [617] Merge Two binary trees

class BTreeNode:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

class BTree:
	def __init__(self, root):
		self.root = BTreeNode(root)

	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(self.root, "")
		elif traversal_type == "inorder":
			return self.inorder_print(self.root, "")
		elif traversal_type == "postorder":
			return self.postorder_print(self.root, "")
		else:
			print("Traversal type: " + str(traversal_type) + " is not suppurted.")
			return False

	def preorder_print(self, start, traversal):
		if start is not None:
			traversal += (str(start.value) + "-")
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def inorder_print(self, start, traversal):
		if start is not None:
			traversal = self.preorder_print(start.left, traversal)
			traversal += (str(start.value) + "-")
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def postorder_print(self, start, traversal):
		if start is not None:
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
			traversal += (str(start.value) + "-")
		return traversal


tree = BTree(1)
tree.root.left = BTreeNode(3)
tree.root.right = BTreeNode(4)
tree.root.left.left = BTreeNode(7)
tree.root.left.right = BTreeNode(8)
tree.root.right.left = BTreeNode(10)
tree.root.right.right = BTreeNode(12)

print(tree.print_tree("inorder"))






