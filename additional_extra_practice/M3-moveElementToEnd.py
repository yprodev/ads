# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
	leftPtr = 0
	rightPtr = len(array) - 1

	while leftPtr < rightPtr:
		# [2, 1, 2, 2, 2, 3, 4, 2]
		while leftPtr < rightPtr and array[rightPtr] == toMove:
			rightPtr -= 1

		if array[leftPtr] == toMove:
			array[leftPtr], array[rightPtr] = array[rightPtr], array[leftPtr]

		leftPtr += 1

	return array
