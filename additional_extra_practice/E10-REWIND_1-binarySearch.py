# O(log(n)) time | O(log(n)) space (because of recursion)
def binarySearchRec(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelperRec(array, target, left, right):
	if left > right:
		return -1;

	middle = (left + right) // 2
	potentialMatch = array[middle]

	if target > potentialMatch:
		return binarySearchHelperRec(array, target, middle + 1, right)
	elif target < potentialMatch:
		return binarySearchHelperRec(array, target, left, middle - 1)
	else:
		return middle

# --------------------------------------------------------------------
# O(log(n)) time | O(1) space
def binarySearchIter(array, target):
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]

		if target == potentialMatch:
			return middle
		if target > potentialMatch:
			left = middle + 1
		else:
			right = middle - 1

	return -1


