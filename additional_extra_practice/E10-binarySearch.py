# O(log(n)) time | O(log(n)) space (because of recursion)
def binarySearchRec(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return -1;

	middle = (left + right) // 2

	potentialMatch = array[middle]

	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearchHelper(array, target, left, middle - 1)
	elif target > potentialMatch:
		return binarySearchHelper(array, target, middle + 1)

# =====================================================================

# O(log(n)) time | O(1) space
def binarySearchIter(array, target, left, right): # init with left = 0, and right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]

	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		right = middle - 1
	elif target > potentialMatch:
		left = middle + 1

	return -1


