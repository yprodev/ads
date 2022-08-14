"""
Input data:

[1, 2, 5, 7, 10, 12, 14, 20]

"""
# Implementation with inserting BST method
# O(n*log(n)) time | O(n) space
def minHeightBstWithInsert(array):
	return constructMinHeightBstWithInsert(array, None, 0, len(array) - 1)

def constructMinHeightBstWithInsert(array, bst, startIdx, endIdx):
	# Base case - Run out of values
	if endIdx < startIdx:
		return

	midIdx = (startIdx + endIdx) // 2

	valueToAdd = array[midIdx]

	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)

	constructMinHeightBstWithInsert(array, bst, startIdx, midIdx - 1)
	constructMinHeightBstWithInsert(array, bst, midIdx + 1, endIdx)

	return bst

# ------------------------------------------------------------------------------

# O(n) time | O(n) space
def minHeightBstManualInsertion(array):
	return constructMinHeightBstManualInsertion(array, None, 0, len(array) - 1)

def constructMinHeightBstWithInsert(array, bst, startIdx, endIdx):
	# Base case - Run out of values
	if endIdx < startIdx:
		return

	midIdx = (startIdx + endIdx) // 2

	newBstNode = BST(array[midIdx])

	if bst is None:
		bst = newBstNode
	else:
		if array[midIdx] < bst.value:
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right

	constructMinHeightBstManualInsertion(array, bst, startIdx, midIdx - 1)
	constructMinHeightBstManualInsertion(array, bst, midIdx + 1, endIdx)

	return bst


# ------------------------------------------------------------------------------
# Cleaner version


# O(n) time | O(n) space
def minHeightBstManualInsertionCleaner(array):
	return constructMinHeightBstManualInsertionCleaner(array, 0, len(array) - 1)

def constructMinHeightBstWithInsert(array, bst, startIdx, endIdx):
	# Base case - Run out of values
	if endIdx < startIdx:
		return None

	midIdx = (startIdx + endIdx) // 2

	newBstNode = BST(array[midIdx])
	newBstNode.left = constructMinHeightBstManualInsertionCleaner(array, startIdx, midIdx - 1)
	newBstNode.right = constructMinHeightBstManualInsertionCleaner(array, midIdx + 1, endIdx)

	return bst

# ------------------------------------------------------------------------------

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)




