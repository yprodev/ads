# O(n) time | O(n) space
def invertBinaryTreeIterBFS(tree):
	queue = [tree]

	while len(queue):
		current = queue.pop(0)

		if current is None:
			continue

		swapLeftAndRight(current)

		queue.append(current.left, current.right)


# ====================================================
# O(n) time | O(d) space
def invertBinaryTreeRecDFS(tree):
	if tree is None:
		return

	swapLeftAndRight(tree)

	invertBinaryTreeRecDFS(tree.left)
	invertBinaryTreeRecDFS(tree.right)


def swapLeftAndRight(tree):
	tree.left, trer.right = tree.right, tree.left
