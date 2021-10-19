# Average: 	O(log(n)) time	| O(log(n)) space
# Worst: 	O(n) time		| O(n) space
def findClosestValueInBST1(tree, target):
	return findClosestValueInBSTHelperRecursive(tree, target, float('inf'))


def findClosestValueInBSTHelperRecursive(tree, target, closest):
	if tree is None:
		return closest

	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value

	if target < tree.value:
		return findClosestValueInBSTHelperRecursive(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBSTHelperRecursive(tree.right, target, closest)
	else:
		return closest

# ================================================================================

# Average: 	O(log(n)) time	| O(1) space
# Worst: 	O(n) time		| O(1) space
def findClosestValueInBST2(tree, target):
	return findClosestValueInBSTHelperIterative(tree, target, float('inf'))


def findClosestValueInBSTHelperIterative(tree, target, closest):
	currentNode = tree

	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value

		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break

	return closest

