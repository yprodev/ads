# O(n) time | O(h) space (h - height / d - depth, possible O(d))
def nodeDepthsIter(root):
	sumOfDepths = 0
	stack = [{ "node": root, "depth": 0 }]

	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]

		if node is None:
			continue

		sumOfDepths += depth

		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})

	return sumOfDepths



# O(n) time | O(h) space (h - height / d - depth, possible O(d))
def nodeDepthsRecur(root, depth = 0):
	if root is None:
		return 0

	return depth + nodeDepthsRecur(root.left, depth + 1) + nodeDepthsRecur(root.right, depth + 1)
