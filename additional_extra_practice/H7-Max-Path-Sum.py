# O(n) time | O(log(n)) space (avg) OR O(n) space (worst)
def maxPathSum(tree):
	_, maxSum = findMaxSum(tree)

	return maxSum


def findMaxSum(tree):
	if tree is None:
		return (0, 0)

	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)

	# This could be a negative value
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

	value = tree.value
	maxSumAsBranch = max(maxChildSumAsBranch + value, value)

	# Triangle
	maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

	return (maxSumAsBranch, maxPathSum)

