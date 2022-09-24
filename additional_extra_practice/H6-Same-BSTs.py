# O(n^2) time | O(n^2) space
def sameBSTs1(arrayOne, arrayTwo):
	# Should have the same number of nodes
	if len(arrayOne) != len(arrayTwo):
		return False

	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True

	# Should have the same root node
	if arrayOne[0] != arrayTwo[0]:
		return False

	leftOne = getSmaller(arrayOne)
	leftTwo = getSmaller(arrayTwo)
	rightOne = getBigger(arrayOne)
	rightTwo = getBigger(arrayTwo)

	return sameBSTs1(leftOne, leftTwo) and sameBSTs1(rightOne, rightTwo)


def getSmaller(array):
	smaller = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])

	return smaller


def getBigger(array):
	biggerOrEqual = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			biggerOrEqual.append(array[i])

	return biggerOrEqual

# ==============================================================================
# O(n^2) time | O(d) space
def sameBSTs2(arrayOne, arrayTwo):
	return areSameBSTs(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBSTs(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
	if rootIdxOne == -1 or rootIdxTwo == -1:
		return rootIdxOne == rootIdxTwo

	# Should have the same root value
	if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
		return False

	leftRootIdxOne = getIndexOfFirstSmallerValue(arrayOne, rootIdxOne, minVal)
	leftRootIdxTwo = getIndexOfFirstSmallerValue(arrayTwo, rootIdxTwo, minVal)
	rightRootIdxOne = getIndexOfFirstBiggerOrEqualValue(arrayOne, rootIdxOne, maxVal)
	rightRootIdxTwo = getIndexOfFirstBiggerOrEqualValue(arrayTwo, rootIdxTwo, maxVal)

	currentVal = arrayOne[rootIdxOne]

	leftAreSame = areSameBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentVal)
	rightAreSame = areSameBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, currentVal, maxVal)

	return leftAreSame and rightAreSame


def getIndexOfFirstSmallerValue(array, startIdx, minVal):
	for i in range(startIdx + 1, len(array)):
		if array[i] < array[startIdx] and >= minVal:
			return i

	return -1


def getIndexOfFirstBiggerOrEqualValue(array, startIdx, maxVal):
	for i in range(startIdx + 1, len(array)):
		if array[i] >= array[startIdx] and < maxVal:
			return i

	return -1
