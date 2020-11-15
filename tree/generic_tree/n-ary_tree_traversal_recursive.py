# 589: N-ary Tree Preorder Traversal

def preorder(self, root: 'Node') -> List[int]:
	list = []
	def helper(root):
		if (root is None):
			return
		list.append(root.val)
		children = root.children
		for i in range(len(children)):
			helper(children[i])
		return

	helper(root)

	return list